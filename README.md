# bardchat-python

A back end application you can run locally to interact with a desktop build of bardchat-flutter.
Cloud deployment code coming soon.

# Instructions

If you don't already have them installed on your local system, install Docker and Docker Compose.
Here is a decent tutorial for how to do it on [Ubuntu](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-install-Docker-and-docker-compose-on-Ubuntu). 

From there, simply download the docker-compose.yaml file into a directory of your choice,
cd into that directory, and run
```
docker compose up
```
If you get a permission error, simply add 'sudo' to the beginning of the command.
This back end has so far only been tested on Linux, but Windows instructions should be coming soon.
