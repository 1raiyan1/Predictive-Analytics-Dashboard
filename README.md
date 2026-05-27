# AI Predictive Analytics Dashboard 📊

An AI-powered analytics dashboard that lets you upload any CSV file and get instant insights, visualizations, and predictions.

🔗 **Live Demo:** [https://predictive-analytics-dashboard-mmbwcuevypqvjvkmxpah2t.streamlit.app](https://predictive-analytics-dashboard-mmbwcuevypqvjvkmxpah2t.streamlit.app)

App Preview
<img width="1919" height="1016" alt="image" src="https://github.com/user-attachments/assets/e9bedbbd-d5c4-453b-8b3d-bfba056e894a" />
<img width="1919" height="1025" alt="image" src="https://github.com/user-attachments/assets/c91cd2b6-ea93-452f-8723-56442a036cec" />
<img width="1919" height="1020" alt="image" src="https://github.com/user-attachments/assets/782671de-7cae-4c89-9c20-9590c0075fc0" />
<img width="1919" height="1015" alt="image" src="https://github.com/user-attachments/assets/1214d8c4-3009-4edd-b134-15a263350db2" />

## Features
- Upload any CSV dataset
- Instant data preview and statistics
- Interactive charts and visualizations (scatter plots, histograms)
- AI-powered insights, trends and predictions
- Powered by Groq LLM (free & fast)

## Tech Stack
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Data Analysis:** Pandas
- **Visualizations:** Plotly
- **LLM:** Groq (Llama 3.1)

## How to Run Locally

1. Clone the repo
2. Create a virtual environment and install dependencies:
```bash
pip install -r requirements.txt
```
3. Run FastAPI backend:
```bash
uvicorn app.main:app --reload
```
4. Run Streamlit frontend:
```bash
streamlit run streamlit_app.py
```
5. Open http://localhost:8501 and upload any CSV file!

## Demo
Upload any CSV → View charts → Generate AI insights instantly!
