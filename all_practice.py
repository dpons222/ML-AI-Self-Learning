import numpy as np
import pandas as pd
import scipy.stats as stats

array = np.array(range(1, 11))
sample = np.random.choice(array, (10), replace = False,)
print(sample)