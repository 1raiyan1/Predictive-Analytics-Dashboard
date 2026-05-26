from groq import Groq
import pandas as pd
import json

def analyze_csv(df, api_key):
    client = Groq(api_key=api_key)
    
    summary = {
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "sample": df.head(5).to_string(),
        "stats": df.describe().to_string()
    }
    
    prompt = f"""You are a data analyst. Analyze this dataset and provide insights.

Dataset Summary:
- Rows: {summary['rows']}
- Columns: {summary['columns']}
- Data Types: {summary['dtypes']}

Sample Data:
{summary['sample']}

Statistical Summary:
{summary['stats']}

Provide:
1. KEY INSIGHTS: 3-5 important findings from the data
2. TRENDS: Any trends or patterns you notice
3. RECOMMENDATIONS: 3 actionable recommendations based on the data
4. PREDICTIONS: What might happen next based on current trends

Be specific and mention actual column names and numbers from the data."""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content