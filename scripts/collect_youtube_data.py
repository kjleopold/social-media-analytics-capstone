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
        The YouTube API key.

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
    Search YouTube for videos.
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


def get_video_statistics(
    youtube,
    video_ids: list[str],
) -> dict[str, dict[str, Any]]:
    """
    Retrieve statistics and content details for videos.
    """

    request = youtube.videos().list(
        part="statistics,contentDetails",
        id=",".join(video_ids),
    )

    response = request.execute()

    statistics: dict[str, dict[str, Any]] = {}

    for item in response["items"]:
        statistics[item["id"]] = item

    return statistics


def enrich_videos(
    videos: list[dict[str, Any]],
    statistics: dict[str, dict[str, Any]],
) -> None:
    """
    Merge video statistics into each video dictionary.
    """

    for video in videos:

        stats = statistics.get(video["video_id"])

        if not stats:
            continue

        video["view_count"] = int(
            stats["statistics"].get("viewCount", 0)
        )

        video["like_count"] = int(
            stats["statistics"].get("likeCount", 0)
        )

        video["comment_count"] = int(
            stats["statistics"].get("commentCount", 0)
        )

        video["favorite_count"] = int(
            stats["statistics"].get("favoriteCount", 0)
        )

        video["duration"] = (
            stats["contentDetails"]["duration"]
        )

        video["definition"] = (
            stats["contentDetails"]["definition"]
        )

        video["caption"] = (
            stats["contentDetails"]["caption"]
        )


def save_to_csv(
    videos: list[dict[str, Any]],
    output_file: Path,
) -> pd.DataFrame:
    """
    Save collected videos to a CSV file.
    """

    df = pd.DataFrame(videos)

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        output_file,
        index=False,
    )

    return df


def main():
    """Run the YouTube data collection pipeline."""

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

    video_ids = [
        video["video_id"]
        for video in videos
    ]

    statistics = get_video_statistics(
        youtube=youtube,
        video_ids=video_ids,
    )

    enrich_videos(
        videos=videos,
        statistics=statistics,
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