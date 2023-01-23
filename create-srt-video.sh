#!/bin/sh
if [ "$4" == "" ]; then
    echo "usage: $0 <image.jpg> <audio.mp3> <subtitle.srt> <target.mp4>"
    exit 1
fi

ffmpeg \
    -r 1 -loop 1 -i "$1" \
    -i "$2" -acodec copy -r 1 -shortest \
    -vf "subtitles=$3:force_style='Fontsize=24,PrimaryColour=&Hffffff&'" \
    "$4"

