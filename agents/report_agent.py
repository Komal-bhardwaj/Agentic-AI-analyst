from llm.llm_config import get_llm

def report_agent(decision_text):
    llm = get_llm()

    prompt = f"""
You are a professional report writer.

Create a final structured report from:
{decision_text}

Format:
- Executive Summary
- Key Findings
- Recommendations
"""

    return llm.invoke(prompt)
