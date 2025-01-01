import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

# Sample data
X = [1], [2], [3], [4], [5]  # Predictor variable
y = [1,5,10,15,20]            # Response variable

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Get the coefficient and intercept
coef = model.coef_
intercept = model.intercept_

print(f"Coefficient: {coef}")
print(f"Intercept: {intercept}")

plt.scatter(model.predict(X), y)
plt.show()
