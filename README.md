# Social Media Analytics: Data Pipeline & Predictive Modeling

**Python · YouTube Data API v3 · ETL · Exploratory Data Analysis · Feature Engineering · Machine Learning**

## Project Overview

This project examines relationships between YouTube video characteristics and audience engagement through a Python data pipeline. Using metadata collected through the YouTube Data API v3, the workflow organizes source data, prepares a cleaned analytical dataset, explores engagement patterns, and compares regression models for predicting video view counts.

The final analytical dataset documented for this project contains **769 video records and 14 attributes** collected across eight predefined YouTube search topics. The modeling workflow compares Linear Regression as a baseline with a Random Forest Regressor.

### Key Findings

- The analytical dataset contains 769 video records across eight predefined search topics.
- The Random Forest Regressor outperformed the Linear Regression baseline across the three reported evaluation metrics.
- Publication-related features, particularly publication year, ranked prominently in the Random Forest feature-importance analysis.
- The analysis identifies predictive relationships within the collected sample. It does not establish that any video characteristic causes higher engagement.

### Key Capabilities

- **API data collection:** Retrieves YouTube video metadata through the YouTube Data API v3.
- **Data preparation:** Cleans and organizes collected records for analysis.
- **Exploratory data analysis:** Uses descriptive statistics and visualizations to investigate engagement patterns.
- **Feature engineering:** Derives publication-related features, converts video duration to minutes, and transforms view counts for modeling.
- **Predictive modeling:** Compares Linear Regression and Random Forest regression using R², mean absolute error (MAE), and root mean squared error (RMSE).
- **Reproducible environment:** Uses `pyproject.toml`, `uv.lock`, and `.python-version` to document and manage the Python environment.
- **Credential management:** Reads the YouTube API key from a local `.env` file excluded from version control.

---

## Architecture & Workflow

The project is organized into five workflow phases. Validation activities are incorporated into the existing preparation and exploratory-analysis workflow; there is no separate validation script in the repository.

```text
┌────────────────────────────────────────┐
│           1. DATA COLLECTION            │
│        YouTube Data API v3              │
│        Retrieve video metadata          │
└────────────────────┬───────────────────┘
                     ▼
┌────────────────────────────────────────┐
│       2. DATA PREPARATION & CLEANING    │
│     Deduplication · Date conversion    │
│       Missing-description handling      │
└────────────────────┬───────────────────┘
                     ▼
┌────────────────────────────────────────┐
│      3. EXPLORATORY DATA ANALYSIS       │
│      Descriptive statistics             │
│      Engagement patterns and charts     │
└────────────────────┬───────────────────┘
                     ▼
┌────────────────────────────────────────┐
│           4. DATA QUALITY REVIEW        │
│     Required fields · Missing values    │
│      Summary statistics · Visuals       │
└────────────────────┬───────────────────┘
                     ▼
┌────────────────────────────────────────┐
│        5. MACHINE LEARNING MODELING     │
│    Feature engineering · Preprocessing  │
│       Regression · Model evaluation     │
└────────────────────────────────────────┘
```

### Phase 1: Data Collection

The collection script retrieves YouTube video metadata for eight predefined search topics and saves the results for downstream analysis.

The collected metadata includes fields such as video identifiers, titles, descriptions, channel names, publication information, engagement counts, duration, caption availability, video definition, and search topic.

**Script:** `scripts/collect_youtube_metadata.py`

### Phase 2: Data Preparation & Cleaning

The cleaning script prepares collected records for analysis. Documented operations include:

- Identifying and removing duplicate video records.
- Converting publication timestamps to datetime values.
- Standardizing missing descriptions.
- Checking required metadata fields.
- Exporting the cleaned dataset for downstream analysis.

The project report documents 135 records with missing descriptions. These descriptions were standardized to empty strings, allowing those records to be retained rather than removed solely because a description was missing. The final analytical dataset contained 769 records and 14 attributes.

**Script:** `scripts/clean_youtube_data.py`

### Phase 3: Exploratory Data Analysis

The exploratory analysis uses pandas, NumPy, and Matplotlib to examine dataset characteristics and engagement patterns.

Analysis documented for the project includes descriptive statistics, frequency counts, engagement distributions across search topics, comparisons of view counts across video-duration groups, relationships between engagement metrics, and visualizations. Because view counts are highly skewed, logarithmic transformations are used in selected visualizations.

**Script:** `scripts/social_media_eda.py`

### Phase 4: Data Quality Review

Data-quality review includes checking duplicate records, required fields, missing values, the presence of required variables, summary statistics, and visualizations for potential unexpected values or errors.

These activities are described in the project workflow and report; they are not implemented as a separate validation script.

### Phase 5: Machine Learning Modeling

The modeling workflow compares two supervised regression approaches for predicting view counts:

- **Linear Regression:** Baseline model for evaluating predictive relationships between selected video characteristics and the target.
- **Random Forest Regressor:** Ensemble model evaluated on the same prediction task.

The documented modeling workflow includes:

- Converting video duration into minutes.
- Extracting publication year and month.
- Applying a logarithmic transformation to view counts.
- Encoding categorical features with scikit-learn preprocessing tools.
- Splitting the data into training and test sets using an 80/20 split.
- Using a fixed random state for reproducible splitting.
- Evaluating both models on the test set using R², MAE, and RMSE.
- Examining Random Forest feature importance.

A scikit-learn `ColumnTransformer` and `OneHotEncoder` prepare categorical variables for modeling.

**Script:** `scripts/social_media_model.py`

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming language | Python |
| API integration | YouTube Data API v3 |
| Data manipulation | pandas, NumPy |
| Data visualization | Matplotlib |
| Machine learning | scikit-learn |
| Data preprocessing | `ColumnTransformer`, `OneHotEncoder` |
| Data storage | CSV |
| Dependency management | `uv`, `pyproject.toml`, `uv.lock` |
| Configuration and credentials | `python-dotenv`, `.env` |
| Version control | Git, GitHub |
| Development environment | Visual Studio Code, terminal |

---

## Repository Structure

The tree below summarizes the main project folders and files. It intentionally excludes local configuration, virtual-environment files, and the report documents managed separately in Overleaf. File names and generated outputs should reflect what is actually committed to the repository.

```text
social-media-analytics-capstone/
│
├── data/
│   ├── raw/
│   │   ├── youtube_search_metadata.csv
│   │   └── youtube_video_metadata.csv
│   └── processed/
│       └── youtube_video_metadata_clean.csv
│
├── reports/
│   ├── figures/             # EDA and model visualizations
│   └── tables/              # Analytical summaries and model results
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
├── pyproject.toml
├── README.md
└── uv.lock
```

The `.env` file, `.venv/` directory, and `Report Docs/` directory are local and should not be committed. The repository's `.gitignore` excludes these items.

---

## Dataset Reference

### Search Topics

The collection workflow covers eight predefined YouTube search topics:

1. Cooking
2. Fitness
3. Travel
4. Finance
5. Python Programming
6. Data Analytics
7. Fortnite
8. Minecraft

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

The table lists principal fields. The final project report documents 14 attributes in the analytical dataset; refer to the processed CSV for the complete schema.

### Data Quality & Limitations

The cleaning workflow addresses duplicate records, missing descriptions, required-field completeness, and selected data-type consistency.

The data comes from videos retrieved using eight predefined search topics. It is not a random or representative sample of all YouTube content. Results may be affected by topic selection, API behavior, the characteristics of returned videos, and metadata availability. The analysis examines patterns and predictive relationships; it does not establish causation.

---

## Model Performance & Evaluation

The project compares Linear Regression and Random Forest regression using R², mean absolute error (MAE), and root mean squared error (RMSE).

| Metric | Linear Regression | Random Forest Regressor |
|---|---:|---:|
| R² | 0.4092 | **0.5842** |
| MAE | 0.6087 | **0.5143** |
| RMSE | 0.7702 | **0.6461** |

### Interpretation

The Random Forest model outperformed the Linear Regression baseline across all three reported metrics on the project's evaluation dataset.

- **R²:** Random Forest achieved 0.5842, compared with 0.4092 for Linear Regression.
- **MAE:** Random Forest produced a lower mean absolute prediction error.
- **RMSE:** Random Forest produced a lower root mean squared error.

The project also examined Random Forest feature importance. Publication-related features, particularly publication year, ranked prominently. Feature importance describes how the fitted model uses features for prediction; it does not demonstrate causation.

**Metric note:** View counts were logarithmically transformed for modeling. The reported MAE and RMSE are on the transformed target scale, not directly in raw view-count units.

---

## Project Setup & Environment

These instructions describe how to set up the project in a local development environment. The commands assume that the script paths and input/output locations match the repository version being run.

### Prerequisites

- The Python version specified in `.python-version`.
- `uv` installed and available in the terminal.
- A valid YouTube Data API v3 key for collecting fresh metadata.
- Git, if cloning the repository.

Project dependencies are declared in `pyproject.toml` and resolved through `uv.lock`. Individual packages do not need to be installed manually with pip.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd social-media-analytics-capstone
```

Replace `<repository-url>` with the actual repository URL. If the repository is already on your computer, open its root folder in Visual Studio Code instead.

### 2. Check Python and uv

```bash
python --version
uv --version
```

Use the Python version specified in `.python-version`. If that version is not installed, install it before synchronizing the environment.

### 3. Synchronize Project Dependencies

From the project root, run:

```bash
uv sync
```

This synchronizes the project environment using its dependency declarations and lockfile.

- `pyproject.toml` declares project metadata, dependencies, and related configuration.
- `uv.lock` records resolved dependency versions.
- `.python-version` identifies the intended Python version.

### 4. Configure the YouTube API Key

Create a file named `.env` in the repository root, alongside `pyproject.toml`:

```text
YOUTUBE_API_KEY=YOUR_API_KEY_HERE
```

Replace the placeholder with your actual API key. The variable name must match the one read by `scripts/collect_youtube_metadata.py`. Keep `.env` excluded from version control and never commit a real API key.

### 5. Run the Pipeline

Run the scripts from the repository root in this order when starting with newly collected data. Each script expects the input files and output locations configured in its implementation.

**Step 1: Collect video metadata**

```bash
uv run python scripts/collect_youtube_metadata.py
```

**Step 2: Clean and prepare the dataset**

```bash
uv run python scripts/clean_youtube_data.py
```

**Step 3: Perform exploratory data analysis**

```bash
uv run python scripts/social_media_eda.py
```

**Step 4: Train and evaluate the models**

```bash
uv run python scripts/social_media_model.py
```

### 6. Optional: Activate the Virtual Environment

You can run commands with `uv run` without manually activating the environment. For interactive work in VS Code, you can also activate it in a terminal.

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux or macOS**

```bash
source .venv/bin/activate
```

To exit an activated environment:

```bash
deactivate
```

If PowerShell blocks activation, you can continue using `uv run` or review your PowerShell execution-policy settings.

---

## Dependency Management Cheatsheet

| Command | Purpose |
|---|---|
| `uv sync` | Synchronize the project environment |
| `uv run python <script.py>` | Run a Python script in the managed environment |
| `uv add <package-name>` | Add a dependency to the project |
| `uv remove <package-name>` | Remove a dependency from the project |
| `uv tree` | Display the dependency tree |
| `uv sync --upgrade` | Upgrade dependencies within applicable constraints and synchronize the environment |
| `python --version` | Check the active Python version |
| `uv --version` | Check the installed `uv` version |

### Updating Dependencies

Add a package:

```bash
uv add package-name
```

Remove a package:

```bash
uv remove package-name
```

Update resolved dependencies within the applicable constraints:

```bash
uv sync --upgrade
```

Review changes to `pyproject.toml` and `uv.lock`, and commit updated files when the changes are intentional.

---

## Configuration & Security

- Keep API credentials in the local `.env` file.
- Confirm `.env` is listed in `.gitignore`.
- Do not publish API keys in source files, notebook outputs, screenshots, or commit history.
- Use your own valid API key when reproducing the collection workflow.
- Be mindful of YouTube Data API quotas and applicable usage terms.
- Preserve `pyproject.toml`, `.python-version`, and `uv.lock` when sharing or cloning the project.

The lockfile helps keep dependency resolution consistent, but results can still differ if the API returns different data, the environment changes, or the code is modified.

---

## Troubleshooting

| Issue | What to check |
|---|---|
| `uv` is not recognized | Confirm `uv` is installed and available on your terminal's PATH. |
| Python version mismatch | Check `.python-version` and `python --version`. |
| Dependencies are missing | Run `uv sync` from the repository root. |
| API key errors | Confirm `.env` exists, the key is valid, and the variable name matches the collection script. |
| API quota or request errors | Check API quota, permissions, request parameters, and the returned error message. |
| Input CSV cannot be found | Verify the preceding script completed and that the input/output paths match the script configuration. |
| Output directory is missing | Check whether the script creates the directory automatically or expects it to exist. |
| Different model results | Verify the dataset, preprocessing, random state, dependency versions, and model configuration. |

---

## Limitations & Potential Enhancements

The project focuses on predictive analysis using YouTube metadata collected through the API. It does not establish causal relationships between video characteristics and engagement, and the findings may not generalize beyond the selected topics and collected sample.

Potential future enhancements include:

- Automated unit tests for collection and transformation steps.
- More detailed logging and error handling.
- Automated execution and pipeline orchestration.
- Additional models and systematic hyperparameter tuning.
- Evaluation on new collection periods and independent datasets.
- Further analysis of feature importance and model generalization.

These are possible extensions, not capabilities claimed as already implemented.

---

## Conclusion

This project demonstrates a Python workflow for collecting external API data, preparing analytical datasets, exploring engagement patterns, engineering features, and comparing predictive regression models.

On the reported evaluation metrics, the Random Forest Regressor outperformed the Linear Regression baseline. Exploratory analysis and feature importance provided additional insight into how selected video characteristics relate to view counts within the collected sample.

The repository provides a practical reference for API-based data collection, data preparation, exploratory analysis, feature engineering, model evaluation, and Python environment management.

## References

1. Google Developers. *YouTube Data API v3.* https://developers.google.com/youtube/v3
2. Leopold, K. J. (2026). *Social Media Analytics Capstone.* GitHub repository: https://github.com/kjleopold/social-media-analytics-capstone
