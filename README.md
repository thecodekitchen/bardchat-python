# bardchat-python

A back end application you can run locally to interact with a desktop build of [bardchat-flutter](https://github.com/thecodekitchen/bardchat-flutter).
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

To start the back end concurrently with the front end, follow the optional step 3.5 in the readme at [bardchat-flutter](https://github.com/thecodekitchen/bardchat-flutter).

To run this application on a managed Kubernetes cluster using Azure Kubernetes Service, Elastic Kubernetes Service, or Google Kubernetes Engine, you can clone the template on my [terraform-k8s-example](https://github.com/thecodekitchen/terraform-k8s-example) repo to your own account and follow the instructions in the readme for deploying a kubernetes manifest. I included a k8s-manifest.yml for a deployment of this app as an example deployment, so you won't need to configure any networking. Just authenticate the Github repo with your desired cloud platform, fill in the secrets and variables as instructed, and run the deploy action for your desired platform.
