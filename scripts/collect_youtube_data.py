"""
collect_youtube_data.py

Collects video metadata from the YouTube Data API.

Author: Kellie J. Leopold
Project: Social Media Analytics Capstone
"""

import html
import os
from pathlib import Path
from typing import Any

import pandas as pd

from dotenv import load_dotenv
from googleapiclient.discovery import build


def load_api_key() -> str:
    """
    Load the YouTube API key from the project's .env file.

    Returns:
        str: The YouTube Data API key.

    Raises:
        ValueError: If the API key cannot be found.
    """
    project_root = Path(__file__).resolve().parents[1]
    load_dotenv(project_root / ".env")

    api_key = os.getenv("YOUTUBE_API_KEY")

    if not api_key:
        raise ValueError("YOUTUBE_API_KEY was not found in the .env file.")

    return api_key


def create_youtube_client(api_key: str):
    """
    Create an authenticated YouTube Data API client.

    Args:
        api_key: YouTube Data API key.

    Returns:
        Resource: Authenticated YouTube API client.
    """
    return build(
        serviceName="youtube",
        version="v3",
        developerKey=api_key,
    )


def search_videos(
    youtube,
    query: str,
    max_results: int = 5,
) -> list[dict[str, Any]]:
    """
    Search YouTube for videos and return structured metadata.

    Args:
        youtube: Authenticated YouTube API client.
        query: Search term.
        max_results: Maximum number of videos to return.

    Returns:
        list[dict[str, Any]]: A list of dictionaries containing
        video metadata.
    """
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_results,
    )

    response = request.execute()

    videos = []

    for item in response["items"]:
        video = {
            "video_id": item["id"]["videoId"],
            "title": html.unescape(item["snippet"]["title"]),
            "description": html.unescape(
                item["snippet"]["description"]
            ),
            "channel_title": item["snippet"]["channelTitle"],
            "published_at": item["snippet"]["publishedAt"],
        }

        videos.append(video)

    return videos

def save_to_csv(
    videos: list[dict[str, Any]],
    output_file: Path,
) -> pd.DataFrame:
    """
    Save collected video metadata to a CSV file.

    Args:
        videos: List of video metadata dictionaries.
        output_file: Path to the output CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the collected data.
    """
    df = pd.DataFrame(videos)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_file, index=False)

    return df

def main():
    """Run the YouTube data collection script."""

    print("Loading API key...")

    api_key = load_api_key()
    print("✅ API key loaded successfully.")

    youtube = create_youtube_client(api_key)
    print("✅ Connected to the YouTube Data API.")

    videos = search_videos(
        youtube=youtube,
        query="data analytics",
        max_results=5,
    )

    project_root = Path(__file__).resolve().parents[1]

    output_file = (
        project_root
        / "data"
        / "raw"
        / "youtube_search_results.csv"
    )

    df = save_to_csv(
        videos=videos,
        output_file=output_file,
    )

    print(f"\n✅ Saved {len(df)} videos to:")
    print(output_file)

    print("\nDataset Preview:\n")
    print(df)

if __name__ == "__main__":
    main()