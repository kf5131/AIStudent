# /// script
# dependencies = [
#   "numpy==1.26.4",
#   "matplotlib==3.8.2",
#   "scikit-learn==1.6.1",
#   "statsmodels==0.14.4"
# ]
# ///



import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm

# Sample data: square footage and corresponding house prices
square_footage = np.array([1500, 1800, 2400, 3000, 3500, 4000]).reshape(-1, 1)
house_prices = np.array([300000, 360000, 480000, 600000, 700000, 800000])

# Fit a simple linear regression model
model = LinearRegression()
model.fit(square_footage, house_prices)

# Predict prices
predicted_prices = model.predict(square_footage)

# Evaluate the model
mse = mean_squared_error(house_prices, predicted_prices)
print(f"Mean Squared Error: {mse}")
print(f"Model Coefficients: {model.coef_}")
print(f"Model Intercept: {model.intercept_}")

# Plot actual vs predicted prices
plt.scatter(square_footage, house_prices, color='blue', label='Actual Prices')
plt.plot(square_footage, predicted_prices, color='red', label='Predicted Prices')
plt.xlabel("Square Footage")
plt.ylabel("House Prices")
plt.title("House Price Prediction")
plt.legend()
plt.show()

# Check residuals for homoscedasticity using statsmodels
X = sm.add_constant(square_footage)  # Add constant for intercept
ols_model = sm.OLS(house_prices, X).fit()
print(ols_model.summary())