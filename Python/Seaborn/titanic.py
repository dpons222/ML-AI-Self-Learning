import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

titanic = pd.read_csv('titanic.csv')

Survived = titanic.Fare[titanic.Survived == 1]
Dies = titanic.Fare[titanic.Survived == 0]

survive_mean = np.mean(Survived)
died_mean = np.mean(Dies)

diff_mean = survive_mean-died_mean

print(diff_mean)

survive_med= np.median(Survived)
died_med = np.median(Dies)

diff_med = survive_med-died_med

print(diff_med)

sns.boxplot(data = titanic, x = 'Survived', y = 'Fare')
plt.show()