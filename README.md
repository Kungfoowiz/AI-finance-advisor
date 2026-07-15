# Setup.
python -m venv .venv
.venv\Scripts\activate.bat
adk create --type=config finance
pip install yfinance, google-adk

# Test Finance API.
python test_finance_api.py

# Test AI.
adk web finance

