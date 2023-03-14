#!/bin/bash

if [ "$1" == "" ]; then
    echo "usage: $0 <file>"
    exit 1
fi

FILENAME="$1"
BASENAME=${1%.*}

ffmpeg -y -i "$FILENAME" -vn -ac 1 -ar 32000 "$BASENAME.low.mp3"
