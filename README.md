# Social Media Analytics Capstone

Master's capstone project for the Master of Science in Data Analytics program at Northwest Missouri State University.

---

## Project Overview

This project examines the relationship between selected YouTube video characteristics and social media engagement using data collected directly from the YouTube Data API v3. The project follows the complete data analytics lifecycle, including data collection, preparation, exploratory data analysis, validation, supervised machine learning, and interpretation of results.

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
- Evaluate model performance using R², MAE, and RMSE.
- Interpret the results and discuss the study's limitations.

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
│   └── processed/
│
├── figures/
├── notebooks/
├── output/
├── scripts/
│   └── collect_youtube_data.py
│
├── src/
│   └── social_media_analytics/
│       └── __init__.py
│
├── Report Docs/
│
├── .env
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

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
Clean and Validate Dataset
        │
        ▼
Export CSV
```

Output:

```text
data/raw/youtube_search_results.csv
```

---

# Dataset

The dataset was collected using the YouTube Data API v3 and includes videos from eight search topics:

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
| search_topic | Search term used to retrieve the video |
| view_count | Total views |
| like_count | Total likes |
| comment_count | Total comments |
| duration | Video duration |
| caption_available | Caption availability |
| definition | Video definition (HD or SD) |

---

# Machine Learning Pipeline

The cleaned dataset was prepared for supervised machine learning by:

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

The Random Forest Regression model outperformed the Linear Regression model across all evaluation metrics.

| Metric | Linear Regression | Random Forest |
|--------|------------------:|--------------:|
| R² | 0.4092 | 0.5842 |
| MAE | 0.6087 | 0.5143 |
| RMSE | 0.7702 | 0.6461 |

The analysis demonstrated that YouTube video engagement is associated with multiple measurable video characteristics. Search topic and video duration were among the characteristics associated with differences in engagement, and the Random Forest model provided more accurate predictions than the Linear Regression model. Overall, the project demonstrated the value of combining exploratory data analysis with machine learning to better understand patterns in social media engagement.

---

# Project Setup

Synchronize dependencies:

```bash
uv sync
```

Activate the virtual environment:

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

Run the data collection script:

```bash
python scripts/collect_youtube_data.py
```

The complete project workflow includes:

1. Collect data from the YouTube Data API.
2. Prepare and clean the dataset.
3. Perform exploratory data analysis.
4. Train and evaluate machine learning models.
5. Generate visualizations and interpret the results.

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

The `.env` file is ignored by Git and should never be committed.

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

Commit:

```bash
git commit -m "Describe what you completed"
```

Push:

```bash
git push
```

View commit history:

```bash
git log --oneline
```

---

# Current Dependencies

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
- [x] Create professional README
- [x] Enable YouTube Data API
- [x] Generate API key

## Data Collection

- [x] Connect to YouTube API
- [x] Build reusable data collection script
- [x] Collect video metadata and engagement statistics
- [x] Create pandas DataFrame
- [x] Export raw CSV

## Data Preparation

- [x] Clean data
- [x] Handle missing values
- [x] Remove duplicates
- [x] Engineer new features
- [x] Validate dataset

## Exploratory Data Analysis

- [x] Summary statistics
- [x] Correlation analysis
- [x] Visualizations
- [x] Identify trends

## Modeling

- [x] Build Linear Regression model
- [x] Build Random Forest Regression model
- [x] Evaluate model performance

## Reporting

- [x] Complete analysis
- [x] Finish visualizations
- [x] Complete LaTeX report
- [x] Submit capstone

---

# Author

**Kellie J. Leopold**

Master of Science in Data Analytics

Northwest Missouri State University

Summer 2026