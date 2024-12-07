#!/bin/sh
"exec" "`dirname $0`/venv/bin/python" "$0" "$@"
import os
import dotenv
import assemblyai as aai

dotenv.load_dotenv()

# Replace with your API token
aai.settings.api_key = os.getenv('ASSEMBLY_API_KEY')

# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

config = aai.TranscriptionConfig(speaker_labels=True)

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
  FILE_URL,
  config=config
)

for utterance in transcript.utterances:
  print(f"Speaker {utterance.speaker}: {utterance.text}")
