import pandas as pd
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'mayor.csv')

print('Dataframe Read: \n')
df = pd.read_csv(file_path)

print(f'''

Dataframe Info:
{df.info()}

Dataframe Head: 
{df.head()}

Dataframe Describe:
{df.describe()}

Dataframe IsNull: 
{df.isnull().sum()}
''')


job_freq = df['title'].value_counts()
job_percent_of_total = job_freq / df['title'].value_counts().sum() *100

job_title_categories = pd.DataFrame(
    {'Frequency' : job_freq,
     'Percentage' : job_percent_of_total}
)

# Format the Percentage column with a percent sign
job_title_categories['Percentage'] = job_title_categories['Percentage'].apply(lambda x: f'{int(x)}%')

print(f'''
Job Title Categories:
       
{job_title_categories}''')

print(f'''
Mean age:
{df['age'].mean()}      

Std Dev:
{df['age'].std()}''')

