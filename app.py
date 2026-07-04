import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("🩺 Diabetes Prediction System")

st.markdown("""
# 🩺 Diabetes Prediction System

### AI Powered Health Screening

Predict the likelihood of diabetes using a trained Machine Learning model.
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🤖 Model", "Logistic Regression")

with col2:
    st.metric("📊 Accuracy", "90%")

with col3:
    st.metric("🧪 Features", "8")

with col4:
    st.metric("⚡ Status", "Ready")

st.markdown("---")

st.subheader("✨ Project Features")

st.markdown("""
✅ Diabetes Prediction

✅ Machine Learning Model

✅ Interactive Dashboard

✅ Analytics Charts

✅ Health Recommendations

✅ Modern User Interface
""")

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
# LOAD CSS
# -----------------------------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.image(
    "https://img.icons8.com/color/240/medical-doctor.png",
    width=120
)

st.sidebar.title("Diabetes AI")

st.sidebar.markdown("---")

st.sidebar.success("🟢 System Ready")

st.sidebar.markdown(
"""
### Navigation

🏠 Home

🩺 Prediction

📊 Analytics

ℹ️ About
"""
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
Model : Logistic Regression

Dataset : Diabetes Prediction

Version : 1.0
"""
)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div class="header">

<h1>🩺 Diabetes Prediction System</h1>

<p>
Predict Diabetes using Machine Learning
</p>

</div>
""",unsafe_allow_html=True)

st.write("")

# -----------------------------
# CARDS
# -----------------------------
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
    <h2>100000</h2>
    <p>Dataset Records</p>
    </div>
    """,unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h2>96%</h2>
    <p>Model Accuracy</p>
    </div>
    """,unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h2>8</h2>
    <p>Input Features</p>
    </div>
    """,unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
    <h2>AI</h2>
    <p>Prediction Ready</p>
    </div>
    """,unsafe_allow_html=True)

st.write("")
st.write("")

left,right = st.columns([2,1])

with left:

    st.markdown("""
    ## Welcome 👋

    This application predicts whether a patient is diabetic or not.

    ### Features

    ✔ Fast Prediction

    ✔ Machine Learning Model

    ✔ Interactive Dashboard

    ✔ Analytics

    ✔ Professional UI

    """)

with right:

    st.info("""
Patient Information Required

• Gender

• Age

• Hypertension

• Heart Disease

• Smoking History

• BMI

• HbA1c Level

• Blood Glucose Level
""")

st.write("")
st.write("")

st.markdown("---")

st.caption("Developed by Krishna Jamdar ❤️")

st.markdown("---")

st.caption("© 2026 Diabetes Prediction System | Developed by Krishna Jamdar")