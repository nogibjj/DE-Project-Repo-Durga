#!/bin/bash

# This script is used to extract data from a csv file

#read a csv file and extract data
extract() {
$data = $(cat $1)
./scripts/logs.sh info_log "Extracting data from $1"
echo $data
}
