#!/bin/sh
for file in "$@"; do
	ffmpeg -i "$file" -c:v libx264 -tag:v avc1 -movflags faststart -crf 30 -preset superfast -progress -v -y "$file".small.mp4
done
