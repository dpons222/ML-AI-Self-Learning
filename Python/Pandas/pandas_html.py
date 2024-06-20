import pandas as pd
'''
read html 
'''
house_price_df = pd.read_html('https://www.livingin-canada.com/house-prices-canada.html')
print(house_price_df[0])