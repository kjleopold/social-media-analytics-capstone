# Multi-Stage ETL Data Pipeline & Predictive Modeling Infrastructure
**Production-Grade Python Ingestion, Schema Mapping, and Automated Preprocessing Pipeline**

## 📋 Architectural Overview
This repository contains a modular, production-ready **ETL (Extract, Transform, Load) data pipeline** built entirely in Python. The system targets, throttles, and ingests semi-structured JSON payloads from external REST endpoints (YouTube Data API v3), applies rigorous programmatically enforced data validation rules, handles missing data edge cases, and pipes clean data into an automated feature-engineering and predictive machine learning execution framework.

```text
[ DATA EXTRACT LAYER ]
Third-Party REST API Endpoints
│
▼ (JSON Streams)
[ DATA TRANSFORM LAYER ]
Modular Preprocessing, Schema Enforcement, & Automated Sanitization
│
▼ (Valid Partitioned CSVs)
[ DATA LOAD & MODEL LAYER ]
Sklearn ColumnTransformer, One-Hot Encoding, & Ensemble Regressors
```

By decoupling the pipeline architecture into isolated scripts for orchestration, transformation, validation, and analytics, this infrastructure mimics modern enterprise data platform systems.

## 🛠️ Core Engineering & Platform Features
*   **Decoupled Multi-Stage Execution:** Separates processing layers into independent orchestration scripts, ensuring clear data lineage boundaries between raw staging and refined reporting datasets.
*   **Robust REST API Ingestion & Rate Throttling:** Programmatically manages API connection state, query pagination, and batch execution workflows to securely interface with rate-limited upstream providers.
*   **Automated Schema Stabilization & Data Quality Controls:** Implements structured exception handling and automated validation rules via `pandas` and `NumPy` to isolate structural anomalies and convert missing data profiles into standard type-safe targets without record drops.
*   **Modern DevOps & Local Hermeticism:** Utilizes the blisteringly fast, rust-backed `uv` environment coordinator for reproducible lockfile synchronization and complete dependency isolation.
*   **Secured Secrets Management:** Enforces structural zero-trust configuration via decouple-layer `.env` pattern mapping, permanently masking infrastructure credentials via strict `.gitignore` filters.
*   **Automated Pipeline Preprocessing:** Leverages Scikit-Learn `ColumnTransformer` arrays to build automated inline normalization matrices, transforming highly skewed metrics using logarithmic smoothing and parsing strings into analytical vectors using one-hot categorical matrix mapping.

---

## 📖 Operational Reference & Setup Guide

### 🏗️ Repository Schema & Data Lineage

```text
social-media-analytics-capstone/
│
├── data/
│   ├── raw/                <-- Immutable Staging Ingestion Layer (CSV)
│   └── processed/          <-- Programmatically Validated & Cleaned Core Target (CSV)
│
├── reports/
│   ├── figures/            <-- Rendered Linear & Non-Linear Structural Profiles
│   └── tables/             <-- Evaluated Pipeline Metric Matrices
│
├── scripts/                <-- Isolated Component Execution Layer
│   ├── collect_youtube_metadata.py  <-- Extraction & JSON-to-Tabular Driver
│   ├── clean_youtube_data.py        <-- Transformation, Anomaly Isolation & Null Fallbacks
│   ├── social_media_eda.py          <-- Exploratory Validation & Linear Traversal
│   └── social_media_model.py        <-- Preprocessing Pipeline & Ensemble Training Loop
│
├── src/
│   └── social_media_analytics/
│       └── __init__.py
│
├── .gitignore              <-- Credential Masking Boundary
├── .python-version
├── pyproject.toml          <-- Declarative Project Specifications
├── README.md
└── uv.lock                 <-- Cryptographically Locked Dependency Assertions
```
\*Note: The `.env` file containing the YouTube Data API key is excluded from GitHub using `.gitignore`.\*

### 📊 Ingested Dataset Reference
The dataset target spans the following eight core predefined search topics:
*   Cooking, Fitness, Travel, Finance, Python Programming, Data Analytics, Fortnite, Minecraft

#### Schema Definition Table:

| Variable | Description |
| :--- | :--- |
| **video_id** | Unique YouTube video ID |
| **title** | Video title |
| **description** | Video description |
| **channel_title** | Channel name |
| **published_at** | Publication date |
| **search_topic** | Search topic used to retrieve the video |
| **view_count** | Total views (Target variable) |
| **like_count** | Total likes |
| **comment_count** | Total comments |
| **duration** | Video duration |
| **caption_available** | Caption availability |
| **definition** | Video definition (HD or SD) |

---

## ⚙️ Project Infrastructure Setup

### 1. Environment Synchronization
Install all project dependencies declarations mapped in `pyproject.toml` and compile the `uv.lock` file cleanly using the `uv` environment packager:
```bash
uv sync
```

### 2. Activate Local Virtual Boundary
Activate your sandboxed runtime environment inside your VSCode terminal:

**Windows PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```
**Linux / macOS POSIX:**
```bash
source .venv/bin/activate
```
\*To leave the boundary later, simply type `deactivate`.\*

### 3. Configure Secrets & Credentials
Create a local `.env` file at your root directory level to securely house your access credentials:
```bash
YOUTUBE_API_KEY=YOUR_API_KEY_HERE
```

### 4. Sequential Pipeline Lifecycle Execution
Run the data system workflows in chronological order to cleanly move from extraction to pipeline metrics evaluation:
```bash
python scripts/collect_youtube_metadata.py
python scripts/clean_youtube_data.py
python scripts/social_media_eda.py
python scripts/social_media_model.py
```

---

## 🛠️ Declarative Environment Management Cheatsheet
Keep these native `uv project` commands handy for maintaining your package manifest and tracking workspace state:
*   **Add a package to pyproject.toml:** `uv add <package-name>`
*   **Remove a dependency:** `uv remove <package-name>`
*   **Update lockfile & modules:** `uv sync --upgrade`
*   **Verify environment sync status:** `uv tree`

## 📦 System Dependency Manifest
All underlying project packages are declared inside `pyproject.toml` and anchored using hash-verified references inside `uv.lock`:
*   `google-api-python-client` (Native API abstract connector)
*   `python-dotenv` (Runtime context variable parser)
*   `pandas` & `numpy` (Vectorized data manipulation arrays)
*   `matplotlib` (Pipeline data reporting visualization)
*   `scikit-learn` (`ColumnTransformer` pipeline mapping algorithms)

---

## 📈 Pipeline Model Performance Matrix

| Performance Metric Matrix | Baseline Linear Regression | Random Forest Ensemble Regressor |
| :--- | :---: | :---: |
| **Coefficient of Determination (\(R^2\))** | `0.4092` | **`0.5842`** |
| **Mean Absolute Error (MAE)** | `0.6087` | **`0.5143`** |
| **Root Mean Squared Error (RMSE)** | `0.7702` | **`0.6461`** |

\*The non-linear ensemble algorithm achieved an \(R^2 = 0.5842\), effectively capturing cross-feature interactions and structural variations within multi-topic transaction records that flat linear profiles failed to resolve.\*