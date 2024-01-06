# AI Financial Analyst Assistant

### "AI Financial-Analyst" is a project that uses OpenAI's Assistants API, parallel function calling, and a code interpreter to assist end users with financial analysis. The project utilizes REST APIs to retrieve financial data, and a Streamlit web application provides an interactive user interface.


## Features
 1. AI-Driven Financial Analysis: Utilizes OpenAI's Assistants API to analyze financial data.
 2. Streamlit Web Application: An interactive web interface for easy access and use.
 3. Dynamic Data Retrieval: Fetches financial information from various REST APIs.

## Assistant Functions
 - get_income_statement: Retrieves the income statement data. This function likely fetches detailed revenue, expense, and 
   profit information for a specified entity over a given period.

 - get_balance_sheet: Obtains the balance sheet data. This would include assets, liabilities, and shareholder equity 
   details, providing a snapshot of an entity's financial condition at a specific point in time.

 - get_cash_flow_statement: Gathers cash flow statement data. It probably details the cash inflows and outflows from      
   operating, investing, and financing activities, offering insights into how an entity generates and uses cash.

 - get_key_metrics: Retrieves key financial metrics. This function likely provides important financial indicators that 
   help in assessing a company's financial health, such as EBITDA, return on equity, debt to equity ratio, etc.

 - get_financial_ratios: Fetches various financial ratios. These ratios, such as the price-to-earnings ratio, current 
   ratio, or liquidity ratio, are crucial for financial analysis and comparative assessments.

 - get_financial_growth: Accesses financial growth data. This function probably tracks the growth trends in various 
   financial aspects like revenue growth, profit growth, etc., over time, indicating the entity's growth trajectory.
   
## Getting Started

To get started with this project, you need to have Python installed on your system. After cloning the repository, install the necessary Python packages using the following command:

Installation Procedure
Follow the steps below to install and run the application:
1. Clone the repository using the command:
    ```
    git clone https://github.com/HamzaAhmedSheikh/ai-financial-analyst-assistant.git
    ```
2. Install the necessary packages by executing:
    ```
    pip install -r requirements.txt
    ```
3. Create a .env file in the root directory of the project and add your OpenAI API key and [Financial Modeling Prep API](https://site.financialmodelingprep.com/developer/docs?ref=mlq.ai). 
   ```
    OPENAI_API_KEY=your_openai_api_key
    FMP_API_KEY=your_financial_modeling_prep_api_key
   ```  

4. Launch the Streamlit application with the command:
    ```
    streamlit run st_app.py
    ```
## Contributing

We welcome contributions to the AI Financial Analyst Assistant project! If you would like to contribute, please submit a pull request with your proposed changes.
   
## Resources
- [OpenAI API Documentation](https://platform.openai.com/docs/introduction)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Financial Modeling Prep API Documentation](https://site.financialmodelingprep.com/developer/docs)
