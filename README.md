<div align="center">

# 🚖 NYC Yellow Taxi Trip Duration Prediction

### End-to-End Machine Learning Engineering Project

*A complete production-ready machine learning system for predicting NYC taxi trip duration using statistical analysis, feature engineering, model explainability, FastAPI, and Docker.*

<br>

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Regression-orange?style=for-the-badge&logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/FastAPI-Production_API-009688?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

<br>

![GitHub stars](https://img.shields.io/github/stars/morsycoo/NYC-Yellow-Taxi-Trip-Duration-Prediction?style=social)
![GitHub forks](https://img.shields.io/github/forks/morsycoo/NYC-Yellow-Taxi-Trip-Duration-Prediction?style=social)

</div>

---

# 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🎯 Business Problem](#-business-problem)
- [💼 Business Value](#-business-value)
- [⭐ Project Highlights](#-project-highlights)
- [📂 Dataset](#-dataset)
- [📊 Dataset Overview](#-dataset-overview)
- [🏗 Repository Structure](#-repository-structure)
- [🛠 Technology Stack](#-technology-stack)
- [📈 Exploratory Data Analysis](#-exploratory-data-analysis)
- [📉 Statistical Analysis](#-statistical-analysis)
- [⚙ Feature Engineering](#-feature-engineering)
- [🤖 Machine Learning Models](#-machine-learning-models)
- [🏆 Final Production Model](#-final-production-model)
- [📊 Model Performance](#-model-performance)
- [🔍 Model Explainability](#-model-explainability)
- [🏭 Production Pipeline](#-production-pipeline)
- [🚀 REST API](#-rest-api)
- [🐳 Docker Deployment](#-docker-deployment)
- [📖 API Documentation](#-api-documentation)
- [⚡ Prediction Workflow](#-prediction-workflow)
- [💾 Installation](#-installation)
- [▶ Running the Project](#-running-the-project)
- [📷 Results](#-results)
- [📚 Lessons Learned](#-lessons-learned)
- [🚀 Future Improvements](#-future-improvements)
- [👨‍💻 Author](#-author)
- [📄 License](#-license)

---

# 📌 Project Overview

This project was developed as a complete **Machine Learning Engineering** project rather than a traditional notebook-based machine learning solution.

The objective is to accurately predict the duration of New York City yellow taxi trips using historical trip information while demonstrating the complete lifecycle of building, evaluating, deploying, and serving a production-ready regression model.

Unlike many machine learning repositories that stop after model training, this project continues through every stage required in a real production environment—from raw data preprocessing to a deployable REST API running inside a Docker container.

Throughout this project, the complete engineering workflow was implemented, including:

- Business Understanding
- Data Cleaning & Validation
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Feature Engineering
- Regression Modeling
- Model Evaluation
- Hyperparameter Optimization
- Feature Importance Analysis
- SHAP Explainability
- Production Pipeline Construction
- Model Serialization
- REST API Development
- Input Validation
- Logging
- Exception Handling
- Docker Deployment
- Interactive Swagger Documentation

The final outcome is a reusable, scalable, and production-ready machine learning system suitable for deployment and portfolio presentation.

---

# 🎯 Business Problem

Trip duration prediction plays a critical role in modern transportation systems.

Accurate travel time estimation directly affects both customer satisfaction and operational efficiency.

Taxi companies and ride-sharing platforms rely heavily on travel time prediction for:

- Estimated Time of Arrival (ETA)
- Driver Allocation
- Fleet Optimization
- Dynamic Pricing
- Route Planning
- Customer Experience
- Operational Cost Reduction

The goal of this project is to build a regression model capable of estimating taxi trip duration with high accuracy while maintaining interpretability and production readiness.

---

# 💼 Business Value

A reliable trip duration prediction system provides value across multiple stakeholders.

### 🚖 For Taxi Companies

- Better fleet utilization
- Reduced idle time
- More efficient dispatching
- Increased operational efficiency

---

### 👨‍✈️ For Drivers

- Better trip planning
- Reduced waiting time
- Improved daily scheduling

---

### 👤 For Customers

- More accurate ETAs
- Improved ride experience
- Better trust in the platform

---

### 📊 For Business Analysts

- Demand forecasting
- Traffic pattern analysis
- Performance monitoring
- Service optimization

---

# ⭐ Project Highlights

This repository demonstrates the implementation of a complete Machine Learning Engineering workflow.

✔ End-to-End Regression Project

✔ Production Machine Learning Pipeline

✔ Comprehensive Exploratory Data Analysis

✔ Statistical Inference & Hypothesis Testing

✔ Advanced Feature Engineering

✔ Multiple Regression Models

✔ Hyperparameter Optimization

✔ Feature Importance Analysis

✔ SHAP Explainability

✔ Production Serialization

✔ FastAPI REST API

✔ Request Validation with Pydantic

✔ Production Logging

✔ Exception Handling

✔ Docker Deployment

✔ Interactive Swagger Documentation

✔ Portfolio-Ready Project

---

# 📂 Dataset

The project uses the **NYC Yellow Taxi Trip Records** dataset.

The dataset contains millions of taxi trips collected from New York City's Taxi & Limousine Commission (TLC).

Each trip includes spatial, temporal, and operational information describing the taxi ride.

The objective is to predict the trip duration using historical trip characteristics.

---

## Dataset Features

The dataset includes features such as:

- VendorID
- Passenger Count
- Trip Distance
- Pickup Datetime
- Dropoff Datetime
- Pickup Latitude
- Pickup Longitude
- Dropoff Latitude
- Dropoff Longitude
- RateCodeID
- Payment Type
- Store and Forward Flag

Additional engineered temporal features were created during preprocessing.

---

## Target Variable

The prediction target is:

```text
Trip Duration (minutes)
```

This is treated as a supervised regression problem.

---

# 📊 Dataset Overview

| Property | Value |
|----------|-------|
| Problem Type | Supervised Regression |
| Domain | Transportation Analytics |
| Dataset | NYC Yellow Taxi Trips |
| Target | Trip Duration |
| ML Task | Regression |
| Explainability | SHAP |
| Deployment | FastAPI + Docker |

---

## Data Processing Pipeline

The raw dataset undergoes several preprocessing stages before model training.

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Missing Value Handling
      │
      ▼
Outlier Treatment
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
```

---

# 🏗 Repository Structure

```text
NYC-Yellow-Taxi-Trip-Duration-Prediction/

├── app/
│   ├── main.py
│   ├── predictor.py
│   ├── schemas.py
│   ├── logger.py
│   └── config.py
│
├── artifacts/
│   ├── feature_names.pkl
│   ├── metadata.json
│   └── metrics.json
│
├── assets/
│   ├── images/
│   └── diagrams/
│
├── data/
│
├── logs/
│
├── models/
│   └── production_pipeline.pkl
│
├── notebooks/
│   └── nyc_taxi_trip_duration_prediction.ipynb
│
├── reports/
│
├── src/
│   ├── preprocessing.py
│   ├── training.py
│   ├── evaluation.py
│   ├── explainability.py
│   ├── inference.py
│   └── utils.py
│
├── tests/
│
├── Dockerfile
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🛠 Technology Stack

## Programming

- Python

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib

## Machine Learning

- Scikit-Learn

## Explainability

- SHAP

## Model Serialization

- Joblib

## API Development

- FastAPI
- Pydantic

## Deployment

- Docker
- Uvicorn

## Development

- Git
- GitHub
- Jupyter Notebook

---

> **Next:** Exploratory Data Analysis → Statistical Analysis → Feature Engineering → Machine Learning Models → Performance Comparison.

