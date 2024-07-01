import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
titanic = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Load / Inspect Data

print(titanic.head())
# Check the shape of the dataset
print(titanic.shape)

# Get a summary of the dataset
print(titanic.info())

# Get basic statistical details
print(titanic.describe())

# Check for missing values
print(titanic.isnull().sum())



# Fill missing values in the 'Age' column with the mean age
titanic['Age'].fillna(titanic['Age'].mean(), inplace=True)

# Drop rows with missing values in the 'Embarked' column
titanic.dropna(subset=['Embarked'], inplace=True)
print('\n Data after dropping nulls: \n',titanic.head())



import matplotlib.pyplot as plt
import seaborn as sns

# Plot the distribution of ages
plt.hist(titanic['Age'], bins=30)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()

# Plot a bar chart of survival counts
sns.countplot(x='Survived', data=titanic)
plt.title('Survival Counts')
plt.show()

# Plot a box plot of age by class
sns.boxplot(x='Pclass', y='Age', data=titanic)
plt.title('Age by Class')
plt.show()

# Plot a heatmap of the correlation matrix
sns.heatmap(titanic.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


