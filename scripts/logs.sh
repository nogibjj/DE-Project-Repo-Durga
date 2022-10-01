#!/bin/bash
# This script is used to create a log file for the script
# Create a log file
LOGFILE=/workspaces/DE-Project-Repo-Durga/logs/application.log
# Create a log file if it does not exist
touch $LOGFILE
# Check if the log file is writable
if [ ! -w $LOGFILE ]; then
    echo "Cannot write to $LOGFILE. Please check permissions."
    exit 1;
fi
#write a log entry

info_log() {
echo "$(date) - $@" >> $LOGFILE
}
#write error log method to log file
error_log() {
echo "$(date) - ERROR: $@" >> $LOGFILE
}
#write debug log method to log file
debug_log() {
echo "$(date) - DEBUG: $@" >> $LOGFILE
}
#write info log method to log file
info_log() {
echo "$(date) - INFO: $@" >> $LOGFILE
}
#write warning log method to log file
warning_log() {
echo "$(date) - WARNING: $@" >> $LOGFILE
}
#write fatal log method to log file
fatal_log() {
echo "$(date) - FATAL: $@" >> $LOGFILE
}

#take parameters and call the appropriate log method    
log_entry() {
case $1 in
error)
error_log ${@:2}
;;
debug)
debug_log ${@:2}
;;
info)
info_log ${@:2}
;;
warning)
warning_log ${@:2}
;;
fatal)
#fatal_log all parameters except the first one
fatal_log ${@:2}
;;
*)
echo "Invalid log type"
;;
esac
}

#take parameters and call the appropriate log method 
log_entry $1 $2
