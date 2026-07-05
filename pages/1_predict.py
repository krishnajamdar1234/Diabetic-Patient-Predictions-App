import streamlit as st
import pickle
import numpy as np
from pathlib import Path

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# LOAD CSS
# -----------------------------
def load_css():
    css_file = Path(__file__).parent.parent / "style.css"

    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🩺 Diabetes Prediction System")
st.sidebar.markdown("---")
st.sidebar.success("Machine Learning Project")

st.sidebar.info("""
Algorithm :
• Logistic Regression

Developer :
Krishna Jamdar
""")

st.sidebar.markdown("---")

# -----------------------------
# LOAD MODEL
# -----------------------------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# TITLE
# -----------------------------
st.title("🩺 Diabetes Prediction System")
st.caption("AI Powered Diabetes Prediction using Machine Learning")

# -----------------------------
# TOP METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🤖 Model", "Logistic Regression")

with col2:
    st.metric("📊 Features", "8")

with col3:
    st.metric("✅ Status", "Ready")

st.markdown("---")

st.subheader("📝 Enter Patient Details")

# -----------------------------
# INPUTS
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=25
    )

    hypertension = st.selectbox(
        "Hypertension",
        [0, 1]
    )

    heart_disease = st.selectbox(
        "Heart Disease",
        [0, 1]
    )

with col2:

    smoking_history = st.selectbox(
        "Smoking History",
        [0, 1, 2, 3, 4, 5]
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=70.0,
        value=25.0
    )

    hba1c = st.number_input(
        "HbA1c Level",
        min_value=3.0,
        max_value=15.0,
        value=5.5
    )

    blood_glucose = st.number_input(
        "Blood Glucose Level",
        min_value=50,
        max_value=400,
        value=100
    )

# -----------------------------
# ENCODING
# -----------------------------
gender = 0 if gender == "Female" else 1

st.markdown("---")

predict = st.button(
    "🔮 Predict Diabetes",
    use_container_width=True
)


# -----------------------------
# PREDICTION
# -----------------------------
if predict:

    features = np.array([[
        gender,
        age,
        hypertension,
        heart_disease,
        smoking_history,
        bmi,
        hba1c,
        blood_glucose
    ]])

    prediction = model.predict(features)
    probability = model.predict_proba(features)

    confidence = float(np.max(probability)) * 100

    st.markdown("---")

    # RESULT
    if prediction[0] == 1:

        st.error("🔴 Diabetes Detected")

    else:

        st.success("🟢 No Diabetes Detected")

    # CONFIDENCE
    st.subheader("Prediction Confidence")

    st.progress(confidence / 100)

    st.write(f"Confidence : {confidence:.2f}%")

    # RISK LEVEL
    st.subheader("Risk Assessment")

    if confidence >= 90:
        st.error("🔴 High Confidence")

    elif confidence >= 70:
        st.warning("🟡 Medium Confidence")

    else:
        st.info("🟢 Low Confidence")

    # -----------------------------
    # HEALTH RECOMMENDATION
    # -----------------------------
    st.subheader("💡 Health Recommendation")

    if prediction[0] == 1:

        st.warning("""
✔ Please consult a healthcare professional.

✔ Follow a balanced diet.

✔ Exercise regularly.

✔ Monitor your blood glucose level.

✔ Reduce sugar intake.
""")

    else:

        st.success("""
✔ Great! No diabetes detected.

✔ Continue regular exercise.

✔ Maintain a healthy diet.

✔ Drink enough water.

✔ Get regular health checkups.
""")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:gray;">
        <h4>🩺 Diabetes Prediction System</h4>
        <p>Developed by <b>Krishna Jamdar</b> ❤️</p>
    </div>
    """,
    unsafe_allow_html=True
)
