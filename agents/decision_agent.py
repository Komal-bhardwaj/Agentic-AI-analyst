from llm.llm_config import get_llm

def decision_agent(validated_text):
    llm = get_llm()

    prompt = f"""
You are a business decision-maker.

Based on the validated analysis:
{validated_text}

Tasks:
- Derive actionable decisions
- Highlight risks
- Suggest business actions
"""

    return llm.invoke(prompt)
