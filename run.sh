#!/bin/bash

# This script is used to run the application

scripts/logs.sh info "Running the application"

scripts/logs.sh info "Calling the extract module"
scripts/extract.sh

scripts/logs.sh info "Calling the transform module"
scripts/transform.sh

scripts/logs.sh info "Calling the load module"
scripts/load.sh

