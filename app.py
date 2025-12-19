import streamlit as st
from analysis.data_loader import load_data
from analysis.eda import basic_eda
from analysis.insights import generate_insights
from agents.data_analyst_agent import data_analyst_agent
from agents.agent_graph import agent_app

st.title("📊 Agentic AI Data Analyst")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    eda = basic_eda(df)
    insights = generate_insights(df)

    st.subheader("🔍 EDA Summary")
    st.json(eda)

    st.subheader("💡 Rule-Based Insights")
    for i in insights:
        st.write("•", i)

    # SINGLE AGENT ANALYSIS
    if st.button("🧠 Ask AI Data Analyst"):
        with st.spinner("Analyzing like a senior data analyst..."):
            ai_response = data_analyst_agent(eda, insights)
        st.subheader("🤖 AI Data Analyst Report")
        st.write(ai_response)

    # MULTI-AGENT + REFINEMENT
    if st.button("🧠 Run Agentic AI Analysis with Refinement"):
        with st.spinner("AI agents working..."):
            result = agent_app.invoke({
                "eda": eda,
                "insights": insights,
                "df": df  # pass original dataset
            })

        st.subheader("📘 Final AI Report")
        st.write(result["report"])

        st.subheader("🗄 Refined Dataset")
        st.dataframe(result["refined_df"])

        # Provide download option
        csv = result["refined_df"].to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Refined CSV",
            data=csv,
            file_name="refined_dataset.csv",
            mime="text/csv"
        )
