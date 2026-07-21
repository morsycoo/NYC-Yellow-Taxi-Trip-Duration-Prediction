# 🚖 NYC Yellow Taxi Trip Duration Prediction

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# Project Overview

This project develops a complete end-to-end Machine Learning system for predicting the duration of NYC Yellow Taxi trips.

Unlike a traditional notebook-only project, this repository demonstrates the complete Machine Learning Engineering lifecycle including:

- Data Cleaning
- Exploratory Data Analysis
- Statistical Analysis
- Feature Engineering
- Model Development
- Model Explainability
- Production Pipeline
- REST API Development
- Docker Deployment

---

# Business Problem

Accurately estimating taxi trip duration improves:

- Customer experience
- Fleet management
- ETA estimation
- Driver scheduling
- Pricing optimization

---

# Dataset

NYC Yellow Taxi Trip Records

Main Features:

- VendorID
- Passenger Count
- Trip Distance
- Pickup Hour
- Pickup Weekday
- Pickup Week
- Pickup Month
- Pickup Latitude
- Pickup Longitude
- RateCodeID

Target Variable

Trip Duration (minutes)

---

# Project Workflow

```
Raw Data
      │
      ▼
Data Cleaning
      │
      ▼
EDA
      │
      ▼
Statistical Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
SHAP Explainability
      │
      ▼
Production Pipeline
      │
      ▼
FastAPI
      │
      ▼
Docker
```

---

# Repository Structure

```text
app/
artifacts/
assets/
data/
logs/
models/
notebook/
reports/
src/
tests/

Dockerfile
requirements.txt
README.md
```

---

# Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- SHAP
- FastAPI
- Docker
- Joblib
- Matplotlib

---

# Machine Learning Pipeline

✔ Data Cleaning

✔ Feature Engineering

✔ Model Training

✔ Hyperparameter Tuning

✔ Model Evaluation

✔ Explainability

✔ Production Pipeline

---

# Model Performance

| Model | MAE | RMSE | R² |
|--------|------:|------:|------:|
| Linear Regression | ... | ... | ... |
| Decision Tree | ... | ... | ... |
| Random Forest | **2.496** | **3.893** | **0.815** |

---

# REST API

Endpoints

GET /

GET /health

POST /predict

Interactive Documentation

```
http://127.0.0.1:8000/docs
```

---

# Docker

Build

```bash
docker build -t nyc-taxi-api .
```

Run

```bash
docker run -d -p 8000:8000 nyc-taxi-api
```

---

# Future Improvements

- XGBoost
- LightGBM
- Traffic Data
- Weather Data
- CI/CD
- Cloud Deployment
- Model Monitoring

---

# Author

Mahmoud Morsy

GitHub

https://github.com/morsycoo

LinkedIn

https://linkedin.com/in/mahmudmursi

Kaggle

https://kaggle.com/mahmoudmorsy

---

# License

MIT License