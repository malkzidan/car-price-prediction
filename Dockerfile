# ============================================================
# Dockerfile for Car Price Prediction Streamlit App
# ============================================================

# -------- 1. Base image --------
FROM python:3.12-slim

# -------- 2. Working directory inside the container --------
WORKDIR /app

# -------- 3. Copy requirements first (for better caching) --------
COPY requirements.txt .

# -------- 4. Install Python dependencies --------
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# -------- 5. Copy the rest of the project --------
COPY data/ ./data/
COPY src/ ./src/
COPY app.py .
COPY models/ ./models/

# -------- 6. Expose Streamlit port --------
EXPOSE 8501

# -------- 7. Run the app --------
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]