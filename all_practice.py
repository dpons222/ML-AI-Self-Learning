import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

TP = 23
TN = 36
FP = 5
FN = 4

accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)

print('Accuracy: ', accuracy)
print('Precision: ', precision)   
print('Recall: ', recall)