import json
import requests
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import streamlit as st

_: bool = load_dotenv(find_dotenv())

INSTRUCTIONS = "Act as a financial analyst by accessing detailed financial data through the Financial Modeling Prep API. Your capabilities include analyzing key metrics, comprehensive financial statements, vital financial ratios, and tracking financial growth trends."

FMP_API_KEY = os.environ.get("FMP_API_KEY")

# Defining Functions to Get Data from REST APIs
# We are not using ~ period and limit parameters as the API Requires a Premium Account for these parameters


def get_income_statement(ticker: str) -> str:
    url = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?period=annual&apikey={FMP_API_KEY}"
    response = requests.get(url)
    return json.dumps(response.json())


def get_balance_sheet(ticker: str) -> str:
    url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?period=annual&apikey={FMP_API_KEY}"
    response = requests.get(url)
    return json.dumps(response.json())


def get_cash_flow_statement(ticker: str) -> str:
    url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?period=annual&apikey=ETZqiw9M5ObXGLxKylHzoI5Ec70NQFue"
    response = requests.get(url)
    return json.dumps(response.json())


def get_key_metrics(ticker: str) -> str:
    url = f"https://financialmodelingprep.com/api/v3/key-metrics/{ticker}?period=annual&apikey={FMP_API_KEY}"
    response = requests.get(url)
    return json.dumps(response.json())


def get_financial_ratios(ticker: str) -> str:
    url = f"https://financialmodelingprep.com/api/v3/ratios-ttm/{ticker}?period=annual&apikey={FMP_API_KEY}"
    response = requests.get(url)
    return json.dumps(response.json())


def get_financial_growth(ticker: str) -> str:
    url = f"https://financialmodelingprep.com/api/v3/financial-growth/{ticker}?period=annual&apikey={FMP_API_KEY}"
    response = requests.get(url)
    return json.dumps(response.json())


# available functions for mapping
available_functions = {
    "get_income_statement": get_income_statement,
    "get_balance_sheet": get_balance_sheet,
    "get_cash_flow_statement": get_cash_flow_statement,
    "get_key_metrics": get_key_metrics,
    "get_financial_ratios": get_financial_ratios,
    "get_financial_growth": get_financial_growth
}


financial_tools_functions = [
    {"type": "code_interpreter"},
    {
        "type": "function",
        "function": {
            "name": "get_income_statement",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {"type": "string"},
                },
                "required": ["ticker"],
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_balance_sheet",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {"type": "string"},
                },
                "required": ["ticker"],
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_cash_flow_statement",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {"type": "string"},
                },
                "required": ["ticker"],
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_key_metrics",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {"type": "string"},
                },
                "required": ["ticker"],
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_financial_ratios",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {"type": "string"},
                },
                "required": ["ticker"],
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_financial_growth",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {"type": "string"},
                },
                "required": ["ticker"],
            }
        }
    }
]
