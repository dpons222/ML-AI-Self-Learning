from sklearn.metrics import mean_squared_error
import numpy as np

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([2, 3, 5, 4, 6])

# Create and fit the model
model = LinearRegression()
model.fit(X, Y)

# Get the slope and intercept
m = model.coef_[0]
b = model.intercept_

print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Plot the data and the regression line
plt.scatter(X, Y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel('Size')
plt.ylabel('Price')
plt.title('Linear Regression')
plt.show()
