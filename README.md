# Social Media Analytics Capstone

Master's capstone project for the Master of Science in Data Analytics program at Northwest Missouri State University.

---

## Project Overview

This project investigates the factors associated with higher levels of social media engagement using data collected through the YouTube Data API v3. The project follows the complete data analytics lifecycle, including data collection, preparation, exploratory data analysis, validation, visualization, predictive analytics, and interpretation of results.

---

## Research Question

**What factors are associated with higher levels of social media engagement?**

---

## Objectives

- Collect publicly available social media data using the YouTube Data API.
- Prepare and clean the collected dataset.
- Explore relationships between video characteristics and engagement metrics.
- Identify variables associated with higher engagement.
- Develop data-driven recommendations based on the findings.

---

## Technologies

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

## Project Workflow

1. Data Collection
2. Data Preparation and Cleaning
3. Exploratory Data Analysis
4. Data Validation
5. Results and Analysis

---

## Repository Structure

```text
social-media-analytics-capstone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── figures/
│
├── notebooks/
│
├── output/
│
├── scripts/
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

# Project Setup

Clone the repository:

```bash
git clone https://github.com/kjleopold/social-media-analytics-capstone.git
cd social-media-analytics-capstone
```

Synchronize the virtual environment and install all dependencies:

```bash
uv sync
```

Activate the virtual environment (Windows PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Deactivate the virtual environment:

```powershell
deactivate
```

---

# Environment Management

Install or update all project dependencies:

```bash
uv sync
```

Install a new package:

```bash
uv add <package-name>
```

Example:

```bash
uv add plotly
```

Update installed packages:

```bash
uv sync --upgrade
```

View installed packages:

```bash
uv pip list
```

---

# YouTube Data API

This project uses the official **YouTube Data API v3**.

The API key is stored securely in the `.env` file.

Example:

```text
YOUTUBE_API_KEY=YOUR_API_KEY_HERE
```

The `.env` file is ignored by Git and should never be committed.

---

# Git Workflow

Check repository status:

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

Push changes to GitHub:

```bash
git push
```

View commit history:

```bash
git log --oneline
```

---

## Suggested Commit Messages

```text
Initial project setup
Configure Python package structure
Add project documentation and README
Configure YouTube Data API
Implement YouTube API connection
Collect initial YouTube dataset
Implement data cleaning
Perform exploratory data analysis
Engineer engagement features
Train predictive model
Generate visualizations
Complete capstone report
```

---

# Current Python Dependencies

Dependencies are managed through **uv** and `pyproject.toml`.

Current packages:

- google-api-python-client
- python-dotenv
- pandas
- numpy
- matplotlib
- scikit-learn
- jupyter

---

# Project Notes

## Data Source

- YouTube Data API v3
- Publicly available YouTube metadata
- Data collected directly from Google's official API

## Expected Data Formats

- JSON (API responses)
- pandas DataFrames
- CSV (saved datasets)

## Planned Outputs

- Raw dataset
- Cleaned dataset
- Visualizations
- Feature engineered dataset
- Predictive models
- Final report

---

# Capstone Progress

## Project Setup

- [x] Create project folder
- [x] Organize project directories
- [x] Configure `uv`
- [x] Create virtual environment
- [x] Configure `.gitignore`
- [x] Configure `.env`
- [x] Initialize Git repository
- [x] Create GitHub repository
- [x] Push initial project to GitHub
- [x] Configure YouTube Data API
- [x] Create professional README

## Data Collection

- [ ] Connect to YouTube API
- [ ] Build data collection script
- [ ] Collect initial dataset
- [ ] Save raw CSV

## Data Preparation

- [ ] Clean dataset
- [ ] Handle missing values
- [ ] Remove duplicates
- [ ] Engineer additional features

## Exploratory Data Analysis

- [ ] Summary statistics
- [ ] Correlation analysis
- [ ] Visualizations
- [ ] Identify trends

## Modeling

- [ ] Select analytical techniques
- [ ] Build predictive model
- [ ] Evaluate results

## Reporting

- [ ] Complete analysis
- [ ] Finalize visualizations
- [ ] Finish LaTeX report
- [ ] Submit capstone

---

# Future Enhancements

Potential improvements beyond the capstone:

- Additional social media platforms
- Sentiment analysis
- NLP on video titles and descriptions
- Thumbnail image analysis
- Time-series analysis
- Interactive dashboards

---

# Author

**Kellie J. Leopold**

Master of Science in Data Analytics

Northwest Missouri State University

Summer 2026