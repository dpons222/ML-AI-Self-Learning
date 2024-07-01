import numpy as np
from scipy import stats


# Probability of rolling a 3 on a fair 6-sided die
P_3 = 1/6
print(f'Probability of rolling a 3: \n{P_3}')

# Expected value of rolling a fair 6-sided die
die_faces = [1, 2, 3, 4, 5, 6]
probabilities = [1/6] * 6
expected_value = np.dot(die_faces, probabilities)
print(f'Expected value of rolling a die: {expected_value}')

# Variance of rolling a fair 6-sided die
mean = expected_value
variance = np.dot([(x - mean)**2 for x in die_faces], probabilities)
print(f'Variance of rolling a die: {variance}')
