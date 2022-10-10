#!/bin/bash

#load the file covid_19_data.csv from ../data to variable csvfile
csvfile=../data/covid_19_data.csv
scripts/logs.sh info "Transforming the data"

/home/vscode/.venv/bin/python /workspaces/DE-Project-Repo-Durga/scripts/transform.py

scripts/logs.sh info "Moving the data to data folder: ../data/covid_19_data_transformed.csv"

