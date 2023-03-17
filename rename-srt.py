#!/usr/bin/python
import os
import sys

if len(sys.argv) < 2:
    print("usage: {} <*.srt> <*.mkv>".format(sys.argv[0]))
    sys.exit(1)

extensions = {}
for file in sys.argv[1:]:
    ext = os.path.splitext(file)[1]
    if ext not in extensions:
        extensions[ext] = []
    extensions[ext].append(file)

if len(extensions) != 2:
    print('error: bad arguments, expected two lists of files')
    sys.exit(1)

subtitles, videos = extensions.values()

if len(subtitles) !=  len(videos):
    print('error: different number of subtitle and video files')
    sys.exit(1)

for (subtitle, video) in zip(sorted(subtitles), sorted(videos)):
    newname = os.path.splitext(video)[0] + '.srt'
    print('{} -> {}'.format(subtitle, newname))
    os.rename(subtitle, newname)
