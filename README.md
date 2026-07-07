# Social Media Analytics Capstone

Master's capstone project for the Master of Science in Data Analytics program at Northwest Missouri State University.

---

## Project Overview

This project investigates the factors associated with higher levels of social media engagement using data collected directly from the YouTube Data API v3. The project follows the complete data analytics lifecycle, including data collection, preparation, exploratory data analysis, validation, predictive modeling, and interpretation of results.

---

## Research Question

**What factors are associated with higher levels of social media engagement?**

---

## Objectives

- Collect publicly available YouTube video metadata using the YouTube Data API.
- Prepare and clean the collected dataset.
- Explore relationships between video characteristics and engagement.
- Identify variables associated with higher engagement.
- Develop data-driven recommendations.

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
5. Results and Analysis

---

# Current Data Collection Pipeline

```text
Load API Key (.env)
        │
        ▼
Create YouTube Client
        │
        ▼
Search Videos
        │
        ▼
Convert Results to Python Dictionaries
        │
        ▼
Create pandas DataFrame
        │
        ▼
Export CSV
```

Current output:

```text
data/raw/youtube_search_results.csv
```

---

# Current Dataset

The current data collection script retrieves the following information for each video:

| Column | Description |
|---------|-------------|
| video_id | Unique YouTube video ID |
| title | Video title |
| description | Video description |
| channel_title | Channel name |
| published_at | Upload date and time |

Future versions will collect:

- View count
- Like count
- Comment count
- Video duration
- Category ID
- Channel statistics

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

The script will:

- Load the API key
- Connect to the YouTube Data API
- Search for videos
- Convert results into structured Python dictionaries
- Create a pandas DataFrame
- Save the data as a CSV file
- Display a preview of the collected data

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
- [x] Search YouTube videos
- [x] Convert API response into Python dictionaries
- [x] Create pandas DataFrame
- [x] Export raw CSV

### Next Steps

- [ ] Collect video statistics
- [ ] Collect engagement metrics
- [ ] Collect channel statistics
- [ ] Collect larger dataset

## Data Preparation

- [ ] Clean data
- [ ] Handle missing values
- [ ] Remove duplicates
- [ ] Engineer new features

## Exploratory Data Analysis

- [ ] Summary statistics
- [ ] Correlation analysis
- [ ] Visualizations
- [ ] Identify trends

## Modeling

- [ ] Select analytical techniques
- [ ] Build predictive model
- [ ] Evaluate model

## Reporting

- [ ] Complete analysis
- [ ] Finish visualizations
- [ ] Complete LaTeX report
- [ ] Submit capstone

---

# Author

**Kellie J. Leopold**

Master of Science in Data Analytics

Northwest Missouri State University

Summer 2026