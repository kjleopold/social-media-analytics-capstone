"""
social_media_eda.py

Perform exploratory data analysis on the cleaned
YouTube dataset.

Author: Kellie J. Leopold
Project: Social Media Analytics Capstone
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def load_dataset(input_file: Path) -> pd.DataFrame:
    """
    Load the cleaned YouTube dataset.

    Args:
        input_file: Path to the cleaned CSV.

    Returns:
        Pandas DataFrame.
    """

    return pd.read_csv(
        input_file,
        parse_dates=["collection_date", "published_at"],
    )


def inspect_dataset(df: pd.DataFrame) -> None:
    """
    Display basic information about the dataset.
    """

    print("\nDataset Information")
    print("-" * 30)

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isna().sum())


def display_summary_statistics(df: pd.DataFrame) -> None:
    """
    Display summary statistics.
    """

    print("\nSummary Statistics")
    print("-" * 30)
    print(df.describe())

    print("\nEngagement Metrics")
    print("-" * 30)
    print(df[["view_count", "like_count", "comment_count"]].describe())


def display_category_counts(df: pd.DataFrame) -> None:
    """
    Display the number of videos in each category.
    """

    print("\nVideos per Category")
    print("-" * 30)
    print(df["search_term"].value_counts())


def create_figures_directory(project_root: Path) -> Path:
    """
    Create the figures directory.
    """

    figures_dir = project_root / "reports" / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    return figures_dir


def plot_view_distribution(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot the distribution of view counts.
    """

    plt.figure(figsize=(8, 5))
    sns.histplot(df["view_count"], bins=30)

    plt.title("Distribution of View Counts")
    plt.xlabel("View Count")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig(figures_dir / "view_count_distribution.png", dpi=300)
    plt.show()


def plot_log_view_distribution(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot the log-transformed distribution of view counts.
    """

    plt.figure(figsize=(8, 5))
    sns.histplot(np.log10(df["view_count"] + 1), bins=30)

    plt.title("Distribution of Log-Transformed View Counts")
    plt.xlabel("Log10(View Count)")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig(figures_dir / "log_view_count_distribution.png", dpi=300)
    plt.show()


def plot_view_category_boxplot(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot view counts by content category.
    """

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="search_term",
        y="view_count",
        showfliers=False,
    )

    plt.yscale("log")
    plt.title("View Count by Content Category")
    plt.xlabel("Content Category")
    plt.ylabel("View Count (Log Scale)")
    plt.xticks(rotation=30)

    plt.tight_layout()
    plt.savefig(figures_dir / "view_count_by_category.png", dpi=300)
    plt.show()


def plot_like_category_boxplot(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot like counts by content category.
    """

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="search_term",
        y="like_count",
        showfliers=False,
    )

    plt.yscale("log")
    plt.title("Like Count by Content Category")
    plt.xlabel("Content Category")
    plt.ylabel("Like Count (Log Scale)")
    plt.xticks(rotation=30)

    plt.tight_layout()
    plt.savefig(figures_dir / "like_count_by_category.png", dpi=300)
    plt.show()


def plot_comment_category_boxplot(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot comment counts by content category.
    """

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="search_term",
        y="comment_count",
        showfliers=False,
    )

    plt.yscale("log")
    plt.title("Comment Count by Content Category")
    plt.xlabel("Content Category")
    plt.ylabel("Comment Count (Log Scale)")
    plt.xticks(rotation=30)

    plt.tight_layout()
    plt.savefig(figures_dir / "comment_count_by_category.png", dpi=300)
    plt.show()


def plot_correlation_heatmap(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot the correlation matrix.
    """

    correlation = df[
        [
            "view_count",
            "like_count",
            "comment_count",
            "favorite_count",
        ]
    ].corr()

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="Blues",
        fmt=".2f",
    )

    plt.title("Correlation Matrix")
    plt.tight_layout()

    plt.savefig(figures_dir / "correlation_matrix.png", dpi=300)
    plt.show()


def main():
    """
    Run the exploratory data analysis pipeline.
    """

    project_root = Path(__file__).resolve().parents[1]

    input_file = (
        project_root
        / "data"
        / "processed"
        / "youtube_video_metadata_clean.csv"
    )

    print("Loading cleaned dataset...")

    df = load_dataset(input_file)

    inspect_dataset(df)
    display_summary_statistics(df)
    display_category_counts(df)

    figures_dir = create_figures_directory(project_root)

    plot_view_distribution(df, figures_dir)
    plot_log_view_distribution(df, figures_dir)
    plot_view_category_boxplot(df, figures_dir)
    plot_like_category_boxplot(df, figures_dir)
    plot_comment_category_boxplot(df, figures_dir)
    plot_correlation_heatmap(df, figures_dir)

    print("\nEDA complete.")
    print("\nFigures saved to:")
    print(figures_dir)


if __name__ == "__main__":
    main()