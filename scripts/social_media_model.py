"""
social_media_model.py

Build and evaluate machine learning models
to predict YouTube video engagement.

Author: Kellie J. Leopold
Project: Social Media Analytics Capstone
"""

from pathlib import Path

import numpy as np
from isodate import parse_duration
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import RegressorMixin
from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score,
)

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

# ---------------------------------------------------------------------
# Global Settings
# ---------------------------------------------------------------------

RANDOM_STATE = 42
TEST_SIZE = 0.20

# Target variable to predict
TARGET = "log_view_count"

NUMERIC_FEATURES = [
    "duration_minutes",
]

ENGINEERED_FEATURES = [
    "published_year",
    "published_month",
]

CATEGORICAL_FEATURES = [
    "search_term",
    "caption",
    "definition",
]

# ---------------------------------------------------------------------
# Data Loading
# ---------------------------------------------------------------------

def load_dataset(input_file: Path) -> pd.DataFrame:
    """
    Load the cleaned YouTube dataset.

    Args:
        input_file: Path to the cleaned CSV file.

    Returns:
        Cleaned DataFrame.
    """

    return pd.read_csv(
        input_file,
        parse_dates=[
            "collection_date",
            "published_at",
        ],
    )

# ---------------------------------------------------------------------
# Feature Engineering
# ---------------------------------------------------------------------

def prepare_features(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.Series]:
    """
    Prepare the features and target variable for modeling.

    Returns:
        X: Predictor variables.
        y: Target variable.
    """

    df = df.copy()

    # Convert video duration to minutes
    df["duration_minutes"] = (
        df["duration"]
        .apply(lambda x: parse_duration(x).total_seconds() / 60)
    )

    # Create log-transformed target variable
    df["log_view_count"] = np.log10(
        df["view_count"] + 1
    )

    # Create date-based features
    df["published_year"] = df["published_at"].dt.year
    df["published_month"] = df["published_at"].dt.month

    # Add engineered features
    numeric_features = (
        NUMERIC_FEATURES
        + ENGINEERED_FEATURES
    )

    X = df[
        numeric_features + CATEGORICAL_FEATURES
    ]

    y = df[TARGET]

    return X, y

# ---------------------------------------------------------------------
# Preprocessing Pipeline
# ---------------------------------------------------------------------

def build_preprocessor() -> ColumnTransformer:
    """
    Build the preprocessing pipeline for the machine
    learning models.

    Returns:
        Configured ColumnTransformer.
    """

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(
                    handle_unknown="ignore",
                ),
                CATEGORICAL_FEATURES,
            ),
        ],
        remainder="passthrough",
    )

    return preprocessor

# ---------------------------------------------------------------------
# Model Training
# ---------------------------------------------------------------------

def train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    model: RegressorMixin,
) -> Pipeline:
    """
    Build and train a machine learning pipeline.

    Args:
        X_train: Training features.
        y_train: Training target values.
        model: Machine learning model.

    Returns:
        Trained pipeline.
    """

    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                build_preprocessor(),
            ),
            (
                "model",
                model,
            ),
        ]
    )

    pipeline.fit(
        X_train,
        y_train,
    )

    return pipeline

# ---------------------------------------------------------------------
# Model Evaluation
# ---------------------------------------------------------------------

def evaluate_model(
    pipeline: Pipeline,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> dict[str, float]:
    """
    Evaluate a trained machine learning model.

    Args:
        pipeline: Trained machine learning pipeline.
        X_test: Testing features.
        y_test: Testing target values.

    Returns:
        Dictionary containing evaluation metrics.
    """

    predictions = pipeline.predict(X_test)

    results = {
        "R2": r2_score(
            y_test,
            predictions,
        ),
        "MAE": mean_absolute_error(
            y_test,
            predictions,
        ),
        "RMSE": root_mean_squared_error(
            y_test,
            predictions,
        ),
    }

    return results

# ---------------------------------------------------------------------
# Feature Importance
# ---------------------------------------------------------------------

def get_feature_importance(
    pipeline: Pipeline,
) -> pd.DataFrame:
    """
    Extract feature importance from the trained
    Random Forest model.

    Args:
        pipeline: Trained Random Forest pipeline.

    Returns:
        DataFrame containing feature names
        and importance scores.
    """
    model = pipeline.named_steps["model"]

    preprocessor = pipeline.named_steps["preprocessor"]

    feature_names = preprocessor.get_feature_names_out()

    importance = model.feature_importances_

    feature_df = pd.DataFrame(
        {
            "Feature": feature_names,
            "Importance": importance,
        }
    )

    feature_df = feature_df.sort_values(
        by="Importance",
        ascending=False,
    )

    return feature_df

def plot_feature_importance(
    feature_importance: pd.DataFrame,
    figures_dir: Path,
) -> None:
    """
    Plot Random Forest feature importance.

    Args:
        feature_importance: Feature importance table.
        reports_dir: Reports directory.
    """

    plot_data = (
        feature_importance
        .sort_values(
            "Importance",
            ascending=True,
        )
    )

    plt.figure(figsize=(10, 8))

    plt.barh(
        plot_data["Feature"],
        plot_data["Importance"],
    )

    plt.title(
        "Random Forest Feature Importance for YouTube Video Engagement"
    )

    plt.xlabel(
        "Importance Score"
    )

    plt.ylabel(
        "Feature"
    )

    plt.tight_layout()

    plt.savefig(
        figures_dir
        / "feature_importance.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()

# ---------------------------------------------------------------------
# Main Function
# ---------------------------------------------------------------------

def main() -> None:
    """
    Build and evaluate machine learning models.
    """

    project_root = Path(__file__).resolve().parent.parent

    input_file = (
        project_root
        / "data"
        / "processed"
        / "youtube_video_metadata_clean.csv"
    )

    df = load_dataset(input_file)

    tables_dir = (
        project_root
        / "reports"
        / "tables"
    )

    figures_dir = (
        project_root
        / "reports"
        / "figures"
    )

    tables_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    figures_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
    )

    # -------------------------------------------------------------
    # Linear Regression
    # -------------------------------------------------------------

    linear_pipeline = train_model(
        X_train,
        y_train,
        LinearRegression(),
    )

    linear_results = evaluate_model(
        linear_pipeline,
        X_test,
        y_test,
    )

    # -------------------------------------------------------------
    # Random Forest
    # -------------------------------------------------------------

    forest_pipeline = train_model(
        X_train,
        y_train,
        RandomForestRegressor(
            random_state=RANDOM_STATE,
        ),
    )

    forest_results = evaluate_model(
        forest_pipeline,
        X_test,
        y_test,
    )

    feature_importance = get_feature_importance(
        forest_pipeline,
    )

    feature_importance["Feature"] = (
        feature_importance["Feature"]
        .str.replace(
            "categorical__",
            "",
            regex=False,
        )
        .str.replace(
            "remainder__",
            "",
            regex=False,
        )
        .str.replace(
            "search_term_",
            "Search Topic: ",
            regex=False,
        )
        .str.replace(
            "caption_",
            "Caption: ",
            regex=False,
        )
        .str.replace(
            "definition_",
            "Definition: ",
            regex=False,
        )
        .str.replace(
            "published_year",
            "Published Year",
            regex=False,
        )
        .str.replace(
            "published_month",
            "Published Month",
            regex=False,
        )
        .str.replace(
            "duration_minutes",
            "Duration (Minutes)",
            regex=False,
        )
        .str.replace(
            "_",
            " ",
            regex=False,
        )
        .str.title()
        .str.replace(
            "Hd",
            "HD",
            regex=False,
        )
        .str.replace(
            "Sd",
            "SD",
            regex=False,
        )
        .str.replace(
            "True",
            "Yes",
            regex=False,
        )
        .str.replace(
            "False",
            "No",
            regex=False,
        )
    )

    feature_importance.to_csv(
        tables_dir / "feature_importance.csv",
        index=False,
    )

    plot_feature_importance(
        feature_importance,
        figures_dir,
    )

    print("\nFEATURE IMPORTANCE")
    print(feature_importance)

    # -------------------------------------------------------------
    # Results
    # -------------------------------------------------------------

    results = pd.DataFrame(
        {
            "Linear Regression": linear_results,
            "Random Forest": forest_results,
        }
    )

    results = results.round(4)

    results.to_csv(
        tables_dir / "model_performance.csv"
    )

    print("\n" + "=" * 60)
    print("MODEL PERFORMANCE")
    print("=" * 60)

    print(results)

# ---------------------------------------------------------------------
# Run Program
# ---------------------------------------------------------------------

if __name__ == "__main__":
    main()

