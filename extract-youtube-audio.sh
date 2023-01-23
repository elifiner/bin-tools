#!/bin/sh

if [ "$1" == "" ]; then
    echo "usage: $0 <url>"
    exit 1
fi

FILENAME=$(youtube-dl -f worstaudio --get-filename -o '%(id)s.%(ext)s' "$1")
youtube-dl -f worstaudio -o $FILENAME "$1"

ffmpeg -y -i $FILENAME -vn -acodec copy $FILENAME.aac
ffmpeg -y -i $FILENAME.aac -sample_fmt s16 -ar 8000 FILENAME.mp3
