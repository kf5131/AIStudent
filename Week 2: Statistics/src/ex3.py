import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the data
data = pd.read_csv('data/car_data.csv')

# Display the first few rows of the data
print(data.head())

# Calculate the correlation coefficient
correlation = data['Price'].corr(data['Mileage'])
print(f"Correlation Coefficient: {correlation}")

# Build a simple linear regression model
X = data['Mileage'].values.reshape(-1, 1)
y = data['Price'].values

###################################
# Build the regression model here #
###################################

model = LinearRegression()
model.fit(X, y)
predicted_prices = model.predict(X)

###################################
# Evaluate the model here         #
###################################

mse = mean_squared_error(y, predicted_prices)

# Plot the data and the regression line
plt.scatter(X, y, color='blue', label='Actual Prices')
plt.plot(X, predicted_prices, color='red', label='Predicted Prices')
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.title("Car Price Prediction")
plt.legend()
plt.show()