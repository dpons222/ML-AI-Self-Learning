import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns


# Create a simple plot to test
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'sales_data_3.csv')

data = pd.read_csv(file_path, header=0)


# Plot a scatter plot
sns.scatterplot(x='column1', y='column2', data=data)
plt.title('Scatter Plot')
plt.show()

# Plot a box plot
sns.boxplot(x='category_column', y='value_column', data=data)
plt.title('Box Plot')
plt.show()

# Plot a heatmap
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap')
plt.show()