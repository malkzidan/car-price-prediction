"""
============================================================
Streamlit app for Car Price Prediction.
- Predicts the selling price (Linear Regression)
- Classifies the car as Expensive / Not Expensive (Logistic Regression)
Themed with a Pink & White color palette.
============================================================
"""
import streamlit as st
import pandas as pd
import joblib


# -------- Page configuration --------
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🌸",
    layout="centered"
)


# ============================================================
# Custom CSS: Pink & White theme
# ============================================================
st.markdown("""
<style>
    /* -------- Global background (soft pink gradient) -------- */
    .stApp {
        background: linear-gradient(135deg, #FFF0F5 0%, #FFFFFF 50%, #FFE4EC 100%);
    }

    /* -------- Main title -------- */
    h1 {
        color: #D6336C !important;
        text-align: center;
        font-weight: 800 !important;
        letter-spacing: 0.5px;
        text-shadow: 0 2px 8px rgba(214, 51, 108, 0.15);
    }

    /* -------- Subheaders -------- */
    h2, h3 {
        color: #C2185B !important;
        font-weight: 700 !important;
    }

    /* -------- Paragraph text -------- */
    p, label, .stMarkdown {
        color: #4A4A4A !important;
    }

    /* -------- Sidebar -------- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFD9E4 0%, #FFFFFF 100%);
        border-right: 2px solid #FFB6C9;
    }

    section[data-testid="stSidebar"] h2 {
        color: #D6336C !important;
        border-bottom: 2px solid #FFB6C9;
        padding-bottom: 8px;
    }

    /* -------- Buttons -------- */
    .stButton > button {
        background: linear-gradient(135deg, #FF7EB6 0%, #D6336C 100%);
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 0.6em 1.4em;
        font-weight: 700;
        font-size: 15px;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(214, 51, 108, 0.3);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #D6336C 0%, #A61E4D 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(214, 51, 108, 0.45);
    }

    /* -------- Metrics (Predicted Price & Classification) -------- */
    div[data-testid="stMetric"] {
        background: white;
        border: 2px solid #FFB6C9;
        border-radius: 16px;
        padding: 18px 20px;
        box-shadow: 0 6px 16px rgba(214, 51, 108, 0.12);
        transition: all 0.3s ease;
    }

    div[data-testid="stMetric"]:hover {
        border-color: #D6336C;
        box-shadow: 0 8px 22px rgba(214, 51, 108, 0.25);
        transform: translateY(-3px);
    }

    div[data-testid="stMetricLabel"] {
        color: #C2185B !important;
        font-weight: 600 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #D6336C !important;
        font-weight: 800 !important;
    }

    /* -------- Success message (Expensive) -------- */
    div[data-testid="stAlert"][class*="stSuccess"] {
        background-color: #FFE4EC !important;
        border-left: 6px solid #D6336C !important;
        color: #A61E4D !important;
        border-radius: 10px;
    }

    /* -------- Info message (Not Expensive) -------- */
    div[data-testid="stAlert"][class*="stInfo"] {
        background-color: #FFF0F5 !important;
        border-left: 6px solid #FF7EB6 !important;
        color: #C2185B !important;
        border-radius: 10px;
    }

    /* -------- Expander -------- */
    details {
        background: white !important;
        border: 2px solid #FFB6C9 !important;
        border-radius: 12px !important;
        padding: 6px 12px !important;
    }

    details summary {
        color: #D6336C !important;
        font-weight: 600 !important;
    }

    /* -------- Slider (Pink track) -------- */
    div[data-testid="stSlider"] > div > div > div > div {
        background-color: #D6336C !important;
    }

    /* -------- Number input & Selectbox borders -------- */
    div[data-testid="stNumberInput"] input,
    div[data-testid="stSelectbox"] > div > div {
        border: 2px solid #FFB6C9 !important;
        border-radius: 10px !important;
    }

    div[data-testid="stNumberInput"] input:focus,
    div[data-testid="stSelectbox"] > div > div:focus-within {
        border-color: #D6336C !important;
        box-shadow: 0 0 0 2px rgba(214, 51, 108, 0.2) !important;
    }

    /* -------- Caption footer -------- */
    .stCaption {
        text-align: center;
        color: #C2185B !important;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)


# -------- Load trained models (cached) --------
@st.cache_resource
def load_models():
    """Load both trained models from the models/ directory."""
    linear_model = joblib.load("models/linear_model.pkl")
    logistic_model = joblib.load("models/logistic_model.pkl")
    return linear_model, logistic_model


linear_model, logistic_model = load_models()


# -------- Header --------
st.title("🌸 Car Price Prediction 🌸")
st.markdown(
    "<p style='text-align:center; font-size:17px; color:#C2185B;'>"
    "Enter the car details in the sidebar to predict its <b>selling price</b> "
    "and classify it as <b>Expensive</b> or <b>Not Expensive</b>."
    "</p>",
    unsafe_allow_html=True
)
st.markdown("---")


# -------- Sidebar: user inputs --------
st.sidebar.header("🚗 Car Details")

year = st.sidebar.slider(
    "Manufacturing Year",
    min_value=2003,
    max_value=2018,
    value=2017,
    step=1
)

present_price = st.sidebar.number_input(
    "Present Price (in lakhs)",
    min_value=0.0,
    max_value=100.0,
    value=8.5,
    step=0.1
)

kms_driven = st.sidebar.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=500000,
    value=15000,
    step=500
)

owner = st.sidebar.selectbox(
    "Number of Previous Owners",
    options=[0, 1, 2, 3],
    index=0
)

st.sidebar.markdown("---")


# -------- Predict button --------
if st.sidebar.button("Predict 🚀"):

    # Build input DataFrame with the same column names used in training
    input_df = pd.DataFrame({
        "Year": [year],
        "Present_Price": [present_price],
        "Kms_Driven": [kms_driven],
        "Owner": [owner],
    })

    # Make predictions
    predicted_price = linear_model.predict(input_df)[0]
    predicted_class = logistic_model.predict(input_df)[0]

    # -------- Display results --------
    st.subheader("💖 Prediction Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Predicted Selling Price",
            value=f"{predicted_price:.2f} lakhs"
        )

    with col2:
        if predicted_class == 1:
            st.metric(label="Classification", value="Expensive 💰")
        else:
            st.metric(label="Classification", value="Not Expensive 🌷")

    st.markdown("<br>", unsafe_allow_html=True)

    # Extra feedback
    if predicted_class == 1:
        st.success("✨ This car is classified as **Expensive**.")
    else:
        st.info("🌸 This car is classified as **Not Expensive**.")

    # Show the input summary
    with st.expander("🔍 See input details"):
        st.dataframe(input_df, use_container_width=True)


# -------- Footer --------
st.markdown("---")
st.caption("💗 Built with Streamlit + Scikit-learn")