import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# Load the dataset
titanic = pd.read_csv('titanic.csv')

# Split data into those who died and those who survived
Died = titanic[titanic['Survived'] == 0]['Fare']
Survived = titanic[titanic['Survived'] == 1]['Fare']

# Create subplots
fig = plt.figure(figsize=(10, 20))

# Create the box plot
ax1 = fig.add_subplot(2, 1, 1)
sns.boxplot(data=titanic, x='Survived', y='Fare', ax=ax1)

# Create the histograms
ax2 = fig.add_subplot(2, 1, 2)
ax2.hist(Died, color="blue", label="Died", density=True, alpha=0.5, bins=30)
ax2.hist(Survived, color="red", label="Survived", density=True, alpha=0.5, bins=30)
ax2.legend()
ax2.set_xlabel('Fare')
ax2.set_ylabel('Density')

plt.show()
