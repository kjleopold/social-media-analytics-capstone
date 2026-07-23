"""
collect_youtube_metadata.py

Collect video metadata from the YouTube Data API.

Author: Kellie J. Leopold
Project: Social Media Analytics Capstone
"""

from datetime import datetime
import html
import os
from pathlib import Path
from typing import Any

import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import Resource, build


SEARCH_TERMS = [
    "cooking",
    "data analytics",
    "finance",
    "fitness",
    "fortnite",
    "minecraft",
    "python programming",
    "travel",
]

VIDEOS_PER_SEARCH = 100


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


def create_youtube_client(api_key: str) -> Resource:
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
    max_videos: int = 100,
) -> list[dict[str, Any]]:
    """
    Search YouTube for videos.
    """

    videos: list[dict[str, Any]] = []
    next_page_token = None

    while len(videos) < max_videos:

        remaining = max_videos - len(videos)

        request = youtube.search().list(
            q=query,
            part="snippet",
            type="video",
            maxResults=min(50, remaining),
            pageToken=next_page_token,
        )

        response = request.execute()

        for item in response["items"]:

            videos.append(
                {
                    "collection_date": datetime.now().isoformat(timespec="seconds"),
                    "search_term": query,
                    "video_id": item["id"]["videoId"],
                    "title": html.unescape(item["snippet"]["title"]),
                    "description": html.unescape(item["snippet"]["description"]),
                    "channel_title": item["snippet"]["channelTitle"],
                    "published_at": item["snippet"]["publishedAt"],
                }
            )

        print(f"Collected {len(videos)} videos for '{query}'...")

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return videos


def get_video_statistics(
    youtube,
    video_ids: list[str],
) -> dict[str, dict[str, Any]]:
    """
    Retrieve statistics and content details for videos.
    """

    statistics: dict[str, dict[str, Any]] = {}

    batch_size = 50
    total_batches = (len(video_ids) + batch_size - 1) // batch_size

    for batch_number, start in enumerate(
        range(0, len(video_ids), batch_size),
        start=1,
    ):

        batch_ids = video_ids[start:start + batch_size]

        print(f"Retrieving statistics (Batch {batch_number} of {total_batches})...")

        request = youtube.videos().list(
            part="statistics,contentDetails",
            id=",".join(batch_ids),
        )

        response = request.execute()

        for item in response["items"]:
            statistics[item["id"]] = item

    return statistics


def enrich_videos(
    videos: list[dict[str, Any]],
    statistics: dict[str, dict[str, Any]],
) -> None:
    """
    Merge video statistics into each video.
    """

    for video in videos:

        stats = statistics.get(video["video_id"])

        if not stats:
            continue

        video["view_count"] = int(stats["statistics"].get("viewCount", 0))
        video["like_count"] = int(stats["statistics"].get("likeCount", 0))
        video["comment_count"] = int(stats["statistics"].get("commentCount", 0))
        video["favorite_count"] = int(stats["statistics"].get("favoriteCount", 0))
        video["duration"] = stats["contentDetails"]["duration"]
        video["definition"] = stats["contentDetails"]["definition"]
        video["caption"] = stats["contentDetails"]["caption"]


def remove_duplicate_videos(
    videos: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Remove duplicate videos based on video_id.
    """

    unique_videos: list[dict[str, Any]] = []
    seen_video_ids: set[str] = set()

    for video in videos:

        video_id = video["video_id"]

        if video_id in seen_video_ids:
            continue

        seen_video_ids.add(video_id)
        unique_videos.append(video)

    duplicates_removed = len(videos) - len(unique_videos)

    print(f"\nRemoved {duplicates_removed} duplicate videos.")
    print(f"Unique videos remaining: {len(unique_videos)}")

    return unique_videos


def save_to_csv(
    videos: list[dict[str, Any]],
    output_file: Path,
) -> pd.DataFrame:
    """
    Save collected videos to a CSV file.
    """

    df = pd.DataFrame(videos)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    return df


def main():
    """
    Run the YouTube data collection pipeline.
    """

    start_time = datetime.now()

    print("Loading API key...")

    api_key = load_api_key()
    print("API key loaded successfully.")

    youtube = create_youtube_client(api_key)
    print("Connected to the YouTube Data API.")

    all_videos: list[dict[str, Any]] = []

    for search_term in SEARCH_TERMS:

        print(f"\nSearching for: {search_term}")

        videos = search_videos(
            youtube=youtube,
            query=search_term,
            max_videos=VIDEOS_PER_SEARCH,
        )

        all_videos.extend(videos)

    video_ids = [video["video_id"] for video in all_videos]

    statistics = get_video_statistics(youtube, video_ids)

    enrich_videos(all_videos, statistics)

    all_videos = remove_duplicate_videos(all_videos)

    project_root = Path(__file__).resolve().parents[1]

    output_file = (
        project_root
        / "data"
        / "raw"
        / "youtube_video_metadata.csv"
    )

    df = save_to_csv(all_videos, output_file)

    elapsed = datetime.now() - start_time

    print("\nCollection Summary")
    print("-" * 30)
    print(f"Search terms: {len(SEARCH_TERMS)}")
    print(f"Unique videos collected: {len(df)}")
    print(f"Output file: {output_file}")
    print(f"Collection completed in: {elapsed}")

    print("\nDataset Preview")
    print("-" * 30)
    print(df.head())


if __name__ == "__main__":
    main()