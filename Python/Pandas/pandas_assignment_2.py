import pandas as pd
import numpy as np

# Sample data
data = {
    'Date': pd.date_range('2023-01-01', periods=10),
    'Store': np.random.randint(1, 3, size=10),
    'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Quantity': np.random.randint(1, 10, size=10),
    'Price': np.random.uniform(10, 30, size=10)
}

df = pd.DataFrame(data)
