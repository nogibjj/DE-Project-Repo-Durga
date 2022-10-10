#!/bin/bash

#read a csv file and extract data from it
extract() {
#call kaggle api to download the data from kaggle to the data folder
scripts/logs.sh info "Downloading from kaggle"
kaggle datasets download -d 'sudalairajkumar/novel-corona-virus-2019-dataset' -p ../data

#unzip the data if it is downloaded as a zip file
scripts/logs.sh info "Unzipping the data"
unzip ../data/novel-corona-virus-2019-dataset.zip -d ../data
#remove the zip file
rm ../data/novel-corona-virus-2019-dataset.zip

scripts/logs.sh info "Extracting the data"
#read the csv file
csvfile=../data/covid_19_data.csv

}
#call the function  
extract


