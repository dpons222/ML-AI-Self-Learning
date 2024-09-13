# %% [markdown]
# # Data Visualization with Matplotlib and Seaborn

# %% [markdown]
# ## Introduction

# %% [markdown]
# Data visualization is a crucial step in the data analysis process. It helps in understanding the data better, identifying patterns, and communicating insights effectively. In this notebook, we will cover various techniques for visualizing data using Matplotlib and Seaborn.

# %% [markdown]
# ## Importing Libraries

# %% 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the random seed for reproducibility
np.random.seed(42)

# %% [markdown]
# ## Creating a Sample DataFrame

# %% 
# Create a sample DataFrame with more realistic data
np.random.seed(42)
n = 100  # Number of samples

# Generate years of experience
years_of_experience = np.random.randint(1, 31, size=n)

# Generate salary based on years of experience with some random noise
base_salary = 30000 + years_of_experience * 2000
salary = base_salary + np.random.randint(-5000, 5000, size=n)

# Create the DataFrame
data = {
    'age': np.random.randint(18, 70, size=n),
    'salary': salary,
    'department': np.random.choice(['Sales', 'Engineering', 'HR', 'Marketing'], size=n),
    'gender': np.random.choice(['Male', 'Female'], size=n),
    'years_of_experience': years_of_experience
}

df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
df.head()

# %% [markdown]
# ## Matplotlib

# %% [markdown]
# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

# %% [markdown]
# ### Line Plot

# %% 
# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(df['years_of_experience'], df['salary'], marker='o', linestyle='-', color='b')
plt.title('Line Plot of Years of Experience vs Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# %% [markdown]
# ### Bar Plot

# %% 
# Create a bar plot
department_counts = df['department'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(department_counts.index, department_counts.values, color='skyblue')
plt.title('Bar Plot of Department Counts')
plt.xlabel('Department')
plt.ylabel('Count')
plt.show()

# %% [markdown]
# ### Histogram

# %% 
# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(df['salary'], bins=20, color='green', edgecolor='black')
plt.title('Histogram of Salaries')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# %% [markdown]
# ### Scatter Plot

# %% 
# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['years_of_experience'], df['salary'], alpha=0.7, edgecolors='w', linewidth=0.5)
plt.title('Scatter Plot of Years of Experience vs Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# %% [markdown]
# ### Box Plot

# %% 
# Create a box plot
plt.figure(figsize=(10, 6))
plt.boxplot([df[df['gender'] == 'Male']['salary'], df[df['gender'] == 'Female']['salary']], labels=['Male', 'Female'])
plt.title('Box Plot of Salaries by Gender')
plt.xlabel('Gender')
plt.ylabel('Salary')
plt.show()

# %% [markdown]
# ## Seaborn

# %% [markdown]
# Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

# %% [markdown]
# ### Distribution Plot

# %% 
# Create a distribution plot
plt.figure(figsize=(10, 6))
sns.histplot(df['salary'], kde=True, color='purple')
plt.title('Distribution Plot of Salaries')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# %% [markdown]
# ### Count Plot

# %% 
# Create a count plot
plt.figure(figsize=(10, 6))
sns.countplot(x='department', data=df, palette='viridis')
plt.title('Count Plot of Departments')
plt.xlabel('Department')
plt.ylabel('Count')
plt.show()

# %% [markdown]
# ### Scatter Plot with Regression Line

# %% 
# Create a scatter plot with regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='years_of_experience', y='salary', data=df, scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title('Scatter Plot of Years of Experience vs Salary with Regression Line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# %% [markdown]
# ### Pair Plot

# %% 
# Create a pair plot
plt.figure(figsize=(12, 10))
sns.pairplot(df, hue='department', palette='bright')
plt.suptitle('Pair Plot of the DataFrame', y=1.02)
plt.show()

# %% [markdown]
# ### Heatmap

# %% 
# Create a heatmap
corr_matrix = df.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

# %% [markdown]
# ## Summary

# %% [markdown]
# In this notebook, we covered various techniques for data visualization using Matplotlib and Seaborn. These visualizations help in understanding the data better, identifying patterns, and communicating insights effectively. By mastering these techniques, you can create powerful and informative visualizations for your data analysis projects.
