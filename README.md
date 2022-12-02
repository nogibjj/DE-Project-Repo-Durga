## Project 4 - Movies Microservice

Movies Microservice that returns a JSON payload and SQLite as Backend DB, 
Used FLask for the Microservice and containerized it using Docker and built CI/CD on AWS.

### Project Objectives:

* Create a Microservice that returns a JSON payload and performs a Data Engineering related task
* Push tested source code to Github and perform Continuous Integration with Github Actions (or similar SaaS Build service)
* Build Continuous Delivery of Flask/FastAPI Data Engineering API on AWS

## Project Architecture
<img width="579" alt="image" src="https://user-images.githubusercontent.com/105465968/205199704-c69b26b5-049b-4988-a1fc-20d36d67f852.png">


## Setup
| File  | Description  |   
|---|---|
| [.devcontainer]()  |    Setup Docker Container. Using Debian as the OS, and customized required extensions in devcontainer.json file. <br /> |  
|[requirements.txt]()   |   Contains the prerequisite packages that need to be installed before running this project.<br /> |   
| [Makefile]()  |   Purpose is to install packages, test the project and to lint and format the files.<br /><br /> |   


<b>MakeFile Usage</b><br /><br />
```make install```to install, <br />
```make test```to test,<br />
```make lint```to lint,<br />
```make all```to perform all the above tasks.
<br /><br />


### Dockerfile:
1. Create a Dockerfile to package the application and all its dependencies in a virtual container - populated the Dockerfile file using FastAPI library
2. Build the Dockerfile
3. Run the Dockerfile

```docker build .```  
```docker image ls```  
```docker run -p 127.0.0.1:8080:<img>```  

### Deploy with AWS 
The following variables are used to open connection with the AWS and saved in the secrets section of the Github project.
- ```AWS_ACCESS_KEY_ID```
- ```AWS_SECRET_ACCESS_KEY```

Create a fully-managed Docker container registry using ECR which will make it easy to store, manage, and deploy Docker container images.
Use AWS CodeBuild to build and test the Docker image (for continuous delivery)


