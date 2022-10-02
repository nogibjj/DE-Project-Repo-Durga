#!/bin/bash

#load the file covid_19_data.csv from ../data to variable csvfile
csvfile=../data/covid_19_data.csv
./logs.sh info "Transforming the data"
#convert the case to upper case in csv file
csvfile=$(cat $csvfile | tr '[:lower:]' '[:upper:]')
cat $csvfile
./logs.sh info "Moving the data to data folder: ../data/covid_19_data_clean.csv"
