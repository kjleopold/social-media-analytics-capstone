"""
social_media_eda.py

Perform exploratory data analysis on the cleaned
YouTube dataset.

Author: Kellie J. Leopold
Project: Social Media Analytics Capstone
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd
from isodate import parse_duration
import seaborn as sns


# ---------------------------------------------------------------------
# Global Plot Style
# ---------------------------------------------------------------------

sns.set_theme(
    style="whitegrid",
    palette="deep",
    context="talk",
)

# ---------------------------------------------------------------------
# Data Loading
# ---------------------------------------------------------------------

def load_dataset(input_file: Path) -> pd.DataFrame:
    """
    Load the cleaned YouTube dataset.

    Args:
        input_file: Path to cleaned CSV.

    Returns:
        Cleaned DataFrame.
    """

    return pd.read_csv(
        input_file,
        parse_dates=["collection_date", "published_at"],
    )


# ---------------------------------------------------------------------
# Data Preparation
# ---------------------------------------------------------------------

def prepare_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare variables used throughout the EDA.

    Creates:
        duration_minutes
        log_view_count
    """

    df = df.copy()

    df["duration_minutes"] = (
        df["duration"]
        .apply(lambda x: parse_duration(x).total_seconds() / 60)
    )

    df["log_view_count"] = np.log10(df["view_count"] + 1)

    if "favorite_count" in df.columns:
        df = df.drop(columns="favorite_count")

    df["log_like_count"] = np.log10(df["like_count"] + 1)
    df["log_comment_count"] = np.log10(df["comment_count"] + 1)

    return df


# ---------------------------------------------------------------------
# Output Directories
# ---------------------------------------------------------------------

def create_output_directories(project_root: Path) -> tuple[Path, Path]:
    """
    Create report output folders.

    Returns:
        figures_dir
        tables_dir
    """

    reports_dir = project_root / "reports"

    figures_dir = reports_dir / "figures"
    tables_dir = reports_dir / "tables"

    figures_dir.mkdir(parents=True, exist_ok=True)
    tables_dir.mkdir(parents=True, exist_ok=True)

    return figures_dir, tables_dir


# ---------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------

def thousands_formatter(
    x: float,
    pos: int,
) -> str:
    """
    Format large numbers for plot axes.
    """

    if x >= 1_000_000:
        return f"{x / 1_000_000:.1f}M"

    if x >= 1_000:
        return f"{x / 1_000:.0f}K"

    return f"{x:.0f}"


def save_plot(
    filename: str,
    figures_dir: Path,
) -> None:
    """
    Save the current figure.
    """

    plt.tight_layout()
    plt.savefig(
        figures_dir / filename,
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()

# ---------------------------------------------------------------------
# Dataset Overview
# ---------------------------------------------------------------------

def inspect_dataset(df: pd.DataFrame) -> None:
    """
    Display basic information about the dataset.
    """

    print("\n" + "=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    print("\nData Types")
    print("-" * 30)
    print(df.dtypes)

    print("\nMissing Values")
    print("-" * 30)
    print(df.isna().sum())


def display_summary_statistics(
    df: pd.DataFrame,
    tables_dir: Path,
) -> None:
    """
    Display and save summary statistics for engagement metrics.
    """

    summary = (
        df[
            [
                "view_count",
                "like_count",
                "comment_count",
                "duration_minutes",
            ]
        ]
        .describe()
        .round(2)
    )

    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)
    print(summary)

    summary.to_csv(
        tables_dir / "summary_statistics.csv"
    )


def display_category_counts(
    df: pd.DataFrame,
    tables_dir: Path,
) -> None:
    """
    Display and save the number of videos
    collected for each content category.
    """

    category_counts = (
        df["search_term"]
        .value_counts()
        .sort_index()
        .rename("video_count")
    )

    print("\n" + "=" * 60)
    print("VIDEOS PER CATEGORY")
    print("=" * 60)
    print(category_counts)

    category_counts.to_csv(
        tables_dir / "videos_per_category.csv"
    )


def save_engagement_summary(
    df: pd.DataFrame,
    tables_dir: Path,
) -> pd.DataFrame:
    """
    Calculate average engagement by content category.

    Returns:
        DataFrame containing average engagement metrics.
    """

    engagement_summary = (
        df.groupby("search_term")[
            [
                "view_count",
                "like_count",
                "comment_count",
            ]
        ]
        .mean()
        .round(0)
        .astype(int)
    )

    print("\n" + "=" * 60)
    print("AVERAGE ENGAGEMENT BY CATEGORY")
    print("=" * 60)
    print(engagement_summary)

    engagement_summary.to_csv(
        tables_dir / "average_engagement_by_category.csv"
    )

    return engagement_summary


# ---------------------------------------------------------------------
# Engagement Distribution
# ---------------------------------------------------------------------

def plot_view_distribution(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot the distribution of video view counts.
    """

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["view_count"],
        bins=30,
        edgecolor="white",
        alpha=0.85,
    )

    plt.title("Distribution of View Counts")
    plt.xlabel("View Count")
    plt.ylabel("Number of Videos")

    plt.gca().xaxis.set_major_formatter(
        FuncFormatter(thousands_formatter)
    )

    plt.xticks(rotation=20)

    save_plot(
        "view_count_distribution.png",
        figures_dir,
    )


def plot_log_view_distribution(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot the log-transformed distribution of view counts.
    """

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["log_view_count"],
        bins=30,
        edgecolor="white",
        alpha=0.85,
    )

    plt.title("Distribution of Views (Log Scale)")
    plt.xlabel("Views (Log Scale)")
    plt.ylabel("Number of Videos")

    save_plot(
        "log_view_distribution.png",
        figures_dir,
    )


# ---------------------------------------------------------------------
# Engagement by Content Category
# ---------------------------------------------------------------------

def plot_metric_by_category(
    engagement_summary: pd.DataFrame,
    metric: str,
    title: str,
    x_label: str,
    filename: str,
    figures_dir: Path,
) -> None:
    """
    Plot the average value of an engagement metric
    by content category.

    Args:
        engagement_summary: Summary DataFrame containing
            average engagement metrics.
        metric: Column to plot.
        title: Figure title.
        x_label: X-axis label.
        filename: Output image filename.
        figures_dir: Directory for saved figures.
    """

    plot_data = (
        engagement_summary
        .reset_index()
        .sort_values(metric, ascending=False)
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=plot_data,
        x=metric,
        y="search_term",
        order=plot_data["search_term"],
        alpha=0.85,
    )

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel("Content Category")

    plt.gca().xaxis.set_major_formatter(
        FuncFormatter(thousands_formatter)
    )

    save_plot(
        filename,
        figures_dir,
    )


def plot_average_views_by_category(
    engagement_summary: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot average views by content category.
    """

    plot_metric_by_category(
        engagement_summary=engagement_summary,
        metric="view_count",
        title="Average Views by Content Category",
        x_label="Average Views",
        filename="average_views_by_category.png",
        figures_dir=figures_dir,
    )


def plot_average_likes_by_category(
    engagement_summary: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot average likes by content category.
    """

    plot_metric_by_category(
        engagement_summary=engagement_summary,
        metric="like_count",
        title="Average Likes by Content Category",
        x_label="Average Likes",
        filename="average_likes_by_category.png",
        figures_dir=figures_dir,
    )


def plot_average_comments_by_category(
    engagement_summary: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot average comments by content category.
    """

    plot_metric_by_category(
        engagement_summary=engagement_summary,
        metric="comment_count",
        title="Average Comments by Content Category",
        x_label="Average Comments",
        filename="average_comments_by_category.png",
        figures_dir=figures_dir,
    )


# ---------------------------------------------------------------------
# Relationship Analysis
# ---------------------------------------------------------------------

def plot_relationship(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    xlabel: str,
    ylabel: str,
    filename: str,
    figures_dir: Path,
) -> None:
    """
    Plot the relationship between two variables.
    """

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x=x,
        y=y,
        alpha=0.60,
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    save_plot(
        filename,
        figures_dir,
    )


def plot_views_vs_likes(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot the relationship between views and likes.
    """

    plot_relationship(
        df=df,
        x="log_view_count",
        y="log_like_count",
        title="Views vs. Likes",
        xlabel="Views (Log Scale)",
        ylabel="Likes (Log Scale)",
        filename="views_vs_likes.png",
        figures_dir=figures_dir,
    )


def plot_views_vs_comments(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot the relationship between views and comments.
    """

    plot_relationship(
        df=df,
        x="log_view_count",
        y="log_comment_count",
        title="Views vs. Comments",
        xlabel="Views (Log Scale)",
        ylabel="Comments (Log Scale)",
        filename="views_vs_comments.png",
        figures_dir=figures_dir,
    )


def plot_duration_vs_views(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot the relationship between video duration and view count.
    """

    plot_relationship(
        df=df,
        x="duration_minutes",
        y="log_view_count",
        title="Video Duration vs. Views",
        xlabel="Video Duration (Minutes)",
        ylabel="Views (Log Scale)",
        filename="duration_vs_views.png",
        figures_dir=figures_dir,
    )


# ---------------------------------------------------------------------
# Feature Analysis
# ---------------------------------------------------------------------

def plot_feature_comparison(
    df: pd.DataFrame,
    feature: str,
    metric: str,
    title: str,
    ylabel: str,
    filename: str,
    figures_dir: Path,
) -> None:
    """
    Compare an engagement metric across
    categories of a feature.
    """

    plot_data = (
        df.groupby(feature)[metric]
        .mean()
        .reset_index()
    )

    plt.figure(figsize=(8, 6))

    sns.barplot(
        data=plot_data,
        x=feature,
        y=metric,
        alpha=0.85,
    )

    plt.title(title)
    plt.xlabel(feature.replace("_", " ").title())
    plt.ylabel(ylabel)

    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(thousands_formatter)
    )

    save_plot(
        filename,
        figures_dir,
    )

def plot_caption_engagement(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Compare average views for videos
    with and without captions.
    """

    plot_feature_comparison(
        df=df,
        feature="caption",
        metric="view_count",
        title="Average Views by Caption Availability",
        ylabel="Average Views",
        filename="views_by_caption.png",
        figures_dir=figures_dir,
    )

def plot_definition_engagement(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Compare average views for HD
    and SD videos.
    """

    plot_feature_comparison(
        df=df,
        feature="definition",
        metric="view_count",
        title="Average Views by Video Definition",
        ylabel="Average Views",
        filename="views_by_definition.png",
        figures_dir=figures_dir,
    )

def plot_correlation_heatmap(
    df: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot correlations among engagement metrics.
    """

    correlation = (
        df[
            [
                "view_count",
                "like_count",
                "comment_count",
                "duration_minutes",
            ]
        ]
        .corr()
    )

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="Blues",
        fmt=".2f",
        square=True,
        linewidths=0.5,
        cbar_kws={"label": "Correlation"},
    )

    plt.title("Correlation Heatmap")

    save_plot(
        "correlation_heatmap.png",
        figures_dir,
    )

def print_key_findings(
    df: pd.DataFrame,
) -> None:
    """
    Display key findings from the exploratory analysis.
    """

    print("\n" + "=" * 60)
    print("KEY FINDINGS")
    print("=" * 60)

    print(f"Videos analyzed: {len(df):,}")

    print(
        f"Average views: "
        f"{df['view_count'].mean():,.0f}"
    )

    print(
        f"Average likes: "
        f"{df['like_count'].mean():,.0f}"
    )

    print(
        f"Average comments: "
        f"{df['comment_count'].mean():,.0f}"
    )

    strongest = (
        df[
            [
                "view_count",
                "like_count",
                "comment_count",
                "duration_minutes",
            ]
        ]
        .corr()["view_count"]
        .drop("view_count")
        .abs()
        .idxmax()
    )

    print(
        f"Strongest relationship with views: "
        f"{strongest}"
    )

    top_category = (
        df.groupby("search_term")["view_count"]
        .mean()
        .idxmax()
    )

    print(
        f"Top-performing content category: "
        f"{top_category}"
    )


# ---------------------------------------------------------------------
# Main Program
# ---------------------------------------------------------------------

def main() -> None:
    """
    Execute the exploratory data analysis workflow.
    """

    project_root = Path(__file__).resolve().parents[1]

    input_file = (
        project_root
        / "data"
        / "processed"
        / "youtube_video_metadata_clean.csv"
    )

    figures_dir, tables_dir = create_output_directories(project_root)

    df = load_dataset(input_file)
    df = prepare_dataset(df)

    inspect_dataset(df)

    display_summary_statistics(df, tables_dir)
    display_category_counts(df, tables_dir)

    engagement_summary = save_engagement_summary(df, tables_dir)

    plot_view_distribution(df, figures_dir)
    plot_log_view_distribution(df, figures_dir)

    plot_average_views_by_category(engagement_summary, figures_dir)
    plot_average_likes_by_category(engagement_summary, figures_dir)
    plot_average_comments_by_category(engagement_summary, figures_dir)

    plot_views_vs_likes(df, figures_dir)
    plot_views_vs_comments(df, figures_dir)
    plot_duration_vs_views(df, figures_dir)

    plot_caption_engagement(df, figures_dir)
    plot_definition_engagement(df, figures_dir)

    plot_correlation_heatmap(df, figures_dir)

    print_key_findings(df)

    print("\nEDA complete!")
    print("Figures and tables saved to the reports directory.")


if __name__ == "__main__":
    main()