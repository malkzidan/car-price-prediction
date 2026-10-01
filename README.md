markdown

<div align="center">

# 🚗 Car Price Prediction

### End-to-end Machine Learning project for predicting car prices and classifying them as Expensive or Not Expensive

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

[![Docker Pulls](https://img.shields.io/docker/pulls/malakzidan/car-price-app?style=for-the-badge&logo=docker)](https://hub.docker.com/r/malakzidan/car-price-app)

</div>

---

## 🎯 About

An end-to-end ML project that:

- **Predicts** used car selling prices using **Linear Regression**.
- **Classifies** cars as **Expensive** or **Not Expensive** using **Logistic Regression**.
- Provides a **Streamlit** web app for real-time predictions.
- Ships as a **Docker image** for easy deployment.

---

## 📈 Results

| Model               | Metric   | Score      |
| ------------------- | -------- | ---------- |
| Linear Regression   | MAE      | **1.39**   |
| Logistic Regression | Accuracy | **95.08%** |

---

## 🚀 Run Locally

````bash
pip install -r requirements.txt
streamlit run app.py
Open: http://localhost:8501

🐳 Run with Docker
bash
docker run -p 8501:8501 malakzidan/car-price-app:v1
Open: http://localhost:8501

Docker Hub: malakzidan/car-price-app

🛠️ Tech Stack
Python 3.12 · scikit-learn · Streamlit · Docker · pandas · numpy

👩‍💻 Author
Malak Zidan — GitHub · Docker Hub

<div align="center">
⭐ If you found this useful, give it a star!

</div> ```
````
