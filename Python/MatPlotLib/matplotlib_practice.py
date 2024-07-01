import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

# Create a simple plot to test
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'sales_data_3.csv')

data = pd.read_csv(file_path, header=0)


# Plot a line chart
plt.plot(data['Quantity'], data['Price'])
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.title('Line Chart')
plt.show()

# Plot a histogram
plt.hist(data['column1'], bins=30)
plt.xlabel('Column 1')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
