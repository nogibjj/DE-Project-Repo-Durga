#!/bin/bash
# This script is used to create a log file for the script
# Create a log file
LOGFILE=./logs/$(basename $0).log
# Create a log file if it does not exist
touch $LOGFILE
echo "$(date)" >> $LOGFILE
echo "" >> $LOGFILE
#write a log entry
log() {
echo "$(date) - $1" >> $LOGFILE
}
#write error log method to log file
error_log() {
echo "$(date) - ERROR: $1" >> $LOGFILE
}
#write debug log method to log file
debug_log() {
echo "$(date) - DEBUG: $1" >> $LOGFILE
}
#write info log method to log file
info_log() {
echo "$(date) - INFO: $1" >> $LOGFILE
}
#write warning log method to log file
warning_log() {
echo "$(date) - WARNING: $1" >> $LOGFILE
}
#write fatal log method to log file
fatal_log() {
echo "$(date) - FATAL: $1" >> $LOGFILE
}