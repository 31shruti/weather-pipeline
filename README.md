
# Automated Weather Data Pipeline

An end-to-end data engineering project that collects, transforms, and stores hourly weather data for four major Indian cities: Jaipur, Delhi, Mumbai, and Bengaluru.

## Project Overview

This project demonstrates an automated ETL (Extract, Transform, Load) pipeline using Python and the Open-Meteo Weather API.

The pipeline:
- Extracts hourly weather data from an external API.
- Cleans and transforms raw JSON data using Pandas.
- Calculates temperature in Fahrenheit.
- Removes duplicate records.
- Stores processed data in an SQLite database.
- Supports PostgreSQL for cloud deployment.

## Architecture

```text
Open-Meteo Weather API
          |
          v
    Data Extraction
       (Python)
          |
          v
 Data Transformation
       (Pandas)
          |
          v
      Data Loading
      (SQLAlchemy)
          |
          v
   SQLite Database
          |
          v
   Future: Dashboard
```

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Pipeline development |
| Requests | API data extraction |
| Pandas | Data cleaning and transformation |
| SQLAlchemy | Database operations |
| SQLite | Local data storage |
| PostgreSQL | Cloud database support |
| Pytest | Automated testing |
| Git & GitHub | Version control |

## Cities Covered

- Jaipur
- Delhi
- Mumbai
- Bengaluru

## Project Structure

```text
weather-pipeline/
│
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── tests/
│   └── test_transform.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/31shruti/weather-pipeline.git
cd weather-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the pipeline

```bash
python -m src.pipeline
```

## Run Tests

```bash
python -m pytest
```

## Data Source

Weather data is collected using the free Open-Meteo API.

API Documentation: https://open-meteo.com/en/docs

## Current Features

- Multi-city weather extraction
- Hourly weather data processing
- Temperature conversion (Celsius to Fahrenheit)
- Duplicate record handling
- SQLite database storage
- PostgreSQL compatibility
- Automated transformation testing

## Future Improvements

- Automated daily pipeline execution using GitHub Actions
- Interactive Streamlit dashboard
- PostgreSQL cloud database integration
- Weather trend analysis and visualizations
- Data quality monitoring

## Author

**Shruti Soni**

B.Tech Computer Science Engineering

GitHub: https://github.com/31shruti
