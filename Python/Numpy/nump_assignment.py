import numpy as np

# Sample data
quantities = np.array([10, 5, 7, 8, 9, 3, 6, 11, 15, 8])
prices = np.array([20, 15, 20, 10, 25, 30, 18, 20, 19, 12])
discounts = np.array([2, 1, 0, 2, 3, 5, 1, 0, 2, 1])


#reshape to 2 by 5 
quantities_reshaped = quantities.reshape(2,5)
prices_reshaped = prices.reshape(2,5)
discounts_reshaped = discounts.reshape(2,5)
print('\nData reshaped to 2 by 5: ')
print(quantities_reshaped)
print(prices_reshaped)
print(discounts_reshaped)

#add 5 to the arrays
quantities_reshaped_plus_5 = quantities_reshaped + 5
prices_reshaped_plus_5 = prices_reshaped + 5
discounts_reshaped_plus_5 = discounts_reshaped + 5
print('\nArrays plus 5: ')
print(quantities_reshaped_plus_5)
print(prices_reshaped_plus_5)
print(discounts_reshaped_plus_5)

#10% discount to the first 5 elements of prices
prices_reshaped_plus_5_discounted_10 = prices_reshaped_plus_5.copy()
prices_reshaped_plus_5_discounted_10[0, :] *= 0.90
print('\n 10% discount on first 5 prices: ')
print(prices_reshaped_plus_5_discounted_10)

#Mathematical Functions

#total sales for each quantity and price pair
total_sales = quantities_reshaped_plus_5 * prices_reshaped_plus_5_discounted_10.astype(np.int64)  # Convert discounted prices to int64
print('\nTotal sales: ')
print(total_sales)

#sum, mean, and dot product of quantities
quantities_sum = quantities_reshaped_plus_5.sum()
quantities_mean = quantities_reshaped_plus_5.mean()
dot_product_quantities_prices = np.dot(quantities_reshaped_plus_5, prices_reshaped_plus_5_discounted_10)
print('\nQuanities sum: ')
print(quantities_sum)
print('\nQuantities mean: ')
print(quantities_mean)
print('\nDot product prices and quantities: ')
print(dot_product_quantities_prices)
