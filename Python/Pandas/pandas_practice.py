import pandas as pd
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'census_data.csv')

print('Dataframe Read: \n')
census = pd.read_csv(file_path, index_col=0)


print(census.head())
print(f'census data types:\n\n{census.dtypes}')
