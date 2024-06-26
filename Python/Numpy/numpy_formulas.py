import numpy as np

def reshape_data(array, shape):
    return array.reshape(shape)

def add_five(array):
    return array + 5

def apply_discount(prices_array):
    # Ensure the array is of type float
    if prices_array.dtype != np.float64:
        prices_array = prices_array.astype(float)
    prices_array[0, :] *= 0.90
    return prices_array

def total_sales(quantities, prices):
    return quantities * prices.astype(np.int64)

def quantities_stats(quantities):
    return quantities.sum(), quantities.mean()

def dot_product(quantities, prices):
    return np.dot(quantities, prices.T)
