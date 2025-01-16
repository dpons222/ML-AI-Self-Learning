import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.linear_model import LogisticRegression  # For linear regression
from sklearn.preprocessing import StandardScaler  # For standardizing features
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.datasets import make_classification

my_list = [3,5,8,10,15]

for i in my_list: 
    print(i)