import asyncio
from dotenv import load_dotenv

load_dotenv()

from agents import Agent, Runner, function_tool,WebSearchTool

@function_tool
def calculate_percentage_change(old_value: float, new_value: float) -> str:
    """Calculate the percentage change between an old and a new value."""
    
    if old_value == 0:
        return "Cannot calculate percentage change because the old value is zero."
    
    change = ((new_value - old_value) / old_value) * 100
    
    return f"Percentage change: {change:.2f}%"

@function_tool
def calculate_roi(investment: float, return_amount: float) -> str:
    """Calculate return on investment (ROI) as a percentage."""

    if investment == 0:
        return "Cannot calculate ROI because investment is zero."

    roi = ((return_amount - investment) / investment) * 100

    return f"ROI: {roi:.2f}%"


agent = Agent(
    name="Business Analyst",
    instructions="""
    You are a professional business analyst.
    Analyze the business problem given by the user.
    Identify the main problem, objectives, possible causes,
    stakeholders, and important information needed for analysis.
    """
)
market_researcher = Agent(
    name="Market Research Agent",
    instructions="""
    You are a professional market research analyst.

    Analyze the business problem and identify:
    1. Current market trends
    2. Customer trends
    3. Market opportunities
    4. Market threats
    5. Important competitors or industry factors

    Give your findings in a clear and structured format.
    """,
    tools=[WebSearchTool()]
)
benchmarking_agent = Agent(
    name="Benchmarking Agent",
    instructions="""
    You are a professional competitive benchmarking analyst.

    Analyze the business problem and identify:
    1. Main competitors
    2. Competitor strengths
    3. Competitor weaknesses
    4. Pricing and product differences
    5. Competitive opportunities for the business

    Give your findings in a clear and structured format.
    """
)
financial_analyst = Agent(
    name="Financial Analysis Agent",
    instructions="""
    You are a professional financial analyst.

    Analyze the business problem and identify:
    1. Revenue-related issues
    2. Major cost factors
    3. Profitability concerns
    4. Financial risks
    5. Possible financial improvements
    6. Important financial KPIs

    Give your findings in a clear and structured format.
    """,
    tools=[calculate_percentage_change, calculate_roi]
)
strategy_advisor = Agent(
    name="Strategy Advisor",
    instructions="""
    You are a senior business strategy consultant.

    Based on the business problem, develop practical strategic recommendations.

    Your recommendations should include:
    1. Main strategic priorities
    2. Recommended actions
    3. Short-term actions
    4. Long-term actions
    5. Expected business impact
    6. Potential risks
    7. Key performance indicators (KPIs)

    Provide realistic and actionable recommendations.
    """
)
report_writer = Agent(
    name="Report Writer",
    instructions="""
    You are a professional business consulting report writer.

    Create a clear and professional consulting report based on
    the business analysis, market research, benchmarking,
    financial analysis, and strategy recommendations.

    The report should contain:
    1. Executive Summary
    2. Business Problem
    3. Market Analysis
    4. Competitor Benchmarking
    5. Financial Analysis
    6. Strategic Recommendations
    7. Action Plan
    8. Risks
    9. Key Performance Indicators (KPIs)
    10. Conclusion

    Use clear headings and concise professional language.
    """
)
manager_agent = Agent(
    name="Consulting Manager",
    instructions="""
    You are the lead consulting manager.

    Analyze the user's business problem and delegate the work
    to the appropriate specialist agents.

    Use:
    - Business Analyst for understanding the business problem
    - Market Research Agent for market trends and opportunities
    - Benchmarking Agent for competitor analysis
    - Financial Analysis Agent for financial analysis
    - Strategy Advisor for strategic recommendations
    - Report Writer for the final consulting report

    Coordinate the specialists and ensure the user receives
    a useful consulting response.
    """,
    handoffs=[
        agent,
        market_researcher,
        benchmarking_agent,
        financial_analyst,
        strategy_advisor,
        report_writer
    ]
)



async def main():
    user_problem = input("Enter your business problem: ")

    business_result = await Runner.run(
    agent,
    user_problem
)

    market_result = await Runner.run(
    market_researcher,
    user_problem
)
    benchmark_result = await Runner.run(
    benchmarking_agent, user_problem
)
    financial_result = await Runner.run(
    financial_analyst, user_problem
)
    strategy_result = await Runner.run(
    strategy_advisor, user_problem
)
    report_result = await Runner.run(
    report_writer, user_problem
)

    print("\n===== BUSINESS ANALYSIS =====")
    print(business_result.final_output)

    print("\n===== MARKET RESEARCH =====")
    print(market_result.final_output)

    print("\n===== BENCHMARKING =====")
    print(benchmark_result.final_output)

    print("\n===== FINANCIAL ANALYSIS =====")
    print(financial_result.final_output)

    print("\n===== STRATEGY RECOMMENDATIONS =====")
    print(strategy_result.final_output)

    print("\n===== CONSULTING REPORT =====")
    print(report_result.final_output)

    

if __name__ == "__main__":
    asyncio.run(main())
