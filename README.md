# Analyzing the Drivers of Social Media Engagement

Master of Science in Data Analytics

Capstone Project

**Author:** Kellie J. Leopold

Northwest Missouri State University

Summer 2026

**Project Status:** Completed (Summer 2026)

---

## Project Overview

This capstone project examines the relationship between selected YouTube video characteristics and social media engagement using data collected directly from the YouTube Data API v3. The project follows the complete data analytics lifecycle, including data collection, data preparation and cleaning, exploratory data analysis, data validation, supervised machine learning modeling, and interpretation of results.

Two supervised machine learning models, Linear Regression and Random Forest Regression, were developed and compared to evaluate how effectively selected video characteristics could be used to predict YouTube video engagement.

---

## Research Question

**Which YouTube video characteristics are associated with higher levels of social media engagement, and how effectively can machine learning models predict engagement using those characteristics?**

---

## Objectives

- Collect publicly available YouTube video metadata using the YouTube Data API v3.
- Prepare, clean, and validate the collected dataset.
- Explore relationships between selected YouTube video characteristics and engagement.
- Develop and compare Linear Regression and Random Forest Regression models.
- Evaluate model performance using R², Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).
- Interpret the findings and discuss the limitations of the study.

---

# Technologies

- Python 3.14
- uv
- Git
- GitHub
- YouTube Data API v3
- pandas
- NumPy
- Matplotlib
- scikit-learn
- Jupyter Notebook

---

# Repository Structure

```text
social-media-analytics-capstone/
│
├── data/
│   ├── raw/
│   │   └── youtube_video_metadata.csv
│   └── processed/
│       └── youtube_video_metadata_clean.csv
│
├── reports/
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

> **Note:** The `.env` file containing the YouTube Data API key is excluded from GitHub using `.gitignore`.

---

# Project Workflow

1. Data Collection
2. Data Preparation and Cleaning
3. Exploratory Data Analysis
4. Data Validation
5. Machine Learning Modeling

---

# Data Collection Pipeline

```text
Load API Key (.env)
        │
        ▼
Create YouTube Client
        │
        ▼
Search Multiple Topics
        │
        ▼
Retrieve Video Metadata and Engagement Statistics
        │
        ▼
Convert Results to Python Dictionaries
        │
        ▼
Create pandas DataFrame
        │
        ▼
Export Raw Dataset
```

Raw dataset:

```text
data/raw/youtube_video_metadata.csv
```

The raw dataset is then cleaned, validated, and exported as:

```text
data/processed/youtube_video_metadata_clean.csv
```

---

# Dataset

The dataset was collected using the YouTube Data API v3 and includes videos from the following search topics:

- Cooking
- Fitness
- Travel
- Finance
- Python Programming
- Data Analytics
- Fortnite
- Minecraft

The final dataset includes variables such as:

| Column | Description |
|---------|-------------|
| video_id | Unique YouTube video ID |
| title | Video title |
| description | Video description |
| channel_title | Channel name |
| published_at | Upload date and time |
| search_topic | Search topic used to retrieve the video |
| view_count | Total view count |
| like_count | Total like count |
| comment_count | Total comment count |
| duration | Video duration |
| caption_available | Caption availability |
| definition | Video definition (HD or SD) |

---

# Machine Learning Pipeline

The cleaned dataset was prepared for supervised machine learning by:

- Engineering new features from the original data.
- Converting video duration into minutes.
- Extracting publication year and publication month.
- Log-transforming view counts to reduce skewness.
- One-hot encoding categorical variables.
- Splitting the data into 80% training and 20% testing datasets.
- Training Linear Regression and Random Forest Regression models.
- Evaluating model performance using:
  - R²
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)

---

# Results Summary

Two supervised machine learning models were evaluated using the same preprocessing pipeline and testing dataset.

The Random Forest Regression model outperformed the Linear Regression model across all evaluation metrics.

| Metric | Linear Regression | Random Forest |
|---------|------------------:|--------------:|
| R² | 0.4092 | 0.5842 |
| MAE | 0.6087 | 0.5143 |
| RMSE | 0.7702 | 0.6461 |

The analysis demonstrated that YouTube video engagement is associated with multiple measurable video characteristics. Differences in engagement were observed across search topics and video duration groups, and the Random Forest model provided more accurate predictions than the Linear Regression model. Overall, the project demonstrated the value of combining exploratory data analysis with supervised machine learning to better understand patterns in social media engagement.

---

# Project Setup

Synchronize dependencies:

```bash
uv sync
```

Activate the virtual environment.

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Deactivate:

```powershell
deactivate
```

---

# Environment Management

Install all dependencies:

```bash
uv sync
```

Add a package:

```bash
uv add <package-name>
```

Example:

```bash
uv add plotly
```

Update packages:

```bash
uv sync --upgrade
```

View installed packages:

```bash
uv pip list
```

---

# Running the Project

Run the project scripts in the following order:

```bash
python scripts/collect_youtube_metadata.py
python scripts/clean_youtube_data.py
python scripts/social_media_eda.py
python scripts/social_media_model.py
```

---

# YouTube Data API

The API key is stored securely in:

```text
.env
```

Example:

```text
YOUTUBE_API_KEY=YOUR_API_KEY
```

The `.env` file is excluded from version control using `.gitignore` and should never be committed.

---

# Git Workflow

Check status:

```bash
git status
```

Stage changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Describe what you completed"
```

Push to GitHub:

```bash
git push
```

View commit history:

```bash
git log --oneline
```

---

# Dependencies

Managed with **uv**.

- google-api-python-client
- python-dotenv
- pandas
- numpy
- matplotlib
- scikit-learn
- jupyter

---

# Capstone Progress

## Project Setup

- [x] Create project repository
- [x] Configure Git
- [x] Configure GitHub
- [x] Configure uv
- [x] Configure virtual environment
- [x] Configure .gitignore
- [x] Configure .env
- [x] Enable YouTube Data API
- [x] Generate API key

## Data Collection

- [x] Connect to the YouTube Data API
- [x] Build reusable data collection script
- [x] Collect video metadata
- [x] Collect engagement statistics
- [x] Export raw dataset

## Data Preparation

- [x] Clean data
- [x] Handle missing values
- [x] Remove duplicates
- [x] Engineer new features
- [x] Validate dataset

## Exploratory Data Analysis

- [x] Perform summary statistics
- [x] Create visualizations
- [x] Identify patterns and trends

## Machine Learning

- [x] Build Linear Regression model
- [x] Build Random Forest Regression model
- [x] Evaluate model performance
- [x] Interpret results

## Reporting

- [x] Complete capstone report
- [x] Create supporting visualizations
- [x] Finalize documentation
- [x] Submit capstone