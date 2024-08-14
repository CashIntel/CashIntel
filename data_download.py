import yfinance as yf
import pandas as pd
from datetime import datetime

# Prompt user for stock ticker
ticker = input("Enter the stock ticker symbol (e.g., AAPL for Apple): ")

# Download historical stock data
end_date = datetime.now().strftime('%Y-%m-%d')
data = yf.download(ticker, start='2010-01-01', end=end_date)

# Save the data to a CSV file
data.to_csv(f'{ticker}_historical_data.csv')

print(f"Data downloaded and saved to {ticker}_historical_data.csv.")
