from llm.llm_config import get_llm

def validator_agent(analysis_text):
    llm = get_llm()

    prompt = f"""
You are a senior data reviewer.

Review the following analysis:
{analysis_text}

Tasks:
- Validate insights
- Point out weak or unsupported claims
- Suggest corrections if needed
"""

    return llm.invoke(prompt)
