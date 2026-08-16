"""
Agent setup module for the AI Management Consultant project.

The main agent definitions are currently maintained in main.py.
This module provides a clean central place to access them.
"""

from main import (
    agent,
    market_researcher,
    benchmarking_agent,
    financial_analyst,
    strategy_advisor,
)

__all__ = [
    "agent",
    "market_researcher",
    "benchmarking_agent",
    "financial_analyst",
    "strategy_advisor",
]