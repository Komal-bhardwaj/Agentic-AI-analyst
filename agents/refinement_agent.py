import pandas as pd
from llm.llm_config import get_llm

def refinement_agent(df: pd.DataFrame, report_text: str) -> pd.DataFrame:
    """
    df: Original dataset
    report_text: Output from Report Agent
    Returns a refined DataFrame according to report recommendations
    """

    llm = get_llm()

    prompt = f"""
You are a data engineer AI.

Here is the report based on a dataset:
{report_text}

Your task:
- Suggest programmatic refinements to the original dataset
- Explain changes in Python/pandas format
- Only suggest operations applicable to the given dataset

Output only the Python code to transform the DataFrame.
"""

    code = llm.invoke(prompt)

    # Execute the code safely
    local_vars = {"df": df.copy(), "pd": pd}
    try:
        exec(code, {}, local_vars)
        refined_df = local_vars.get("df", df)
    except Exception as e:
        print("Refinement code failed:", e)
        refined_df = df

    return refined_df
