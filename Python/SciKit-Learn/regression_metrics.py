from sklearn.metrics import mean_squared_error
import numpy as np

# Example true and predicted values
# y_true contains the actual values of the target variable
# y_pred contains the predicted values by the model
y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

# Calculate Mean Squared Error (MSE)
# mean_squared_error calculates the average of the squares of the differences between actual and predicted values
mse = mean_squared_error(y_true, y_pred)

# Calculate Root Mean Squared Error (RMSE)
# RMSE is the square root of MSE, which gives the error in the same units as the target variable
rmse = np.sqrt(mse)

# Print the calculated metrics
print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')
