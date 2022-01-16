#!/bin/bash

# Created by Koutyan.S (https://tech.kosukelab.com/)
# This is sub program for creating send messages.

source ./bot_config.py

MC_LOG="/var/lib/docker/containers/${CONTAINER_ID}/${CONTAINER_ID}-json.log"

LOG_FILE="./discordbot.log"
LOG_BAK_FILE="./discordbot_bak.log"
OUTPUT_FILE="./login_check_result"

sudo tail -n 1 $MC_LOG > $LOG_FILE
diff_result=`diff $LOG_FILE $LOG_BAK_FILE`

if [ -n "$diff_result" ]; then
  cat $LOG_FILE | while read line
  do
    if [[ $line =~ "connected" ]]; then
      cat $LOG_FILE | awk -F'[:,]' '{print $5,$6}' | awk -F'[]]' '{print $2}' > $OUTPUT_FILE
    fi
  done
  cp $LOG_FILE $LOG_BAK_FILE
else
  rm $OUTPUT_FILE && touch $OUTPUT_FILE
fi