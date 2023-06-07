from fastapi import FastAPI, Header
from typing import Annotated
from bardapi import Bard
from pydantic import BaseModel
from surrealdb import Surreal
import requests
import pickle5 as pickle
import json

class Query(BaseModel):
    q: str
    ctx: list[str]|None
    cid: str|None

def load_context(bard:Bard, ctx:list[str]):
    print(ctx)
    prompt_template = """
    Read all the information available on the following web pages.
    Be prepared to answer detailed questions which require synthesizing this information into original solutions.
    """
    for url in ctx:
        prompt_template += f'\n{ctx}'
    print(prompt_template)
    init_answer = bard.get_answer(prompt_template)['content']
    print(init_answer)

app = FastAPI()

@app.post("/ask")
async def ask_bard(query: Query, authorization: Annotated[str | None, Header()] = None):
    async with Surreal("ws://localhost:8080/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("test", "test")
        token=authorization

        session = requests.Session()
        session.headers = {
                    "Host": "bard.google.com",
                    "X-Same-Domain": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "Origin": "https://bard.google.com",
                    "Referer": "https://bard.google.com/",
                }
        session.cookies.set("__Secure-1PSID", token)
        existing = {}
        if query.cid != None:
            existing = await db.select(f'session:{query.cid}')
        if existing == {}:
            bard = Bard(token=token, session=session, timeout=30)
            if query.ctx != None:
                load_context(bard, query.ctx)
            response = bard.get_answer(query.q)
            cid = response['conversation_id']
            answer = response['content']
            hex = pickle.dumps(bard).hex()
            await db.query(f'CREATE session:{cid} SET bard = "{hex}"')
            return json.dumps({'answer': answer, 'cid': cid})
        else:
            hex = existing['bard']
            print(hex)
            print(type(hex))
            bard = pickle.loads(bytes.fromhex(hex))
            response = bard.get_answer(query.q)
            cid = response['conversation_id']
            answer = response['content']
            hex = pickle.dumps(bard).hex()
            await db.query(f'UPDATE session:{cid} SET bard = "{hex}"')
            return json.dumps({'answer': answer, 'cid': cid})