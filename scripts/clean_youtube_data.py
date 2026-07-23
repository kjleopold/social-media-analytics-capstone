"""
clean_youtube_data.py

Clean and prepare the YouTube dataset for analysis.

Author: Kellie J. Leopold
Project: Social Media Analytics Capstone
"""

from pathlib import Path

import pandas as pd


def load_dataset(input_file: Path) -> pd.DataFrame:
    """
    Load the raw YouTube dataset.

    Args:
        input_file: Path to the raw CSV.

    Returns:
        Pandas DataFrame.
    """

    return pd.read_csv(input_file)


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


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate video IDs.
    """

    before = len(df)

    df = df.drop_duplicates(subset="video_id")

    removed = before - len(df)

    print(f"\nDuplicate rows removed: {removed}")

    return df


def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert columns to appropriate data types.
    """

    df["collection_date"] = pd.to_datetime(df["collection_date"])
    df["published_at"] = pd.to_datetime(df["published_at"])

    return df


def validate_dataset(df: pd.DataFrame) -> None:
    """
    Validate the cleaned dataset.
    """

    print("\nValidation Summary")
    print("-" * 30)

    print(f"Duplicate video IDs: {df['video_id'].duplicated().sum()}")
    print(f"Missing descriptions: {df['description'].isna().sum()}")
    print(f"Missing titles: {df['title'].isna().sum()}")
    print(f"Missing channel names: {df['channel_title'].isna().sum()}")


def save_dataset(
    df: pd.DataFrame,
    output_file: Path,
) -> None:
    """
    Save cleaned dataset.
    """

    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)


def main():
    """
    Run the data cleaning pipeline.
    """

    project_root = Path(__file__).resolve().parents[1]

    input_file = (
        project_root
        / "data"
        / "raw"
        / "youtube_video_metadata.csv"
    )

    output_file = (
        project_root
        / "data"
        / "processed"
        / "youtube_video_metadata_clean.csv"
    )

    print("Loading dataset...")

    df = load_dataset(input_file)

    original_rows = len(df)
    descriptions_standardized = df["description"].isna().sum()

    inspect_dataset(df)

    df = remove_duplicates(df)
    duplicates_removed = original_rows - len(df)

    df = convert_data_types(df)
    df["description"] = df["description"].fillna("")

    validate_dataset(df)

    print("\nFinal Data Types")
    print("-" * 30)
    print(df.dtypes)

    save_dataset(df, output_file)

    print("\nCleaning Summary")
    print("-" * 30)

    print(f"Original records: {original_rows}")
    print(f"Duplicate records removed: {duplicates_removed}")
    print(f"Missing descriptions standardized: {descriptions_standardized}")
    print(f"Final records: {len(df)}")
    print(f"Final attributes: {len(df.columns)}")

    print("\nSaved cleaned dataset:")
    print(output_file)


if __name__ == "__main__":
    main()