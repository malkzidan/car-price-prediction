<div align="center">

# 🚗 Car Price Prediction

### End-to-end Machine Learning project for predicting car prices and classifying them as **Expensive** or **Not Expensive**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

[![Docker Pulls](https://img.shields.io/docker/pulls/malakzidan/car-price-app?style=for-the-badge&logo=docker)](https://hub.docker.com/r/malakzidan/car-price-app)
[![GitHub last commit](https://img.shields.io/github/last-commit/malkzidan/car-price-prediction?style=for-the-badge)](https://github.com/malkzidan/car-price-prediction)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Dataset](#-dataset)
- [Machine Learning Models](#-machine-learning-models)
- [Results](#-results)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Docker](#-docker)
- [Screenshots](#-screenshots)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Overview

This project is an **end-to-end Machine Learning application** that:

1. **Predicts** the selling price of a used car using **Linear Regression**.
2. **Classifies** whether a car is **Expensive** or **Not Expensive** using **Logistic Regression**.
3. Provides an interactive **Streamlit** web interface for real-time predictions.
4. Is fully **Dockerized** and available on **Docker Hub** for easy deployment.

---

## ✨ Features

- 🧠 **Two ML models trained** — Linear Regression + Logistic Regression.
- 📊 **Interactive visualizations** — Correlation matrix, feature relationships.
- 🎨 **Beautiful UI** — Pink & White themed Streamlit app.
- 🐳 **Dockerized** — One command to run anywhere.
- 🌐 **Available on Docker Hub** — `docker run -p 8501:8501 malakzidan/car-price-app:v1`
- 📦 **Clean project structure** — Separated data, models, and source code.

---

## 📊 Dataset

The dataset contains information about **301 used cars** with **9 features**:

| Feature         | Description                           |
| --------------- | ------------------------------------- |
| `Car_Name`      | Name of the car                       |
| `Year`          | Manufacturing year                    |
| `Selling_Price` | Price the car was sold for (in lakhs) |
| `Present_Price` | Current showroom price (in lakhs)     |
| `Kms_Driven`    | Total kilometers driven               |
| `Fuel_Type`     | Petrol / Diesel / CNG                 |
| `Seller_Type`   | Dealer / Individual                   |
| `Transmission`  | Manual / Automatic                    |
| `Owner`         | Number of previous owners             |

> 📌 **Note:** Prices are in **Indian lakhs** (1 lakh = 100,000 INR).

---

## 🤖 Machine Learning Models

### 1️⃣ Linear Regression — Price Prediction

- **Goal:** Predict the **selling price** of a car.
- **Features used:** `Year`, `Present_Price`, `Kms_Driven`, `Owner`
- **Target:** `Selling_Price`
- **Train/Test split:** 80% / 20%

### 2️⃣ Logistic Regression — Price Classification

- **Goal:** Classify cars as **Expensive** (1) or **Not Expensive** (0).
- **Threshold:** Median of `Selling_Price` (≈ 3.60 lakhs)
- **Features used:** `Year`, `Present_Price`, `Kms_Driven`, `Owner`
- **Target:** `Expensive` (binary)

---

## 📈 Results

| Model                   | Metric                    | Score      |
| ----------------------- | ------------------------- | ---------- |
| **Linear Regression**   | Mean Absolute Error (MAE) | **1.39**   |
| **Logistic Regression** | Accuracy                  | **95.08%** |

**Sample Predictions:**

| Input                           | Predicted Price | Classification   |
| ------------------------------- | --------------- | ---------------- |
| Year=2017, Price=8.5, Kms=15000 | **6.63 lakhs**  | 💰 Expensive     |
| Year=2008, Price=8.5, Kms=15000 | **2.84 lakhs**  | 🌷 Not Expensive |

---

## 🛠️ Tech Stack

<div align="center">

| Category             | Technology                  |
| -------------------- | --------------------------- |
| **Language**         | Python 3.12                 |
| **ML Libraries**     | scikit-learn, pandas, numpy |
| **Web Framework**    | Streamlit                   |
| **Visualization**    | matplotlib, seaborn         |
| **Containerization** | Docker                      |
| **Registry**         | Docker Hub                  |
| **Version Control**  | Git + GitHub                |

</div>

---

## 📁 Project Structure
