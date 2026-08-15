import streamlit as st
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import asyncio

from agents import Agent, Runner
from main import (
    agent,
    market_researcher,
    benchmarking_agent,
    financial_analyst,
    strategy_advisor,
)


st.set_page_config(
    page_title="AI Management Consultant",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 AI Management Consultant")
st.write(
    "Multi-agent AI platform for business analysis, market research, "
    "financial analysis and strategic recommendations."
)
st.subheader("📊 Upload Business Data")

uploaded_file = st.file_uploader(
    "Upload your business data (CSV or Excel)",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("✅ File uploaded successfully!")

        st.write("### 📋 Data Preview")
        st.dataframe(df.head(10))

        st.write("### 📊 Dataset Summary")
        st.write(f"**Rows:** {df.shape[0]}")
        st.write(f"**Columns:** {df.shape[1]}")

    except Exception as e:
        st.error(f"Error reading file: {e}")

st.subheader("💼 Business Problem")

business_problem = st.text_area(
    "Describe your business problem:",
    placeholder=(
        "Example: My online clothing business has high website traffic "
        "but low sales."
    ),
    height=150
)


async def run_consulting_team(problem):

    business = await Runner.run(
        agent,
        problem
    )

    market = await Runner.run(
        market_researcher,
        problem
    )

    benchmark = await Runner.run(
        benchmarking_agent,
        problem
    )

    financial = await Runner.run(
        financial_analyst,
        problem
    )

    strategy = await Runner.run(
        strategy_advisor,
        problem
    )

    final_consultant = Agent(
        name="Final Consultant",
        instructions="""
        You are the lead management consultant.

        Create a professional executive-level business consulting report
        using the outputs provided by the specialist agents.

        Include:

        1. Executive Summary
        2. Main Business Problem
        3. Business Analysis
        4. Market Research
        5. Competitor Benchmarking
        6. Financial Analysis
        7. Strategic Recommendations
        8. Priority Action Plan
        9. Key KPIs to Monitor
        10. Risks and Next Steps

        Keep the report clear, practical and structured.
        Do not invent numerical data that was not provided.
        """,
    )

    combined_information = f"""
    ORIGINAL BUSINESS PROBLEM:
    {problem}

    BUSINESS ANALYST:
    {business.final_output}

    MARKET RESEARCH:
    {market.final_output}

    COMPETITOR BENCHMARKING:
    {benchmark.final_output}

    FINANCIAL ANALYSIS:
    {financial.final_output}

    STRATEGY ADVISOR:
    {strategy.final_output}
    """

    final = await Runner.run(
        final_consultant,
        combined_information
    )

    return (
        business.final_output,
        market.final_output,
        benchmark.final_output,
        financial.final_output,
        strategy.final_output,
        final.final_output,
    )

business_output = ""
market_output = ""
benchmark_output = ""
financial_output = ""
strategy_output = ""


if st.button("🚀 Analyze Business", type="primary"):

    if not business_problem.strip():

        st.warning("Please enter a business problem first.")

    else:

        with st.spinner(
            "🤖 AI consulting team is analyzing your business..."
        ):

            # Prepare business problem with uploaded data
            problem_for_ai = business_problem

if uploaded_file is not None:
    data_summary = df.head(20).to_string(index=False)

    problem_for_ai = f"""
{business_problem}

ADDITIONAL BUSINESS DATA:
The user uploaded a business dataset.

Dataset size:
- Rows: {df.shape[0]}
- Columns: {df.shape[1]}

Column names:
{", ".join(df.columns.astype(str))}

Sample data:
{data_summary}

Please use this data as supporting evidence in your business analysis.
Identify important patterns, possible problems, and actionable insights.
"""
results = asyncio.run(
run_consulting_team(business_problem)
)
            
(
    business_output,
    market_output,
    benchmark_output,
    financial_output,
    strategy_output,
    final_output
) = results

st.success("✅ Complete analysis generated!")


st.divider()

st.header("📋 Executive Consultant Report")
st.write(final_output)

st.divider()

with st.expander("📊 Business Analysis"):
            st.write(business_output)

with st.expander("🌐 Market Research"):
            st.write(market_output)

with st.expander("🏆 Competitor Benchmarking"):
            st.write(benchmark_output)

with st.expander("💰 Financial Analysis"):
            st.write(financial_output)

with st.expander("🎯 Strategy Recommendations"):
            st.write(strategy_output)

st.divider()

st.subheader("📄 Download Full Report")

from html import escape

def create_pdf():
    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    story = []

    story.append(
        Paragraph("AI Management Consultant Report", styles["Title"])
    )
    story.append(Spacer(1, 15))

    sections = [
        ("Business Analysis", business_output),
        ("Market Research", market_output),
        ("Competitor Benchmarking", benchmark_output),
        ("Financial Analysis", financial_output),
        ("Strategy Recommendations", strategy_output),
    ]

    for title, content in sections:
        story.append(Paragraph(title, styles["Heading2"]))
        story.append(Spacer(1, 8))

        for line in str(content).split("\n"):
            if line.strip():
                story.append(
                    Paragraph(
                        escape(line),
                        styles["BodyText"]
                    )
                )
                story.append(Spacer(1, 5))

        story.append(Spacer(1, 10))

    doc.build(story)

    buffer.seek(0)
    return buffer


pdf_file = create_pdf()

st.download_button(
    label="📥 Download PDF Report",
    data=pdf_file,
    file_name="AI_Management_Consultant_Report.pdf",
    mime="application/pdf"
)