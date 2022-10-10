#!/bin/bash

# This script is used to run the application

scripts/logs.sh info "Running the application"

scripts/logs.sh info "Calling the extract module"
scripts/extract.sh

scripts/logs.sh info "Calling the transform module"
scripts/transform.sh

scripts/logs.sh info "Calling the load module"
/home/vscode/.venv/bin/python /workspaces/DE-Project-Repo-Durga/scripts/loadTable.py

