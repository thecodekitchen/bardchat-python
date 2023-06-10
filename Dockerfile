FROM python:3.10
WORKDIR /code


RUN pip install --no-cache-dir fastapi uvicorn
RUN pip install --no-cache-dir git+https://github.com/thecodekitchen/Bard-API.git
RUN pip install --no-cache-dir surrealdb pickle5
COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]