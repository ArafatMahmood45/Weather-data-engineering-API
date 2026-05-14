# 🌦️ Weather Data Engineering API

## Overview
A lightweight data engineering project that processes historical weather station data and exposes it through a RESTful API using Flask and Pandas.

It demonstrates a simple data pipeline: **data ingestion → transformation → API serving**.

---
## 🌐 Live Demo

🔗 https://weather-data-engineering-api-1.onrender.com/

You can access the deployed API here.
---

## Tech Stack
- Python
- Flask
- Pandas

---

## Features
- Load and process weather station datasets
- Query temperature by station and date
- Retrieve full station records
- Filter data by year
- Simple HTML page for API documentation

---

## API Endpoints

**Get temperature by station and date**
- /api/v1/<station>/<date>/

**Get all data for a station**
- /api/v1/<station>/

**Get yearly data for a station**
- /api/v1/yearly/<station>/<year>/


---

## How to Run
```bash
pip install -r requirements.txt
python main.py
