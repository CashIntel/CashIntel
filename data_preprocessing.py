import pandas as pd

# Function to calculate RSI
def calculate_rsi(df, window=14):
    delta = df['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Function to calculate MACD
def calculate_macd(df, short_window=12, long_window=26, signal_window=9):
    short_ema = df['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = df['Close'].ewm(span=long_window, adjust=False).mean()
    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal_window, adjust=False).mean()
    return macd, signal_line

# Function to calculate Bollinger Bands
def calculate_bollinger_bands(df, window=20):
    rolling_mean = df['Close'].rolling(window=window).mean()
    rolling_std = df['Close'].rolling(window=window).std()
    upper_band = rolling_mean + (rolling_std * 2)
    lower_band = rolling_mean - (rolling_std * 2)
    return upper_band, lower_band

# Prompt user for stock ticker
ticker = input("Enter the stock ticker symbol (e.g., AAPL for Apple): ")

# Load the dataset
df = pd.read_csv(f'{ticker}_historical_data.csv', index_col='Date', parse_dates=True)

# Check for missing values
print("Missing values:", df.isnull().sum())

# Drop rows with missing values
df = df.dropna()

# Create new features
df['Moving_Average_50'] = df['Close'].rolling(window=50).mean()
df['Moving_Average_200'] = df['Close'].rolling(window=200).mean()
df['Daily_Return'] = df['Close'].pct_change()
df['RSI'] = calculate_rsi(df)
df['MACD'], df['Signal_Line'] = calculate_macd(df)
df['Upper_Band'], df['Lower_Band'] = calculate_bollinger_bands(df)

# Drop rows with NaN values created by rolling calculations
df = df.dropna()

# Save the cleaned data to a new CSV file
df.to_csv(f'{ticker}_cleaned_data.csv')

print(f"Data cleaned and saved to {ticker}_cleaned_data.csv.")
