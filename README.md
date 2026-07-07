# Social Media Analytics Capstone

Master's capstone project for the Master of Science in Data Analytics program at Northwest Missouri State University.

## Project Overview

This project investigates the factors associated with higher levels of social media engagement using data collected through the YouTube Data API. The project includes data collection, data preparation, exploratory data analysis, validation, visualization, and predictive analytics to identify patterns that may contribute to successful content performance.

## Research Question

**What factors are associated with higher levels of social media engagement?**

## Technologies

- Python
- YouTube Data API v3
- pandas
- NumPy
- Matplotlib
- scikit-learn
- Jupyter Notebook
- Git
- uv

## Project Workflow

- Data Collection
- Data Preparation and Cleaning
- Exploratory Data Analysis
- Data Validation
- Results and Analysis

## Repository Structure

```text
data/
├── raw/
└── processed/

figures/
notebooks/
output/
scripts/

README.md
pyproject.toml
uv.lock
```

## Project Setup

Clone the repository:

```bash
git clone https://github.com/kjleopold/social-media-analytics-capstone.git
cd social-media-analytics-capstone
```

Install project dependencies:

```bash
uv sync
```

Activate the virtual environment (Windows PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Run the data collection script:

```bash
python scripts/collect_youtube_data.py
```

## Git Workflow

After completing a meaningful milestone:

```bash
git add .
git commit -m "Describe what you completed"
git push
```