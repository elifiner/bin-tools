#!/bin/bash
if [ "$1" == "" ]; then
    echo "usage: $0 <movie>"
    exit 1
fi

ffmpeg -i "$1" -c copy -map 0:s:0 "${1%%.*}".srt
