#!/bin/sh
"exec" "`dirname $0`/venv/bin/python" "$0" "$@"
import os
import sys
import argparse
import dotenv
import openai

# Load environment variables from .env file
dotenv.load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up argparse to parse command line arguments
parser = argparse.ArgumentParser(description="Call OpenAI API")
parser.add_argument("prompt", help="The prompt to send to the API")
parser.add_argument("--model", default="text-davinci-003", help="The name of the model to use (default: text-davinci-003)")
parser.add_argument("--temperature", type=float, default=0.7, help="The sampling temperature to use (default: 0.7)")
parser.add_argument("--max-tokens", type=int, default=2048, help="The maximum number of tokens to generate (default: 2048)")
args = parser.parse_args()

# Read additional data from stdin
data = sys.stdin.read()

# Call the OpenAI API with the prompt and parameters
response = openai.Completion.create(
    engine=args.model,
    prompt=args.prompt + data,
    temperature=args.temperature,
    max_tokens=args.max_tokens,
)

# Print the response from the API
print(response.choices[0].text.strip())
