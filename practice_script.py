import numpy as np
import pandas as pd
import seaborn as sns

import unittest


# import tensorflow as tf
# import matplotlib.pyplot as plt
# import random
# # import scipy.stats as stats
# # import matplotlib.pyplot as plt

# # from sklearn.model_selection import train_test_split  # For splitting data
# # from sklearn.linear_model import LogisticRegression  # For linear regression
# # from sklearn.preprocessing import StandardScaler  # For standardizing features
# # from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
# # from sklearn.datasets import make_classification


# Function that gets tested
def times_ten(number):
    return number * 10

# Test class
class TestTimesTen(unittest.TestCase):
    def test_times_ten(self):
        for num in [0, 1000000, -100]:
            with self.subTest():
                expected_result = num * 10
                message = 'Expected times_ten(' + str(num) + ') to return ' + str(expected_result)
                self.assertEqual(times_ten(num), expected_result, message)

unittest.main()