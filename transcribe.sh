#!/bin/sh
. .env
curl --request POST \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  --upload-file "$1" \
  --url 'https://api.deepgram.com/v1/listen?model=whisper' \
  --output "$1".json
jq -r '.results.channels[0].alternatives[0].transcript' "$1".json > "$1".txt
echo "$1".txt
