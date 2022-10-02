#!/bin/bash

#load the file covid_19_data.csv from ../data to variable csvfile
csvfile=../data/covid_19_data.csv

#convert the case to upper case in csv file
csvfile=$(echo $csvfile | tr '[:lower:]' '[:upper:]')

#remove column one from csvfile
cut -d, -f1 --complement $csvfile > ../data/covid_19_data_clean.csv
