# IDS 706 Project 1 - Onilne Banking Data Analysis on Azure Databricks Cluster
 
## About Project
In this project, we try to analyze online banking data by querying the db. Cluster is hosted on Microsoft Azure Cluster via Databricks. 
There are two ways we can query:
1. Using the API 
2. Using the CLI

## Diagram
![Diagram](Diagram.png)

## Setup
[.devcontainer]() - Setup Docker Container. Using Debian as the OS, and customized required extensions in devcontainer.json file. <br />
[requirements.txt]() - Contains the prerequisite packages that need to be installed before running this project.<br />
[Makefile]()  - Purpose to install packages, test the project and to lint and format.<br /><br />
<b>Usage</b><br /><br />
```make install```to install, <br />
```make test```to test,<br />
```make lint```to lint,<br />
```make all```to perform all the above tasks.
<br /><br />
DataBricks Configuration
The following variables are used to open connection with the Databricks cluster and saved in the secrets section of the Github project.
- ```DATABRICKS_HOST```
- ```DATABRICKS_HTTP_PATH```
- ```DATABRICKS_SERVER_HOSTNAME```
- ```DATABRICKS_TOKEN```

To test the connectivity,  ```databricks-cli``` can be used, please execute the following command:
```
databricks clusters list --output JSON | jq
```

## Query package
This project contains a package [dblib](https://github.com/nogibjj/ids-706-project-1-chang/tree/main/dblib) that connects with and executes queries to the Databricks database.

## CLI interface
This project uses ```click``` to build a CLI interface from which users can execute queries. Use the following command.

```
./query.py cli-query
```

or

```
./query.py cli-query <--query QUERYTEXT>
```

## FastAPI inferface
This project also uses ```FastAPI``` to build a microservice that enables users to query in a RESTful way. Use the following command to start the service.

```
./app.py
```

Then visit the prompted URL, and you will see a welcome message. Attach ```/query``` to the end of the URL. You will see the query result.

## CI/CD
This project uses GitHub Actions. It is built upon each push.
