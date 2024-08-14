import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Prompt user for stock ticker
ticker = input("Enter the stock ticker symbol (e.g., TSLA for Tesla): ")

# Load the cleaned dataset
df = pd.read_csv(f'{ticker}_cleaned_data.csv', index_col='Date', parse_dates=True)

# Use all available data to ensure the correct range of prices
X = df[['Moving_Average_50', 'Moving_Average_200', 'Daily_Return', 'RSI', 'MACD', 'Signal_Line', 'Upper_Band', 'Lower_Band']]
y = df['Close']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict the stock prices
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Sort the data by index for correct plotting
y_test_sorted = y_test.sort_index()
y_pred_sorted = pd.Series(y_pred, index=y_test.index).sort_index()

# Plot actual vs predicted stock prices
plt.figure(figsize=(10, 6))
plt.plot(y_test_sorted.index, y_test_sorted, label='Actual Prices')
plt.plot(y_pred_sorted.index, y_pred_sorted, label='Predicted Prices')
plt.title(f'{ticker} Actual vs Predicted Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Add date formatting to the x-axis
date_form = DateFormatter("%Y-%m-%d")
plt.gca().xaxis.set_major_formatter(date_form)

# Adjust the y-axis limit to fit the data
plt.ylim(min(y_test_sorted.min(), y_pred_sorted.min()), max(y_test_sorted.max(), y_pred_sorted.max()))

plt.savefig(f'{ticker}_actual_vs_predicted.png')
plt.show()
