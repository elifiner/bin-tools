#!/bin/sh

if [ "$1" == "" ]; then
    echo "usage: $0 <file>"
    exit 1
fi

FILENAME=$1
BASENAME={$1%.*}

ffmpeg -y -i $FILENAME -vn -acodec copy $BASENAME.aac
ffmpeg -y -i $BASENAME.aac -sample_fmt s16 -ar 8000 $BASENAME.mp3
