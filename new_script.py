import numpy as np

import pandas as pd

pd.set_option('display.max_columns', None)

import scipy.stats as stats

import matplotlib.pyplot as plt

import seaborn as sns

from scipy.stats import chi2_contingency,ttest_1samp

import unittest





from sklearn.datasets import load_iris

from sklearn.pipeline import Pipeline



from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder

from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif

from sklearn.impute import SimpleImputer



from sklearn.model_selection import train_test_split, GridSearchCV

from sklearn.decomposition import PCA

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.linear_model import LogisticRegression, LinearRegression, SGDClassifier

# from sklearn.linear_model import Lasso, Ridge  # For regularized regression

# from sklearn.tree import DecisionTreeClassifier

# from sklearn.cluster import KMeans

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, AdaBoostClassifier



# #metrics

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report, roc_curve, roc_auc_score, mean_squared_error

# from sklearn.datasets import make_classification


X, y = load_iris(return_X_y=True)

X.shape






rng = np.random.RandomState(0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20, random_state=rng)

X_train.shape

X_train

pipe = Pipeline([ 

('scaler', MinMaxScaler()),

('clf', SGDClassifier())

])



pipe.fit(X_train, y_train)

X_train