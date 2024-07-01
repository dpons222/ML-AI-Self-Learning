import numpy as np
from scipy import stats

# Sample data
data = [2, 4, 4, 4, 5, 5, 7, 9]

# Mean
mean = np.mean(data)
print(f'Mean: {mean}')

# Median
median = np.median(data)
print(f'Median: {median}')

# Mode
mode_result = stats.mode(data, keepdims=False)
print(f'Mode: {mode_result.mode}, Count: {mode_result.count}')

# Standard Deviation
std_dev = np.std(data)
print(f'Standard Deviation: {std_dev}')

# Correlation
data2 = [10, 20, 20, 40, 50, 50, 70, 90]
correlation = np.corrcoef(data, data2)
print(f'Correlation matrix:\n {correlation}')
