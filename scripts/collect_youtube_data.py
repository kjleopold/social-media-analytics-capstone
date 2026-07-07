"""
collect_youtube_data.py

Connects to the YouTube Data API and verifies that the API key works.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from googleapiclient.discovery import build

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

# check if the .env file exists in the project root directory
project_root = Path(__file__).resolve().parents[1]
load_dotenv(project_root / ".env")

#check if the YOUTUBE_API_KEY environment variable is set
api_key = os.getenv("YOUTUBE_API_KEY")

# check if the API key is loaded successfully
if api_key:
    print("API key loaded successfully.")
else:
    print("API key not found.")

# --------------------------------------------------
# Connect to the YouTube Data API
# --------------------------------------------------

# Import the necessary libraries
youtube = build(
    "youtube",
    "v3",
    developerKey=api_key,
)

print("Connected to the YouTube Data API.")

# --------------------------------------------------
# Perform a simple search
# --------------------------------------------------

# Perform a search for videos related to "data analytics"
request = youtube.search().list(
    q="data analytics",
    part="snippet",
    type="video",
    maxResults=5,
)

response = request.execute()

print("\nSearch Results:\n")

for index, item in enumerate(response["items"], start=1):
    print(f"{index}. {item['snippet']['title']}")

