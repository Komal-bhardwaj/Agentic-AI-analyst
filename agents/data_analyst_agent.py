from llm.llm_config import get_llm

def data_analyst_agent(eda_summary, insights):
    llm = get_llm()

    prompt = f"""
You are a professional data analyst.

EDA Summary:
{eda_summary}

Initial Insights:
{insights}

Tasks:
1. Explain the dataset in simple terms
2. Highlight key patterns
3. Identify data quality issues
4. Suggest next steps for analysis

Respond in clear bullet points.
"""

    response = llm.invoke(prompt)
    return response
