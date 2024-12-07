#!/bin/sh
"exec" "`dirname $0`/venv/bin/python" "$0" "$@"
import os
import dotenv
import assemblyai as aai
import argparse
from tqdm import tqdm

dotenv.load_dotenv()

# Set up argument parser
parser = argparse.ArgumentParser(description='Transcribe audio file with speaker labels')
parser.add_argument('file_path', help='Path to the audio file to transcribe')
args = parser.parse_args()

# Get file size for progress bar
file_size = os.path.getsize(args.file_path)

# Initialize AssemblyAI
aai.settings.api_key = os.getenv('ASSEMBLY_API_KEY')
config = aai.TranscriptionConfig(speaker_labels=True)

# Create progress bar and read file
with open(args.file_path, 'rb') as audio_file:
    with tqdm(total=file_size, unit='B', unit_scale=True, desc='Uploading') as pbar:
        data = b''
        while chunk := audio_file.read(8192):  # Read in 8KB chunks
            data += chunk
            pbar.update(len(chunk))

# Transcribe with loaded data
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
    data,
    config=config
)

# Print results
for utterance in transcript.utterances:
    print(f"Speaker {utterance.speaker}: {utterance.text}")
