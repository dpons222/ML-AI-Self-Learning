import numpy as np
import pandas as pd
import scipy.stats as stats

results = 0
for i in range(0, 5):
    results += ((-1)**i) / (1+i)
    print(f'iteration {i}: {results}')
print(f'total results: {results}')  

print(47/60)