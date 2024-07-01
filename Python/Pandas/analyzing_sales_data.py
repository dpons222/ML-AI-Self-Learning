import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'sales_data_3.csv')


#load the data
df = pd.read_csv(file_path, header=0)
print('\nDataframe info: \n', df.info())
print('\nOriginal Data Head: ')
print(df.head(3))
print('\n Dataframe shape: \n', df.shape)
print('\nDataframe describe: \n', df.describe())

#clean the data / check nulls
print('\nCheck for null data: ')
print(df.isnull().sum())
df.dropna(axis=1, how='all', inplace=True)
print("\nData after dropping rows with null values:")
print(df.head(3))

#Check Data types and clean (datetime)
print('\nCheck orginal data types: ')
print(df.dtypes)
df['Date'] = pd.to_datetime(df['Date'])
print('\nCheck cleaned data types')
print(df.dtypes)

#add new Total Sales Column
total_sales = df['Quantity'] * df['Price']
df['Total Sales'] = total_sales
print('\n Table with Total Sales added:')
print(df)

#calculate total quantity sold for each product
total_quantity_sold_per_product = df.groupby('Product')['Quantity'].sum()
print('\nTotal Quantity sold per product: ')
print(total_quantity_sold_per_product)

#calculate total sales dollars for each product
total_sales_dollars_per_product = df.groupby('Product')['Price'].sum()
print('\nTotal Sales Dollars per product: ')
print(total_sales_dollars_per_product)

#calculate average sales per transaction 
average_sales_per_transaction = df.groupby('Store')['Price'].mean()
print('\nAverage price per transaction')
print(average_sales_per_transaction)
