"""
============================================================
Training script for Linear Regression and Logistic Regression
models. Saves both models as .pkl files for use in the
Streamlit app.
============================================================
"""
import os
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, accuracy_score


# -------- 1. Paths --------
DATA_PATH = "data/car_data.csv"
MODELS_DIR = "models"
os.makedirs(MODELS_DIR, exist_ok=True)


# -------- 2. Load the dataset --------
df = pd.read_csv(DATA_PATH)
print(f"[INFO] Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")


# ============================================================
# 3. Train Linear Regression (predict Selling Price)
# ============================================================
print("\n[STEP] Training Linear Regression...")

linear_X = df[['Year', 'Present_Price', 'Kms_Driven', 'Owner']]
linear_y = df['Selling_Price']

X_train, X_test, y_train, y_test = train_test_split(
    linear_X, linear_y,
    test_size=0.2,
    random_state=42
)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

linear_preds = linear_model.predict(X_test)
linear_mae = mean_absolute_error(y_test, linear_preds)
print(f"       MAE = {linear_mae:.4f}")

joblib.dump(linear_model, f"{MODELS_DIR}/linear_model.pkl")
print(f"       [OK] Saved: {MODELS_DIR}/linear_model.pkl")


# ============================================================
# 4. Train Logistic Regression (classify Expensive / Not)
# ============================================================
print("\n[STEP] Training Logistic Regression...")

# Create a new binary column: 1 if price >= median, else 0
median_price = df['Selling_Price'].median()
df['Expensive'] = (df['Selling_Price'] >= median_price).astype(int)
print(f"       Median Price = {median_price:.2f}")

logistic_X = df[['Year', 'Present_Price', 'Kms_Driven', 'Owner']]
logistic_y = df['Expensive']

X_train, X_test, y_train, y_test = train_test_split(
    logistic_X, logistic_y,
    test_size=0.2,
    random_state=42,
    stratify=logistic_y
)

logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_train, y_train)

logistic_preds = logistic_model.predict(X_test)
logistic_acc = accuracy_score(y_test, logistic_preds)
print(f"       Accuracy = {logistic_acc:.4f}")

joblib.dump(logistic_model, f"{MODELS_DIR}/logistic_model.pkl")
print(f"       [OK] Saved: {MODELS_DIR}/logistic_model.pkl")


print("\n[DONE] All models have been saved successfully in the 'models/' directory.")