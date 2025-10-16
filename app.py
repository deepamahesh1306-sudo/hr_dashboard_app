import streamlit as st
import pandas as pd
import numpy as np

st.title("🏢 HR Dashboard")
st.write("Employee data & attrition insights")

# Upload CSV file
uploaded_file = st.file_uploader("Upload Employee CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Employee Data")
    st.dataframe(df)

    # Attrition count
    st.subheader("Attrition Overview")
    if 'Attrition' in df.columns:
        attrition_count = df['Attrition'].value_counts()
        st.bar_chart(attrition_count)
    
    # Average Salary
    if 'MonthlyIncome' in df.columns:
        st.subheader("Average Salary")
        st.metric("Average Monthly Income", int(df['MonthlyIncome'].mean()))
    
    # Department wise count
    if 'Department' in df.columns:
        st.subheader("Department Distribution")
        dept_count = df['Department'].value_counts()
        st.bar_chart(dept_count)
else:
    st.info("Upload a CSV file to see HR dashboard")
