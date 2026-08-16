import streamlit as st
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import asyncio
import re 
from html import escape

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

with st.sidebar:
    st.markdown("""<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="width:48px;height:48px;border-radius:14px;background:linear-gradient(135deg,#6366f1,#8b5cf6);display:flex;align-items:center;justify-content:center;font-size:26px;">🤖</div>
<div>
<div style="font-size:21px;font-weight:700;color:white;">AI Consultant</div>
<div style="font-size:12px;color:#c7d2fe;margin-top:4px;">Business Intelligence & Strategy</div>
</div>
</div>""", unsafe_allow_html=True)
      

    st.divider()

    st.markdown("### 📊 Dashboard")
    st.write("Business Analysis")
    st.write("Market Research")
    st.write("Competitor Analysis")
    st.write("Financial Analysis")

    st.divider()

    st.markdown("### 📄 Reports")
    st.write("Executive Report")
    st.write("PDF Report")

# =========================
# CUSTOM UI
# =========================

st.markdown("""
<style>

/* Remove unnecessary top spacing */
[data-testid="stSidebar"] > div:first-child {
    padding-top: 1rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #172554 100%);
}

[data-testid="stSidebar"] .block-container {
    padding-top: 1rem;
    padding-left: 1.2rem;
    padding-right: 1.2rem;
}

/* Sidebar title */
.sidebar-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 4px;
}

.sidebar-subtitle {
    font-size: 13px;
    opacity: 0.75;
    margin-bottom: 20px;
}

/* Main page */
.main-title {
    font-size: 38px;
    font-weight: 750;
    margin-bottom: 5px;
}

.main-subtitle {
    font-size: 16px;
    opacity: 0.75;
    margin-bottom: 25px;
}

/* Reduce excessive Streamlit spacing */
.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">🤖 AI Management Consultant</div>
<div class="main-subtitle">
Multi-agent AI platform for business analysis, market research,
financial analysis and strategic recommendations.
</div>
""", unsafe_allow_html=True)

st.write(
    "Multi-agent AI platform for business analysis, market research, "
    "financial analysis and strategic recommendations."
)
with st.container(border=True):
    st.markdown("### 📊 Business Data")
    st.caption("Upload a CSV or Excel file containing your business data.")

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
        # KPI Dashboard
        st.subheader("📊 Business KPI Dashboard")

        numeric_cols = df.select_dtypes(include="number").columns

        if len(numeric_cols) > 0:
            cols = st.columns(min(4, len(numeric_cols)))
            for i, col in enumerate(numeric_cols[:4]):
                cols[i].metric(
                    label=col,
                    value=f"{df[col].sum():,.2f}"
                )
        else:
            st.info("No numeric columns available for KPI calculation.")

        # KPI Visualization
        if len(numeric_cols) > 0:
            st.subheader("📈 KPI Visualization")
            selected_kpi = st.selectbox(
                "Select KPI to visualize",
                numeric_cols
                )
        st.line_chart(df[selected_kpi])

        # Automatic Business Insights
        st.subheader("💡 Automatic Business Insights")

        for col in numeric_cols[:4]:
            total = df[col].sum()
            average = df[col].mean()
            maximum = df[col].max()
            minimum = df[col].min()

            st.write(f"### {col}")
            st.write(f"- **Total:** {total:,.2f}")
            st.write(f"- **Average:** {average:,.2f}")
            st.write(f"- **Highest:** {maximum:,.2f}")
            st.write(f"- **Lowest:** {minimum:,.2f}")

        # Download Business Report
        st.subheader("📥 Download Business Report")
        report = f"""
        AI MANAGEMENT CONSULTANT — BUSINESS REPORT
        Dataset Size:
        Rows: {df.shape[0]}
        Columns: {df.shape[1]}
        KEY BUSINESS METRICS:
        """
        for col in numeric_cols[:4]:
            report += f"""
            {col}
            Total: {df[col].sum():,.2f}
            Average: {df[col].mean():,.2f}
            Highest: {df[col].max():,.2f}
            Lowest: {df[col].min():,.2f}
            """

        pdf_buffer = BytesIO()
        doc = SimpleDocTemplate(pdf_buffer, pagesize=A4)
        styles = getSampleStyleSheet()
        story = [Paragraph("AI MANAGEMENT CONSULTANT – BUSINESS REPORT", styles["Title"])]
        
        for line in report.split("\n"):
            if line.strip():
                story.append(Paragraph(escape(line.strip()), styles["BodyText"]))
                story.append(Spacer(1, 5))

        doc.build(story)
        pdf_buffer.seek(0)

        st.download_button(
            label="📥 Download Business Report PDF",
            data=pdf_buffer,
            file_name="business_report.pdf",
            mime="application/pdf"
            )

        # AI Data Insights
        st.subheader("🧠 AI Data Insights")
        if len(numeric_cols) > 0:
            data_for_ai = df.head(30).to_string(index=False)
            data_insight_prompt = f"""
            You are a business data analyst.
            Analyze the following business dataset and provide actionable insights.

            Dataset:
            {data_for_ai}
            Identify:
            1. Best-performing areas
            2. Worst-performing areas
            3. Important trends or patterns
            4. Potential business problems
            5. Business opportunities
            6. Three practical recommendations
            Use only information supported by the provided data.
            If the data is insufficient for a conclusion, clearly say so.
            """
            with st.spinner("🧠 AI is analyzing your business data..."):
                insight_result = asyncio.run(
                    Runner.run(
                        agent,
                        data_insight_prompt
                        )
                        )
            st.write(insight_result.final_output)


    except Exception as e:
        st.error(f"Error reading file: {e}")

st.markdown("## 📥 Business Input")
st.caption("Describe your business problem and provide the data you want the AI consultant to analyze.")

with st.container(border=True):
    st.markdown("### 💼 Business Problem")
    st.caption("Tell the AI consultant what you want to understand or improve.")

    business_problem = st.text_area(
        "Describe your business problem:",
        placeholder=(
            "Example: My online electronics business is growing in revenue, "
            "but I am not sure which products are driving profitability."
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
final_output = ""



if st.button("🚀 Analyze Business", type="primary", use_container_width=True):

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
st.markdown("## 📊 AI Analysis Results")
st.caption("Review the complete business analysis, insights, risk assessment and strategic recommendations.")

st.header("📋 Executive Consultant Report")
st.write(final_output)
# AI Risk Assessment
st.divider()
st.subheader("⚠️ AI Risk Assessment")

risk_prompt = f"""
You are a senior business risk analyst.

Analyze the following business consulting report:

{final_output}

Create a concise risk assessment.

Evaluate:

1. Financial Risk
2. Market Risk
3. Operational Risk
4. Customer Risk
5. Overall Business Risk

For each risk:
- Give a risk level: LOW, MEDIUM, or HIGH
- Explain the main reason
- Give one practical mitigation action

Finally provide:
Overall Risk Level: LOW, MEDIUM, or HIGH

Use only information supported by the consulting report.
Do not invent numerical data.
"""

with st.spinner("⚠️ AI is assessing business risks..."):
    risk_result = asyncio.run(
        Runner.run(
            agent,
            risk_prompt
        )
    )

st.write(risk_result.final_output)


# Recommendation Priority Matrix
st.divider()
st.subheader("🎯 Recommendation Priority Matrix")

priority_prompt = f"""
You are a senior business strategy consultant.

Analyze this consulting report:

{final_output}

Create a recommendation priority matrix.

Identify the 5 most important recommendations.

For each recommendation provide:

1. Recommendation
2. Priority: HIGH, MEDIUM, or LOW
3. Expected Impact: HIGH, MEDIUM, or LOW
4. Implementation Difficulty: EASY, MEDIUM, or HARD
5. Short reason

Finally identify the ONE recommendation that should be implemented first.

Use only information supported by the consulting report.
Do not invent numerical data.
"""

with st.spinner("🎯 Prioritizing recommendations..."):
    priority_result = asyncio.run(
        Runner.run(
            agent,
            priority_prompt
        )
    )

st.write(priority_result.final_output)

# What-If Scenario Analysis
st.divider()
st.subheader("🔮 What-If Scenario Analysis")

scenario = st.text_input(
    "Describe a business scenario you want to evaluate:",
    placeholder="Example: What if marketing spending increases by 20%?"
)

if scenario:
    scenario_prompt = f"""
You are a business strategy consultant.

Here is the original consulting report:

{final_output}

The user wants to evaluate this scenario:

{scenario}

Analyze the potential business impact of this scenario.

Provide:
1. Scenario Summary
2. Expected Impact on Revenue
3. Expected Impact on Costs
4. Expected Impact on Customers
5. Potential Benefits
6. Potential Risks
7. Recommended Action

Do not invent exact numerical results unless they are supported
by the provided data. Clearly state when an estimate cannot be
calculated from the available information.
"""

    with st.spinner("🔮 Analyzing business scenario..."):
        scenario_result = asyncio.run(
            Runner.run(
                agent,
                scenario_prompt
            )
        )

    st.write(scenario_result.final_output)

# Data Quality & Anomaly Detection
st.divider()
st.subheader("🔎 Data Quality & Anomaly Detection")

st.write("### Data Quality Check")

if uploaded_file is not None:

    # Missing values
    missing_values = df.isnull().sum()
    total_missing = int(missing_values.sum())

    # Duplicate rows
    duplicate_rows = int(df.duplicated().sum())

    # Total rows and columns
    total_rows = int(df.shape[0])
    total_columns = int(df.shape[1])

    # Display summary
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Rows", total_rows)

    with col2:
        st.metric("Total Columns", total_columns)

    with col3:
        st.metric("Missing Values", total_missing)

    with col4:
        st.metric("Duplicate Rows", duplicate_rows)

    st.write("### Missing Values by Column")

    missing_table = missing_values[
        missing_values > 0
    ].reset_index()

    missing_table.columns = ["Column", "Missing Values"]

    if len(missing_table) > 0:
        st.dataframe(
            missing_table,
            use_container_width=True
        )
    else:
        st.success("✅ No missing values detected.")

    st.write("### Duplicate Row Check")

    if duplicate_rows > 0:
        st.warning(
            f"⚠️ {duplicate_rows} duplicate row(s) detected."
        )
    else:
        st.success("✅ No duplicate rows detected.")

else:

    st.info(
        "📂 Upload a CSV or Excel file to perform data quality analysis."
    )

# Numerical outlier detection
st.write("### 📈 Outlier Detection")

numeric_columns = df.select_dtypes(include="number").columns

if len(numeric_columns) > 0:

    outlier_data = []

    for col in numeric_columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[
            (df[col] < lower_bound) |
            (df[col] > upper_bound)
        ]

        outlier_data.append({
            "Column": col,
            "Outliers": len(outliers)
        })

    outlier_df = pd.DataFrame(outlier_data)

    st.dataframe(outlier_df)

else:
    st.info("No numerical columns available for outlier detection.")

# Business Trend Analysis
st.divider()
st.subheader("📈 Business Trend Analysis")

if len(numeric_cols) > 0:

    trend_column = st.selectbox(
        "Select a business metric for trend analysis",
        numeric_cols,
        key="trend_metric"
    )

    trend_data = df[trend_column].dropna()

    if len(trend_data) >= 2:

        first_value = trend_data.iloc[0]
        last_value = trend_data.iloc[-1]

        if first_value != 0:
            percentage_change = (
                (last_value - first_value) / abs(first_value)
            ) * 100
        else:
            percentage_change = 0

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Starting Value",
                f"{first_value:,.2f}"
            )

        with col2:
            st.metric(
                "Latest Value",
                f"{last_value:,.2f}"
            )

        with col3:
            st.metric(
                "Change",
                f"{percentage_change:.2f}%"
            )

        st.line_chart(trend_data)

        if percentage_change > 0:
            st.success(
                f"📈 {trend_column} shows an overall increasing trend."
            )
        elif percentage_change < 0:
            st.warning(
                f"📉 {trend_column} shows an overall decreasing trend."
            )
        else:
            st.info(
                f"➡️ {trend_column} shows no overall change."
            )

    else:
        st.info("Not enough data points for trend analysis.")

else:
    st.info("No numerical columns available for trend analysis.")

# Business Segmentation
st.divider()
st.subheader("👥 Business Segmentation")

categorical_cols = df.select_dtypes(
    include=["object", "category"]
).columns.tolist()

if len(categorical_cols) > 0:

    segment_col = st.selectbox(
        "Select a category for segmentation",
        categorical_cols,
        key="segment_column"
    )

    segment_counts = df[segment_col].value_counts().head(10)

    st.write("### Segment Distribution")
    st.bar_chart(segment_counts)

    if len(numeric_cols) > 0:

        segment_metric = st.selectbox(
            "Select metric to compare",
            numeric_cols,
            key="segment_metric"
        )

        segment_performance = (
            df.groupby(segment_col)[segment_metric]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

        st.write("### Segment Performance")
        st.bar_chart(segment_performance)

        if len(segment_performance) > 0:
            best_segment = segment_performance.index[0]

            st.success(
                f"🏆 Best performing segment: {best_segment}"
            )

else:
    st.info("No categorical columns available for segmentation.")

# AI Business Data Chat
st.divider()
st.subheader("💬 Ask AI About Your Business Data")

if uploaded_file is not None:

    data_context = df.head(50).to_string(index=False)

    user_question = st.text_input(
        "Ask a question about your uploaded data:",
        placeholder="Example: Which product has the highest revenue?"
    )

    if user_question:

        chat_prompt = f"""
You are an expert business data analyst.

The user uploaded the following business dataset:

{data_context}

The user asks:

{user_question}

Answer the question using only the available dataset.

If the dataset does not contain enough information to answer,
clearly explain what information is missing.

Give a concise and practical business-oriented answer.
"""

        with st.spinner("🤖 AI is analyzing your question..."):

            chat_result = asyncio.run(
                Runner.run(
                    agent,
                    chat_prompt
                )
            )

        st.write("### 🤖 AI Answer")
        st.write(chat_result.final_output)

else:
    st.info("Upload a CSV or Excel file to ask questions about your data.")

# Advanced Business Comparison
st.divider()
st.subheader("📊 Advanced Business Comparison")

if len(numeric_cols) >= 2:

    comparison_cols = st.multiselect(
        "Select up to 3 metrics to compare",
        numeric_cols,
        max_selections=3,
        key="comparison_metrics"
    )

    if len(comparison_cols) >= 2:

        comparison_data = df[comparison_cols]

        st.write("### Metric Comparison")
        st.bar_chart(comparison_data)

        st.write("### Comparison Summary")

        summary_data = pd.DataFrame({
            "Metric": comparison_cols,
            "Average": [
                df[col].mean()
                for col in comparison_cols
            ],
            "Total": [
                df[col].sum()
                for col in comparison_cols
            ],
            "Maximum": [
                df[col].max()
                for col in comparison_cols
            ]
        })

        st.dataframe(
            summary_data,
            use_container_width=True
        )

    else:
        st.info("Select at least 2 metrics to compare.")

else:
    st.info(
        "At least two numerical columns are required "
        "for comparison analysis."
    )

# AI Action Plan
st.divider()
st.subheader("🎯 AI Action Plan")

action_prompt = f"""
You are a senior management consultant.

Based on the following consulting report:

{final_output}

Create a practical business action plan.

Divide the plan into:

1. Immediate Actions (0–30 days)
2. Short-Term Actions (1–3 months)
3. Long-Term Actions (3–12 months)

For every action provide:
- Action
- Business objective
- Priority: HIGH, MEDIUM, or LOW
- Expected benefit
- KPI to monitor
- Suggested timeline

Finally provide the TOP 3 actions management should start with.

Keep the recommendations practical and supported by the consulting report.
Do not invent numerical data.
"""

with st.spinner("🎯 Creating AI action plan..."):
    action_result = asyncio.run(
        Runner.run(
            agent,
            action_prompt
        )
    )

st.write("### 📋 Recommended Action Plan")
st.write(action_result.final_output)

# Executive Decision Scorecard
st.divider()
st.subheader("📋 Executive Decision Scorecard")

scorecard_prompt = f"""
You are a senior management consultant.

Based on the consulting report below:

{final_output}

Create an executive decision scorecard.

Evaluate these areas:

1. Financial Performance
2. Market Position
3. Customer Performance
4. Operational Performance
5. Growth Potential

For each area provide:
- Rating: POOR, FAIR, GOOD, or EXCELLENT
- Short explanation
- Most important improvement needed

Then provide:

Overall Business Health:
POOR / FAIR / GOOD / EXCELLENT

Top 3 Management Priorities:
1.
2.
3.

Key Decision:
Give one clear decision that management should consider next.

Use only information supported by the consulting report.
Do not invent numerical data.
"""

with st.spinner("📋 Preparing executive decision scorecard..."):
    scorecard_result = asyncio.run(
        Runner.run(
            agent,
            scorecard_prompt
        )
    )

st.write(scorecard_result.final_output)

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
        rightMargin=45,
        leftMargin=45,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    styles["Title"].fontSize = 20
    styles["Title"].leading = 24
    styles["Heading1"].fontSize = 16
    styles["Heading1"].leading = 20
    styles["Heading2"].fontSize = 13
    styles["Heading2"].leading = 17
    styles["BodyText"].fontSize = 10
    styles["BodyText"].leading = 15
    styles["BodyText"].spaceAfter = 8

    story = []

    # Main title
    story.append(
        Paragraph(
            "AI Management Consultant Report",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    # IMPORTANT:
    # Do NOT add final_output here because it already summarizes
    # the individual consultant outputs and causes duplication.

    sections = [
        ("Business Analysis", business_output),
        ("Market Research", market_output),
        ("Competitor Benchmarking", benchmark_output),
        ("Financial Analysis", financial_output),
        ("Strategy Recommendations", strategy_output),
        ("AI Risk Assessment", risk_result.final_output),
        ("Recommendation Priority Matrix", priority_result.final_output),
        ("AI Action Plan", action_result.final_output),
        ("Executive Decision Scorecard", scorecard_result.final_output),
    ]

    for section_title, content in sections:

        # Section heading
        story.append(
            Paragraph(
                escape(section_title),
                styles["Heading1"]
            )
        )

        story.append(Spacer(1, 10))

        content = str(content).strip()

        # Split into paragraphs using blank lines
        paragraphs = re.split(r"\n\s*\n", content)

        for paragraph in paragraphs:

            paragraph = paragraph.strip()

            if not paragraph:
                continue

            # Convert markdown headings
            if paragraph.startswith("### "):
                text = escape(paragraph[4:].strip())

                story.append(
                    Paragraph(
                        text,
                        styles["Heading2"]
                    )
                )

            elif paragraph.startswith("## "):
                text = escape(paragraph[3:].strip())

                story.append(
                    Paragraph(
                        text,
                        styles["Heading1"]
                    )
                )

            # Bullet points
            elif paragraph.startswith("- ") or paragraph.startswith("* "):
                lines = paragraph.split("\n")

                for line in lines:
                    line = line.strip()

                    if line.startswith("- ") or line.startswith("* "):
                        line = line[2:].strip()

                    story.append(
                        Paragraph(
                            "• " + escape(line),
                            styles["BodyText"]
                        )
                    )

            # Normal paragraph
            else:
                text = escape(paragraph)

                # Convert **bold** text
                text = re.sub(
                    r"\*\*(.*?)\*\*",
                    r"<b>\1</b>",
                    text
                )

                # Convert numbered lines into readable paragraphs
                text = text.replace("\n", " ")

                story.append(
                    Paragraph(
                        text,
                        styles["BodyText"]
                    )
                )

            story.append(Spacer(1, 6))

        # Space between major sections
        story.append(Spacer(1, 15))

    # Build PDF
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