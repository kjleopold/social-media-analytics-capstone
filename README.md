# Social Media Analytics: Data Pipeline & Predictive Modeling

**Python · ETL · REST API Integration · Data Quality · Feature
Engineering · Machine Learning**

## Project Overview

This project examines the relationship between YouTube video
characteristics and audience engagement through a modular Python data
pipeline. Using publicly available data from the YouTube Data API v3,
the workflow collects video metadata, prepares and validates analytical
datasets, explores engagement patterns, and evaluates supervised machine
learning models.

The pipeline separates data collection, preparation, exploratory
analysis, validation, and modeling into distinct stages. The final
analytical dataset contains **769 video records and 14 attributes**
spanning eight predefined search topics. Linear Regression and Random
Forest regression models were evaluated to assess how video
characteristics relate to view counts.

### Key Capabilities

-   **API data ingestion:** Retrieves video metadata through the YouTube
    Data API v3.
-   **ETL workflow:** Separates collection, cleaning, exploratory
    analysis, validation, and modeling.
-   **Data quality management:** Addresses duplicate records, required
    fields, missing descriptions, and dataset completeness.
-   **Exploratory data analysis:** Examines engagement patterns across
    content topics and video characteristics.
-   **Feature engineering:** Extracts publication-related features,
    transforms skewed view counts, and encodes categorical variables.
-   **Predictive modeling:** Compares Linear Regression and Random
    Forest regression using R², MAE, and RMSE.
-   **Environment management:** Uses `pyproject.toml`, `uv`, and
    `uv.lock`.
-   **Credential handling:** Loads API credentials from a local `.env`
    file excluded from version control.

------------------------------------------------------------------------

## Architecture & Workflow

The project follows five sequential phases.

``` text
┌──────────────────────────────────────┐
│          1. DATA COLLECTION          │
│  YouTube Data API v3                 │
│  Retrieve and structure video data   │
└──────────────────┬───────────────────┘
                   ▼
┌──────────────────────────────────────┐
│    2. DATA PREPARATION & CLEANING    │
│  Deduplication · Date conversion     │
│  Missing-value handling              │
└──────────────────┬───────────────────┘
                   ▼
┌──────────────────────────────────────┐
│      3. EXPLORATORY DATA ANALYSIS    │
│  Descriptive statistics              │
│  Engagement patterns · Visualizations│
└──────────────────┬───────────────────┘
                   ▼
┌──────────────────────────────────────┐
│          4. DATA VALIDATION          │
│  Required-field and completeness     │
│  checks · Dataset readiness review   │
└──────────────────┬───────────────────┘
                   ▼
┌──────────────────────────────────────┐
│      5. MACHINE LEARNING MODELING    │
│  Feature engineering · Preprocessing │
│  Regression · Model evaluation       │
└──────────────────────────────────────┘
```

### Phase 1: Data Collection

The collection script uses the YouTube Data API v3 to retrieve video
metadata for eight predefined search topics. API responses are processed
into structured records and saved for downstream analysis.

Collected attributes include video identifiers, titles, descriptions,
channel names, publication information, engagement counts, video
duration, caption availability, video definition, and search-topic
information.

**Script:** `scripts/collect_youtube_metadata.py`

### Phase 2: Data Preparation & Cleaning

The preparation script loads collected data into pandas and applies
cleaning operations to prepare the dataset for analysis.

Documented operations include:

-   Identifying and removing duplicate video records.
-   Converting publication timestamps into datetime values.
-   Standardizing missing descriptions.
-   Checking required metadata fields.
-   Exporting the cleaned dataset for subsequent analysis.

The final report documents 135 records with missing descriptions. Those
descriptions were standardized to empty strings, allowing the records to
be retained rather than removed solely because the description was
missing. The final dataset contained 769 records and 14 attributes.

**Script:** `scripts/clean_youtube_data.py`

### Phase 3: Exploratory Data Analysis

Exploratory analysis using pandas, NumPy, and Matplotlib examined
dataset characteristics and patterns in video engagement.

Analysis included descriptive statistics, frequency counts, engagement
distributions across search topics, comparisons of view counts across
video-duration groups, relationships between engagement metrics, and
visualizations. Because view counts were highly skewed, logarithmic
transformations were used in selected visualizations.

**Script:** `scripts/social_media_eda.py`

### Phase 4: Data Validation

The validation phase reviewed the cleaned dataset before model training.
Checks documented in the final report included reviewing duplicate
records, required fields and missing values, the presence of required
variables, summary statistics, and visualizations for unexpected values
or errors.

**Validation approach:** Documented as a project workflow phase and
performed through the data-preparation and exploratory-analysis
workflow. The repository structure does not identify a separate
validation script.

### Phase 5: Machine Learning Modeling

The modeling workflow prepares analytical features and compares two
supervised regression approaches.

-   **Linear Regression:** Baseline model for evaluating relationships
    between selected video characteristics and the engagement target.
-   **Random Forest Regressor:** Ensemble model used to evaluate
    predictive performance using the same task.

The workflow includes:

-   Converting video duration into minutes.
-   Extracting publication year and month.
-   Applying a logarithmic transformation to view counts.
-   Encoding categorical features using scikit-learn preprocessing
    tools.
-   Splitting the dataset into training and test sets using an 80/20
    split.
-   Using a fixed random state for reproducible splitting.
-   Evaluating both models on the test data.
-   Comparing R², MAE, and RMSE.
-   Examining Random Forest feature importance.

A scikit-learn `ColumnTransformer` and `OneHotEncoder` prepare
categorical variables for modeling.

**Script:** `scripts/social_media_model.py`

------------------------------------------------------------------------

## Technology Stack

  Category                  Technologies
  ------------------------- --------------------------------------
  Programming language      Python
  API integration           YouTube Data API v3
  Data manipulation         pandas, NumPy
  Visualization             Matplotlib
  Machine learning          scikit-learn
  Preprocessing             `ColumnTransformer`, `OneHotEncoder`
  Data exchange             CSV
  Dependency management     `uv`, `pyproject.toml`, `uv.lock`
  Configuration             `python-dotenv`, `.env`
  Version control           Git, GitHub
  Development environment   VS Code, terminal

------------------------------------------------------------------------

## Repository Structure

``` text
social-media-analytics-capstone/
│
├── data/
│   ├── raw/                # Collected source data
│   └── processed/          # Cleaned analytical data
│
├── reports/
│   ├── figures/            # Analysis and model visualizations
│   └── tables/             # Model evaluation results
│
├── scripts/
│   ├── collect_youtube_metadata.py
│   ├── clean_youtube_data.py
│   ├── social_media_eda.py
│   └── social_media_model.py
│
├── src/
│   └── social_media_analytics/
│       └── __init__.py
│
├── .gitignore
├── .python-version
├── pyproject.toml           # Project configuration and dependencies
├── README.md
└── uv.lock                  # Resolved dependency versions
```

Directory contents depend on which workflow stages have been executed
and which outputs are retained in the repository.

------------------------------------------------------------------------

## Dataset Reference

### Search Topics

The collection workflow covers eight predefined YouTube search topics:

1.  Cooking
2.  Fitness
3.  Travel
4.  Finance
5.  Python Programming
6.  Data Analytics
7.  Fortnite
8.  Minecraft

### Principal Data Fields

| Field | Description |
|---|---|
| `video_id` | Unique YouTube video identifier |
| `title` | Video title |
| `description` | Video description |
| `channel_title` | Name of the publishing channel |
| `published_at` | Publication timestamp |
| `search_topic` | Search topic associated with the record |
| `view_count` | Number of views; regression target |
| `like_count` | Number of likes |
| `comment_count` | Number of comments |
| `duration` | Video duration |
| `caption_available` | Caption availability indicator |
| `definition` | Video definition, such as HD or SD |

**Dataset note:** The final report documents 14 attributes. The table
above lists principal fields described in the project documentation;
consult the final processed CSV for the complete schema.

### Data Quality & Limitations

The cleaning and validation phases address duplicate records, missing
descriptions, required-field completeness, and consistency of selected
data types.

The analysis is based on videos retrieved from eight predefined search
topics, not a random or representative sample of all YouTube content.
Results may be affected by topic selection, API availability,
returned-video characteristics, and metadata availability. The analysis
investigates patterns and predictive relationships; it does not
establish causation.

------------------------------------------------------------------------

## Model Performance & Evaluation

The project compares Linear Regression and Random Forest regression
using R², mean absolute error (MAE), and root mean squared error (RMSE).

  Metric     Linear Regression   Random Forest Regressor
  -------- ------------------- -------------------------
  R²                    0.4092                **0.5842**
  MAE                   0.6087                **0.5143**
  RMSE                  0.7702                **0.6461**

### Interpretation

The Random Forest model outperformed the Linear Regression baseline
across all three reported metrics.

-   **R²:** Random Forest achieved 0.5842, compared with 0.4092 for
    Linear Regression.
-   **MAE:** Random Forest produced a lower mean absolute prediction
    error.
-   **RMSE:** Random Forest produced a lower root mean squared error.

These results indicate that Random Forest performed better on the
project's evaluation dataset using the selected features and
preprocessing approach.

The final report also examined Random Forest feature importance.
Publication-related features, particularly publication year, ranked
prominently. Feature importance reflects how a model uses information
for prediction; it does not prove causation.

**Metric interpretation:** View counts were logarithmically transformed
for modeling. The MAE and RMSE reported in the final project are
interpreted on the transformed target scale, not directly as errors in
raw view counts.

------------------------------------------------------------------------

## Project Setup & Environment Reference

This section documents how to set up and run the project again from a
local development environment.

### Prerequisites

-   Python version specified in `.python-version`.
-   `uv` installed and accessible from the terminal.
-   A valid YouTube Data API v3 key.
-   Git, if cloning the repository.

Project dependencies are declared in `pyproject.toml` and resolved
through `uv.lock`. **Packages do not need to be installed individually
with pip.**

### 1. Clone the Repository

``` bash
git clone <repository-url>
cd social-media-analytics-capstone
```

Replace `<repository-url>` with the actual repository URL. If the
repository is already on your computer, open its root folder in VS Code
instead.

### 2. Check Python and uv

``` bash
python --version
uv --version
```

Use the Python version specified in `.python-version`. If it is not
installed, install it before synchronizing the environment.

### 3. Synchronize Project Dependencies

From the project root, run:

``` bash
uv sync
```

This synchronizes the environment using the project's dependency
declarations and lockfile.

-   `pyproject.toml` declares project metadata, dependencies, and
    related configuration.
-   `uv.lock` records resolved dependency versions.
-   `.python-version` identifies the intended Python version.

### 4. Configure the YouTube API Key

Create a file named `.env` in the repository root, alongside
`pyproject.toml`.

``` text
YOUTUBE_API_KEY=YOUR_API_KEY_HERE
```

Replace the placeholder with your actual API key. Confirm that the
collection script reads this same environment-variable name. Keep `.env`
excluded from version control and never commit a real API key to GitHub.

### 5. Run the Pipeline in Order

Run each script from the repository root using `uv run`, which executes
the command within the project's managed environment.

**Step 1: Collect video metadata**

``` bash
uv run python scripts/collect_youtube_metadata.py
```

**Step 2: Clean and prepare the dataset**

``` bash
uv run python scripts/clean_youtube_data.py
```

**Step 3: Perform exploratory data analysis**

``` bash
uv run python scripts/social_media_eda.py
```

**Step 4: Train and evaluate the models**

``` bash
uv run python scripts/social_media_model.py
```

Run the scripts in sequence when starting with newly collected data.
Each script expects the input files and output locations configured in
its implementation.

### 6. Optional: Activate the Virtual Environment

You can use `uv run` without manually activating the environment. For
interactive work in VS Code, you can also activate it in the terminal.

**Windows PowerShell**

``` powershell
.venv\Scripts\Activate.ps1
```

**Linux or macOS**

``` bash
source .venv/bin/activate
```

To exit an activated environment:

``` bash
deactivate
```

If PowerShell blocks activation, you can continue using `uv run` or
review your PowerShell execution-policy settings.

------------------------------------------------------------------------

## Dependency Management Cheatsheet

  -----------------------------------------------------------------------
  Command                             Purpose
  ----------------------------------- -----------------------------------
  `uv sync`                           Synchronize the project environment

  `uv run python <script.py>`         Run a Python script in the managed
                                      environment

  `uv add <package-name>`             Add a dependency to the project

  `uv remove <package-name>`          Remove a dependency from the
                                      project

  `uv tree`                           Display the dependency tree

  `uv sync --upgrade`                 Upgrade dependencies within
                                      applicable constraints and
                                      synchronize the environment

  `python --version`                  Check the active Python version

  `uv --version`                      Check the installed `uv` version
  -----------------------------------------------------------------------

### Updating Dependencies

Add a package:

``` bash
uv add package-name
```

Remove a package:

``` bash
uv remove package-name
```

Update resolved dependencies within the applicable constraints:

``` bash
uv sync --upgrade
```

Review changes to `pyproject.toml` and `uv.lock`, and commit the updated
files when the changes are intentional.

------------------------------------------------------------------------

## Configuration & Security Notes

-   Keep API credentials in the local `.env` file.
-   Confirm `.env` is listed in `.gitignore`.
-   Do not publish API keys in source files, notebook outputs,
    screenshots, or commit history.
-   Use your own valid API key when reproducing the collection workflow.
-   Be mindful of YouTube Data API quotas and applicable usage terms.
-   Preserve `pyproject.toml`, `.python-version`, and `uv.lock` when
    sharing or cloning the project.

The lockfile helps keep dependency resolution consistent, but results
may still differ if the source API returns different data, the
environment changes, or the code is modified.

------------------------------------------------------------------------

## Troubleshooting Reference

  -----------------------------------------------------------------------
  Issue                               What to check
  ----------------------------------- -----------------------------------
  `uv` is not recognized              Confirm `uv` is installed and
                                      available on your terminal's PATH.

  Python version mismatch             Check `.python-version` and
                                      `python --version`.

  Dependencies are missing            Run `uv sync` from the repository
                                      root.

  API key errors                      Confirm `.env` exists, the key is
                                      valid, and the variable name
                                      matches the collection script.

  API quota or request errors         Check API quota, permissions,
                                      request parameters, and the
                                      returned error message.

  Input CSV cannot be found           Verify the preceding script
                                      completed and the input/output
                                      paths match the script
                                      configuration.

  Output directory is missing         Check whether the script creates
                                      the directory automatically or
                                      expects it to exist.

  Different model results             Verify the dataset, preprocessing,
                                      random state, dependency versions,
                                      and model configuration.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Limitations & Potential Enhancements

The project focuses on analytical modeling using publicly available
YouTube metadata. It does not establish causal relationships between
video characteristics and engagement, and findings may not generalize
beyond the selected topics and collected sample.

Potential future enhancements include:

-   Automated unit tests for data collection, transformation, and
    validation.
-   More detailed logging and error handling.
-   Automated execution and pipeline orchestration.
-   Additional models and systematic hyperparameter tuning.
-   Evaluation on new collection periods and independent datasets.
-   Further analysis of feature importance and model generalization.

These are potential extensions, not capabilities claimed as already
implemented.

------------------------------------------------------------------------

## Conclusion

This project demonstrates a modular Python workflow for collecting
external API data, preparing and validating analytical datasets,
exploring engagement patterns, and comparing predictive machine learning
models.

The final analysis found that Random Forest regression outperformed the
Linear Regression baseline on the reported evaluation metrics.
Exploratory analysis and feature importance provided additional insight
into the relationships between selected video characteristics and
engagement.

The repository provides a practical reference for API-based data
acquisition, data preparation, exploratory analysis, feature
engineering, model evaluation, and Python environment management.

## References

1.  Google Developers. *YouTube Data API v3.*
    https://developers.google.com/youtube/v3
2.  Leopold, K. J. (2026). *Social Media Analytics Capstone.* GitHub
    repository:
    https://github.com/kjleopold/social-media-analytics-capstone
