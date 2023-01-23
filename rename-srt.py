#!/usr/bin/python
import os
import re
import sys
import glob

if len(sys.argv) < 3:
    print("usage: {} '*.srt' '*.mkv'".format(sys.argv[0]))
    sys.exit(1)

subtitles = glob.glob(sys.argv[1])
videos = glob.glob(sys.argv[2])

for (subtitle, video) in zip(sorted(subtitles), sorted(videos)):
    print(subtitle, video)
    newname = re.sub('\.\w+$', '.srt', video)
    os.rename(subtitle, newname)
