# About the Finance Advisor AI tool  
This tool combines Google Gemini AI and YFinance (formerly Yahoo Finance) to analyse stock investment risks.  
  
### How to set it up
python -m venv .venv  
.venv\Scripts\activate.bat  
adk create --type=config finance  
pip install yfinance, google-adk  
  
### How to test the YFinance API only  
python test_finance_api.py  
  
### How to test the AI  
adk web finance  
  
  
