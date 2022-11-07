# Google Trends Analysis on SQLITE

## Project Architecture
<img width="402" alt="image" src="https://user-images.githubusercontent.com/105465968/200236085-851fee97-3055-427d-bddb-d7bf8b265335.png">

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

<b>Sqllite DB:</b><br /><br />
1. Created Trends DB locally<br />
2. Inserted Data from Kaggle Dataset csv file into Trends db<br />
3. Query and draw insights

## Queries:
1. Top Trends by year
2. Top Trends in 2020 
3. Top searched queries by Location
4. Top searched movies in 2020 
5. Top Searched words in 2020 and 2019 repeating in multiple categories or locations 
<img width="827" alt="image" src="https://user-images.githubusercontent.com/105465968/200237124-8bcf283f-d5d6-4a84-a5d4-2f1c8fb9f25d.png">







