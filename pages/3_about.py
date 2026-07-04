import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Sidebar
st.sidebar.title("🩺 Diabetes Prediction System")

st.sidebar.markdown("---")

st.sidebar.success("About Project")

st.sidebar.info("""
Algorithm:
• Logistic Regression

Developer:
Krishna Jamdar
""")

st.sidebar.markdown("---")

# Title
st.title("ℹ️ About This Project")

st.markdown("---")

st.header("🩺 Project Overview")

st.write("""
This Diabetes Prediction System uses a Machine Learning model
(Logistic Regression) to predict whether a patient is diabetic
based on health parameters.
""")

st.header("📌 Features")

st.markdown("""
- ✅ Diabetes Prediction
- ✅ Interactive Dashboard
- ✅ Analytics Visualization
- ✅ Machine Learning Model
- ✅ User Friendly Interface
""")

st.header("🛠️ Technologies Used")

st.markdown("""
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
""")

st.header("👨‍💻 Developer")

st.success("Krishna Jamdar")

st.markdown("---")

st.caption("© 2026 Diabetes Prediction System")