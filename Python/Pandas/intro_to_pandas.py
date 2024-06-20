import pandas as pd
import numpy as np


portfolio_df = pd.DataFrame({'Company':['Apple', 'Tesla', 'Google'],
                             'Symbol':['AAPL','TSLA','GOOG'],
                             'Price $': [214.29, 184.86, 176.45],
                             'Shares' : [300, 10, 2]})

total_per_share = portfolio_df['Price $'] * portfolio_df['Shares']
total_sum = total_per_share.sum()

print('Total value per share \n', total_per_share.round(2), 'Total value of portfolio: \n', total_sum)