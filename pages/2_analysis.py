import streamlit as st
import pandas as pd
import plotly.express as px

# 👇 FIRST
st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

# 👇 NANTAR function
def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# 👇 NANTAR call
load_css()

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

st.title("📊 Diabetes Analytics Dashboard")

# Dataset Load
df = pd.read_csv("final_data.csv")

# Top Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Records", len(df))

with col2:
    st.metric("Features", len(df.columns)-1)

with col3:
    diabetic = df["diabetes"].sum()
    st.metric("Diabetic Patients", diabetic)

with col4:
    non = len(df)-diabetic
    st.metric("Non-Diabetic", non)

st.markdown("---")

# BMI Chart
fig1 = px.histogram(
    df,
    x="bmi",
    color="diabetes",
    title="BMI Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

# Age Chart
fig2 = px.histogram(
    df,
    x="age",
    color="diabetes",
    title="Age Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# Blood Glucose
fig3 = px.box(
    df,
    x="diabetes",
    y="blood_glucose_level",
    title="Blood Glucose Level"
)

st.plotly_chart(fig3, use_container_width=True)

# HbA1c
fig4 = px.scatter(
    df,
    x="HbA1c_level",
    y="blood_glucose_level",
    color="diabetes",
    title="HbA1c vs Blood Glucose"
)

st.plotly_chart(fig4, use_container_width=True)


st.markdown("---")

st.subheader("📋 Dataset Summary")

st.dataframe(df.describe(), use_container_width=True)

st.markdown("---")

st.subheader("👀 First 10 Records")

st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")

st.caption("© 2026 Diabetes Prediction System | Analytics Dashboard")
