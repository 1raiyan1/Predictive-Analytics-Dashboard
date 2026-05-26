import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import json

st.set_page_config(page_title="AI Analytics Dashboard", page_icon="📊", layout="wide")
st.title("📊 AI Predictive Analytics Dashboard")
st.markdown("Upload any CSV file — AI will analyze it and give you insights instantly!")

st.divider()

api_key = st.text_input("Enter your Groq API Key", type="password")
uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file and api_key:
    df = pd.read_csv(uploaded_file)
    uploaded_file.seek(0)
    
    st.subheader("📋 Data Preview")
    st.dataframe(df.head(10))
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", len(df))
    col2.metric("Total Columns", len(df.columns))
    col3.metric("Missing Values", df.isnull().sum().sum())
    
    st.divider()
    
    st.subheader("📈 Visualizations")
    
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    
    if len(numeric_cols) >= 2:
        col1, col2 = st.columns(2)
        
        with col1:
            x_col = st.selectbox("X Axis", numeric_cols)
        with col2:
            y_col = st.selectbox("Y Axis", numeric_cols, index=1)
        
        fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
        st.plotly_chart(fig, use_container_width=True)
        
        fig2 = px.histogram(df, x=numeric_cols[0], title=f"Distribution of {numeric_cols[0]}")
        st.plotly_chart(fig2, use_container_width=True)
    
    st.divider()
    
    if st.button("🤖 Generate AI Insights"):
        with st.spinner("AI is analyzing your data..."):
            files = {"file": (uploaded_file.name, uploaded_file, "text/csv")}
            data = {"api_key": api_key}
            
            response = requests.post(
                "http://localhost:8000/analyze",
                files=files,
                data=data
            )
            
            if response.status_code == 200:
                result = response.json()
                
                st.subheader("🧠 AI Analysis")
                st.markdown(result["analysis"])
            else:
                st.error("Something went wrong!")