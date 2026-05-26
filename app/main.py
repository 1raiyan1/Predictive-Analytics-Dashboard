from fastapi import FastAPI, UploadFile, File, Form
from app.analyzer import analyze_csv
import pandas as pd
import io

app = FastAPI()

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    api_key: str = Form(...)
):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))
    
    analysis = analyze_csv(df, api_key)
    
    stats = {
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "describe": df.describe().to_dict()
    }
    
    return {
        "analysis": analysis,
        "stats": stats,
        "preview": df.head(10).to_dict()
    }