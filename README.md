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

# 📈 Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to understand the structure, quality, and behavior of the NYC Yellow Taxi dataset before model development.

Rather than immediately training a regression model, the project focused on discovering hidden patterns, identifying anomalies, and validating assumptions about the data.

The analysis covered:

- Dataset structure inspection
- Data types verification
- Missing value analysis
- Duplicate detection
- Distribution analysis
- Correlation analysis
- Temporal analysis
- Geographic distribution
- Outlier detection

---

## Key Findings

### Trip Duration Distribution

The target variable exhibited a highly right-skewed distribution.

Most taxi trips were relatively short, while a very small percentage represented unusually long journeys.

This observation justified:

- Outlier investigation
- Robust evaluation metrics
- Careful interpretation of prediction errors

---

### Trip Distance

Trip distance showed one of the strongest positive relationships with trip duration.

As expected:

- Longer trips generally required more travel time.
- Extremely long distances often corresponded to higher prediction uncertainty.

---

### Temporal Patterns

Temporal analysis revealed noticeable demand variations across:

- Hours of the day
- Days of the week
- Months

Rush-hour periods consistently produced longer average trip durations due to traffic congestion.

---

### Missing Values

The cleaned dataset contained no critical missing values after preprocessing.

Data quality checks ensured consistency before model training.

---

### Outliers

Several extreme observations were detected.

Examples included:

- Unrealistically long trips
- Extremely short trips
- Abnormal travel distances

Instead of blindly removing all outliers, they were carefully analyzed to distinguish between legitimate observations and data anomalies.

---

## Visualizations

The notebook includes:

- Target Distribution
- Trip Distance Distribution
- Correlation Heatmap
- Hourly Demand Analysis
- Weekly Demand Analysis
- Monthly Demand Analysis
- Scatter Plots
- Box Plots
- Histogram Analysis

---

# 📉 Statistical Analysis

Beyond traditional exploratory analysis, this project incorporated statistical methods to better understand the underlying characteristics of the data.

The objective was not only to build an accurate model but also to validate assumptions using statistical reasoning.

---

## Topics Covered

The statistical analysis included:

- Probability Theory
- Conditional Probability
- Joint Probability
- Marginal Probability
- Bayes' Theorem
- Sampling
- Sampling Distribution
- Central Limit Theorem
- Confidence Intervals
- Hypothesis Testing
- Correlation Analysis
- Covariance Analysis

---

## Confidence Intervals

Confidence intervals were used to estimate population statistics while accounting for sampling uncertainty.

Rather than relying on single-point estimates, interval estimation provided a more realistic representation of uncertainty.

---

## Hypothesis Testing

Hypothesis testing was applied to investigate whether observed differences in trip characteristics were statistically significant.

The project introduced concepts including:

- Null Hypothesis
- Alternative Hypothesis
- Test Statistics
- P-values
- Statistical Significance

---

## Business Perspective

Statistical analysis helps distinguish genuine business patterns from random fluctuations.

This improves confidence in model development and supports evidence-based decision making.

---

# ⚙️ Feature Engineering

Feature engineering played a central role in improving predictive performance.

Raw taxi records were transformed into informative numerical features that better captured temporal and operational behavior.

---

## Engineered Features

Temporal features:

- Pickup Hour
- Pickup Weekday
- Pickup Week
- Pickup Month

Operational features:

- Passenger Count
- VendorID
- RateCodeID

Spatial features:

- Pickup Latitude
- Pickup Longitude

Target:

- Trip Duration

---

## Why Feature Engineering Matters

Machine learning models rely heavily on feature quality.

Well-designed features often contribute more to predictive performance than choosing increasingly complex algorithms.

---

## Engineering Decisions

Several design principles guided feature creation:

- Avoid data leakage
- Preserve interpretability
- Keep preprocessing reproducible
- Maintain compatibility with the production pipeline

---

# 🤖 Machine Learning Models

Several regression algorithms were evaluated throughout the project.

Each model served a different purpose during experimentation.

---

## Linear Regression

Used as the baseline model.

Advantages:

- Fast
- Highly interpretable
- Establishes a performance benchmark

Limitations:

- Assumes linear relationships
- Limited capacity for nonlinear patterns

---

## Decision Tree Regressor

Introduced nonlinear decision boundaries.

Advantages:

- Easy to interpret
- Captures nonlinear relationships

Limitations:

- High variance
- Sensitive to overfitting

---

## Random Forest Regressor

The final production model.

Advantages:

- Strong predictive performance
- Robust against overfitting
- Handles nonlinear interactions
- Stable across different datasets

---

# 📊 Model Performance

The following table summarizes the performance of the main regression models evaluated throughout the project.

| Model | MAE ↓ | RMSE ↓ | R² ↑ | Status |
|--------|------:|-------:|------:|:------:|
| Linear Regression | 3.828 | 5.519 | 0.628 | Baseline |
| Decision Tree | 2.637 | 4.114 | 0.793 | Tuned |
| Random Forest | **2.496** | **3.893** | **0.815** | 🏆 Production |

---

## Performance Improvement

| Model Evolution | MAE Improvement | RMSE Improvement | R² Improvement |
|-----------------|---------------:|-----------------:|---------------:|
| Linear Regression → Decision Tree | **31.1% ↓** | **25.5% ↓** | **+26.3%** |
| Decision Tree → Random Forest | **5.3% ↓** | **5.4% ↓** | **+2.7%** |
| Linear Regression → Random Forest | **34.8% ↓** | **29.5% ↓** | **+29.8%** |

---

## Final Production Model

🏆 **Random Forest Regressor (Final)**

| Metric | Value |
|--------|------:|
| MAE | **2.496413** |
| RMSE | **3.893483** |
| R² Score | **0.814663** |
| Training Time | **270.36 sec** |

---

## 📊 Complete Benchmark Results

| Rank | Model | MAE ↓ | RMSE ↓ | R² ↑ | Training Time (sec) | Status |
|-----:|--------|------:|-------:|------:|--------------------:|:------:|
| 🥇 1 | Random Forest (Final) | **2.496413** | **3.893483** | **0.814663** | 270.36 | 🚀 Production |
| 🥈 2 | Random Forest (Baseline) | 2.601847 | 4.057575 | 0.798712 | 101.01 | Baseline |
| 🥉 3 | Decision Tree (Tuned) | 2.636622 | 4.114148 | 0.793060 | 58.99 | Tuned |
| 4 | Decision Tree (Default) | 3.504377 | 5.506155 | 0.629334 | 92.85 | Initial |
| 5 | Linear Regression | 3.828084 | 5.519339 | 0.627557 | **2.79** | Baseline |

The optimized Random Forest model achieved the best overall balance between prediction accuracy, robustness, and generalization. It was therefore selected as the final production model and integrated into the deployment pipeline.

---


