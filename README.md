# IDS 706 Project 2 - ETL Pipeline for Covid Data on Azure Databricks Cluster
 
## About Project
Cluster is hosted on Microsoft Azure Cluster via Databricks. We perform the Extract, Transform and Load Operations on Covid Data obtained from Kaggle CLI

This Project could be run with:
BASH CLI

## Project Architecture


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

## DataBricks Configuration
The following variables are used to open connection with the Databricks cluster and saved in the secrets section of the Github project.
- ```DATABRICKS_HOST```
- ```DATABRICKS_HTTP_PATH```
- ```DATABRICKS_SERVER_HOSTNAME```
- ```DATABRICKS_TOKEN```

<br/>To test the connectivity,  ```databricks-cli``` can be used, please execute the following command:
```
databricks clusters list --output JSON | jq
```

## CLI 
This project uses ```bash```  scripts to execute the ETL operations. Use the following command.

```
./run.sh
```

The script ```run.sh``` calls the below commands internally to execute ETL:
```
scripts/extract.sh
```
```
scripts/transform.sh
```
```
scripts/loadTable.py
```

## CI/CD
Github Actions are enabled to automatically build and test for continuous integration and deployment.


