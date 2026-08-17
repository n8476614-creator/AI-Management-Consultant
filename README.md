# 🤖 AI Management Consultant

### Multi-Agent AI Platform for Business Analysis, Strategy & Decision Support

AI Management Consultant is an AI-powered business consulting application built using Python, Streamlit, and the OpenAI Agents SDK.

The application uses specialised AI agents to analyse business problems, business data, market conditions, competitors, financial performance, risks, and strategic opportunities. It combines the results into a detailed executive consulting report and downloadable PDF.

---

## 📌 Project Overview

Businesses often need to analyse multiple areas before making important decisions, such as:

- Business performance
- Revenue and costs
- Product performance
- Market conditions
- Competitor positioning
- Financial performance
- Operational efficiency
- Business risks
- Growth opportunities

Analysing all these areas manually can be time-consuming.

The **AI Management Consultant** solves this problem by using a multi-agent AI consulting system. Different specialised agents analyse different aspects of the business, and their findings are combined into a professional consulting report.

---

## 🎯 Problem Statement

Develop an AI-powered consulting system capable of:

- Analysing business problems
- Researching industries and markets
- Benchmarking competitors
- Identifying operational inefficiencies
- Analysing financial performance
- Identifying business risks
- Recommending business strategies
- Generating professional consulting reports

---

## 💡 Objectives

The main objectives of this project are:

1. Analyse business problems using AI.
2. Analyse uploaded CSV and Excel business data.
3. Identify important business KPIs.
4. Detect missing values, duplicate records, and unusual data.
5. Analyse business trends and segments.
6. Provide market and competitor insights.
7. Analyse financial performance.
8. Identify potential business risks.
9. Generate practical strategic recommendations.
10. Create an executive-level consulting report.
11. Generate a downloadable PDF report.

---
# ✨ Key Features

- 📊 **Business Data Upload** — Upload and analyse business data in CSV and Excel formats.

- 📈 **KPI Dashboard** — Automatically analyse numerical business metrics and visualise important KPIs.

- 💡 **Automatic Business Insights** — Generate insights including totals, averages, highest values, lowest values, and important business patterns.

- 🔎 **Data Quality Analysis** — Detect missing values, duplicate records, and numerical outliers using the IQR method.

- 📈 **Business Trend Analysis** — Analyse selected business metrics, percentage changes, and performance trends.

- 🧩 **Segment Analysis** — Analyse categorical data and compare performance across different business segments.

- 💬 **Ask AI About Business Data** — Ask natural-language questions about the uploaded dataset and receive AI-powered business insights.

- 📊 **Advanced Business Comparison** — Compare multiple business metrics using charts, averages, totals, and maximum values.

- 🤖 **Multi-Agent AI Consulting** — Use specialised AI agents for business analysis, market research, competitor benchmarking, financial analysis, strategy, and report generation.

- 🌐 **Market Research** — Analyse market and industry conditions relevant to the business problem.

- 🏆 **Competitor Benchmarking** — Evaluate competitor positioning and identify competitive insights.

- 💰 **Financial Analysis** — Analyse financial considerations and identify important financial insights.

- 🎯 **Strategic Recommendations** — Generate practical business strategies based on the combined AI analysis.

- ⚠️ **AI Risk Assessment** — Identify financial, market, operational, customer, and overall business risks with mitigation recommendations.

- 📋 **Executive Decision Scorecard** — Evaluate financial performance, market position, customer performance, operational performance, and growth potential.

- 🎯 **AI Action Plan** — Generate immediate, short-term, and long-term business actions with priorities, expected benefits, KPIs, and timelines.

- 📄 **Executive Consultant Report** — Combine all specialist-agent findings into a structured executive-level consulting report.

- 📥 **PDF Report Generation** — Generate and download the final consulting report as a professional PDF.

- 🧠 **AI-Powered Decision Support** — Provide management with data-driven insights, priorities, risks, recommendations, and next steps.

# 🔄 Multi-Agent Workflow

```text
                         👤 USER
                            │
                            ▼
               📋 Business Problem + Data
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼
        📊 Business Data         💼 Business Problem
           Analysis                     │
                │                       │
                └───────────┬───────────┘
                            ▼
                  🤖 AI Consulting Team
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
 🧠 Business Analyst  🌐 Market Researcher  🏆 Benchmarking
        │                   │                   │
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                 ┌──────────┴──────────┐
                 │                     │
                 ▼                     ▼
        💰 Financial Analyst     🎯 Strategy Advisor
                 │                     │
                 └──────────┬──────────┘
                            │
                            ▼
                  📄 Final Consultant
                    / Report Writer
                            │
                            ▼
              📋 Executive Consultant Report
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
       ⚠️ Risk          🎯 Action       📊 Decision
       Assessment          Plan          Scorecard
             │              │              │
             └──────────────┼──────────────┘
                            │
                            ▼
                     📥 PDF Report
```

---

# 🏗️ System Architecture

The AI Management Consultant follows a multi-agent architecture in which the Streamlit application acts as the user interface and orchestration layer.

The system accepts a business problem and optional business data, processes the information, and delegates the consulting task to specialised AI agents.

### Main Components

- **Streamlit UI** — Provides the interactive application interface.
- **Business Data Layer** — Handles CSV and Excel data upload and analysis.
- **AI Agent Layer** — Contains specialised consulting agents.
- **Consulting Workflow** — Coordinates the specialist agents and combines their results.
- **Executive Reporting Layer** — Generates the final consultant report, risk assessment, action plan, and decision scorecard.
- **PDF Generation Layer** — Converts the final consulting output into a downloadable PDF report.

### Architecture Diagram
  ![Architecture diagram](https://github.com/n8476614-creator/AI-Management-Consultant/blob/main/Architecture_diagram%20.jpeg?raw=true)

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core programming language and application logic |
| 🎨 **Streamlit** | Interactive web application and user interface |
| 🤖 **OpenAI Agents SDK** | Multi-agent AI orchestration and consulting workflow |
| 📊 **Pandas** | Business data processing and analysis |
| 📄 **ReportLab** | PDF report generation |
| ⚡ **Asyncio** | Asynchronous execution of AI agents |
| 📁 **CSV / Excel** | Business data input formats |

---
# 📂 Reposistory Content

```text
AI-Management-Consultant/
│
├── README.md
├── app.py
├── main.py
├── agents_setup.py
├── tools.py
├── requirement.txt
├── .gitignore
│
├── architecture_diagram.jpeg
│
├── screenshots/
│   ├── main dashboard.jpeg
│   ├── business_data.jpeg
│   ├── kpi_dashboard.jpeg
│   ├── business_insights.jpeg
│   ├── business_input.jpeg
│   ├── executive_report.jpeg
│   ├── risk_assessment.jpeg
│   ├── trend_analysis.jpeg
│   ├── business_segmentation.jpeg
│   ├── action_plan.jpeg
│   ├── decision_scorecard.jpeg
│   ├── key_decision.jpeg
│   ├── pdf_report.png
│   └── ai_agents.jpeg
│
├── demo/
│   └── demo-video-link.txt
│
├── PROJECT_DOCUMENTATION.md
│
└── AI_Management_Consultant.pptx
```
---

# ⚙️ Installation & Setup

Follow these steps to install and run the AI Management Consultant locally.

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Management-Consultant
```

## 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

## 3. Install Dependencies

Install the required Python packages using:

```bash
pip install -r requirement.txt
```

## 4. Configure the API Key

Create a `.env` file in the project directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

## 5. Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

## 6. How to Use the Application

1. Upload your business data in **CSV or Excel** format.
2. Review the **Data Preview** and **Dataset Summary**.
3. Review the **KPI Dashboard** and KPI visualisations.
4. Check the **Automatic Business Insights**.
5. Review **Data Quality, Anomaly, Trend, and Segment Analysis**.
6. Ask questions about your uploaded business data using **AI Business Data Chat**.
7. Use **Advanced Business Comparison** to compare business metrics.
8. Enter the main **Business Problem**.
9. Run the **AI Consulting Team**.
10. Review the generated **Business Analysis, Market Research, Competitor Benchmarking, Financial Analysis, and Strategy Recommendations**.
11. Review the **AI Risk Assessment**.
12. Review the **AI Action Plan**.
13. Review the **Executive Decision Scorecard**.
14. Review the **Executive Consultant Report**.
15. Generate and download the final **PDF Report**.

---

# 📊 Project Outcomes

The completed AI Management Consultant demonstrates:

- 🤖 Multi-agent AI architecture
- 🧠 Specialised AI agent roles
- 📊 Business data analysis
- 📈 KPI analysis and visualisation
- 💡 AI-powered business insights
- 🔎 Data quality and anomaly detection
- 📈 Business trend analysis
- 🧩 Segment analysis
- 💬 AI-powered business data chat
- 🏆 Competitor benchmarking
- 💰 Financial analysis
- 🎯 Strategic recommendations
- ⚠️ Risk assessment
- 📋 Executive decision support
- 🎯 Automated action planning
- 📄 Executive consulting report generation
- 📥 PDF report generation
- 🎨 Interactive Streamlit user interface

---

# 🖥️ Screenshots

The following screenshots showcase the major features and key stages of the AI Management Consultant application demonstrated in the project demo.

- 🏠 **Application Dashboard**
- 📊 **Business Data Upload & Analysis**
- 📈 **KPI Dashboard & Visualisation**
- 💡 **Automatic Business Insights**
- 🔎 **Data Quality & Anomaly Detection**
- 📈 **Business Trend & Segment Analysis**
- 💬 **AI Business Data Chat**
- 📊 **Advanced Business Comparison**
- 🤖 **Multi-Agent Consulting Analysis**
- 🌐 **Market Research**
- 🏆 **Competitor Benchmarking**
- 💰 **Financial Analysis**
- 🎯 **Strategic Recommendations**
- ⚠️ **AI Risk Assessment**
- 📋 **AI Action Plan**
- 📊 **Executive Decision Scorecard**
- 📄 **Executive Consultant Report**
- 📥 **PDF Report Generation**

These screenshots provide a visual overview of the application's complete workflow and major outputs.

---

# 🔐 Security

The application uses an API key to communicate with the AI service.

For security:

- Store the API key in a local `.env` file.
- Never upload `.env` to GitHub.
- Never expose API keys in screenshots, presentations, or demo videos.
- Keep `.venv/` and other local environment files out of version control.
- Do not hard-code API keys directly into Python source files.

The repository uses `.gitignore` to prevent sensitive files such as `.env` from being uploaded.

---

# 🎓 Project Context

The **AI Management Consultant** is a multi-agent AI project designed to support business analysis, market research, competitor benchmarking, financial analysis, strategic recommendations, risk assessment, and executive decision-making.

The project demonstrates how specialised AI agents can collaborate to analyse a complex business problem and generate structured, actionable consulting insights.

---

# 🏁 Conclusion

The AI Management Consultant provides an AI-powered approach to business consulting by combining business data analysis with specialised AI agents.

The system brings together multiple areas of analysis and transforms them into practical recommendations, risk insights, action plans, and an executive-level consulting report.

---

# 👩‍💻 Author

**Nancy Choudhary**

AI Management Consultant  
Multi-Agent Business Intelligence & Strategy Platform

---
