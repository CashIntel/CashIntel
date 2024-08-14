import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Prompt user for stock ticker
ticker = input("Enter the stock ticker symbol (e.g., AAPL for Apple): ")

# Load the cleaned dataset
df = pd.read_csv(f'{ticker}_cleaned_data.csv', index_col='Date', parse_dates=True)

# Plot historical closing prices
plt.figure(figsize=(10, 6))
plt.plot(df['Close'], label='Close Price')
plt.plot(df['Moving_Average_50'], label='50-Day Moving Average')
plt.plot(df['Moving_Average_200'], label='200-Day Moving Average')
plt.title(f'{ticker} Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.savefig(f'{ticker}_closing_prices.png')
plt.show()

# Plot daily returns
plt.figure(figsize=(10, 6))
sns.histplot(df['Daily_Return'], bins=50, kde=True)
plt.title(f'{ticker} Daily Returns')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.savefig(f'{ticker}_daily_returns.png')
plt.show()
