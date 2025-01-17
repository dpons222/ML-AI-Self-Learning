import numpy as np
import pandas as pd
# import scipy.stats as stats
# import matplotlib.pyplot as plt

# from sklearn.model_selection import train_test_split  # For splitting data
# from sklearn.linear_model import LogisticRegression  # For linear regression
# from sklearn.preprocessing import StandardScaler  # For standardizing features
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
# from sklearn.datasets import make_classification


for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    elif i % 5 == 0:
        print(i, "Buzz")
    else:
        print(i)