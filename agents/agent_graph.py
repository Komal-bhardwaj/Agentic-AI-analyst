from langgraph.graph import StateGraph
from typing import TypedDict
import pandas as pd

# Import all agents
from agents.data_analyst_agent import data_analyst_agent
from agents.validator_agent import validator_agent
from agents.decision_agent import decision_agent
from agents.report_agent import report_agent
from agents.refinement_agent import refinement_agent

# Define the state schema
class AgentState(TypedDict):
    eda: dict
    insights: list
    df: pd.DataFrame        # Original dataset
    analysis: str
    validated: str
    decision: str
    report: str
    refined_df: pd.DataFrame

# ---------------------------
# CREATE THE AGENT GRAPH
# ---------------------------
graph = StateGraph(AgentState)

# 1️⃣ Data Analyst Agent
graph.add_node("analyze", lambda state: {
    "analysis": data_analyst_agent(state["eda"], state["insights"])
})

# 2️⃣ Validator Agent
graph.add_node("validate", lambda state: {
    "validated": validator_agent(state["analysis"])
})

# 3️⃣ Decision Agent
graph.add_node("decide", lambda state: {
    "decision": decision_agent(state["validated"])
})

# 4️⃣ Report Agent
graph.add_node("report", lambda state: {
    "report": report_agent(state["decision"])
})

# 5️⃣ Refinement Agent (applies report suggestions to CSV)
graph.add_node("refine", lambda state: {
    "refined_df": refinement_agent(state["df"], state["report"])
})

# ---------------------------
# SET THE FLOW OF AGENTS
# ---------------------------
graph.set_entry_point("analyze")

graph.add_edge("analyze", "validate")
graph.add_edge("validate", "decide")
graph.add_edge("decide", "report")
graph.add_edge("report", "refine")

# ---------------------------
# COMPILE THE GRAPH
# ---------------------------
agent_app = graph.compile()
