<div align="center">

# 🚗 Car Price Prediction

### End-to-End Machine Learning Project for Predicting Car Prices and Classifying Cars as Expensive or Not Expensive

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)](https://www.docker.com/)

[![Docker Pulls](https://img.shields.io/docker/pulls/malakzidan/car-price-app?style=for-the-badge\&logo=docker)](https://hub.docker.com/r/malakzidan/car-price-app)

</div>

---

## 🎯 About

**Car Price Prediction** is an end-to-end Machine Learning project built to analyze used cars and make two types of predictions:

* 💰 **Price Prediction:** Predicts the selling price of a used car using **Linear Regression**.
* 🏷️ **Price Classification:** Classifies cars as **Expensive** or **Not Expensive** using **Logistic Regression**.
* 🌐 **Web Application:** Provides an interactive **Streamlit** interface for real-time predictions.
* 🐳 **Containerization:** The application is packaged as a **Docker image** for easy deployment.

---

## 📊 Model Results

| Model               | Task                 | Metric   |      Score |
| ------------------- | -------------------- | -------- | ---------: |
| Linear Regression   | Price Prediction     | MAE      |   **1.39** |
| Logistic Regression | Price Classification | Accuracy | **95.08%** |

---

## 🛠️ Tech Stack

* 🐍 Python 3.12
* 🧮 NumPy
* 🐼 Pandas
* 🤖 Scikit-learn
* 🌐 Streamlit
* 🐳 Docker

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/malakzidan/Car-Price-Prediction.git
cd Car-Price-Prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## 🐳 Run with Docker

You can run the application directly using the published Docker image.

```bash
docker run -p 8501:8501 malakzidan/car-price-app:v1
```

Then open:

```text
http://localhost:8501
```

### Docker Hub

[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-car--price--app-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)](https://hub.docker.com/r/malakzidan/car-price-app)

---

## 🔄 Project Workflow

```text
Raw Car Data
     │
     ▼
Data Cleaning & Preprocessing
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Feature Engineering
     │
     ├──────────────────────┐
     ▼                      ▼
Linear Regression     Logistic Regression
     │                      │
     ▼                      ▼
Selling Price         Expensive /
Prediction            Not Expensive
     │                      │
     └──────────┬───────────┘
                ▼
         Streamlit App
                │
                ▼
           Docker Image
```

---

## 📁 Project Structure

```text
Car-Price-Prediction/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── data/
│   └── car_data.csv
│
└── models/
    ├── linear_regression.pkl
    └── logistic_regression.pkl
```

---

## 💡 Features

### 💰 Price Prediction

Enter the car details and the application predicts the expected **selling price** using the trained Linear Regression model.

### 🏷️ Price Classification

The application also determines whether the car is classified as:

* 🔴 **Expensive**
* 🟢 **Not Expensive**

using Logistic Regression.

---

## 👩‍💻 Author

### Malak Zidan

🎓 Computer Science Student
📊 Data Analyst & AI Enthusiast

* 🔗 [GitHub](https://github.com/malakzidan)
* 🐳 [Docker Hub](https://hub.docker.com/u/malakzidan)
* 💼 [LinkedIn](https://www.linkedin.com/)

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

</div>
