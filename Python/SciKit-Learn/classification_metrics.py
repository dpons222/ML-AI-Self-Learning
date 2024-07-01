from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Example true and predicted labels
# y_true contains the actual labels of the samples
# y_pred contains the predicted labels by the model
y_true = [0, 1, 1, 1, 0, 1, 0, 0, 1, 1]
y_pred = [0, 0, 1, 1, 0, 1, 0, 0, 0, 1]

# Calculate accuracy
# accuracy_score calculates the ratio of correctly predicted labels to the total labels
accuracy = accuracy_score(y_true, y_pred)

# Calculate precision
# precision_score calculates the ratio of true positives to the total predicted positives
precision = precision_score(y_true, y_pred)

# Calculate recall
# recall_score calculates the ratio of true positives to the total actual positives
recall = recall_score(y_true, y_pred)

# Calculate F1 score
# f1_score calculates the harmonic mean of precision and recall
f1 = f1_score(y_true, y_pred)

# Print the calculated metrics
print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
