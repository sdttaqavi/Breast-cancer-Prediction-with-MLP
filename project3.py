# -*- coding: utf-8 -*-
"""project3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_7fN1TQCR8aq1IyeGjG1Rl-N1y1R4z7e

**Data Preprocessing**
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

!gdown 1X76S-596LOf2wtSy2FVMUEC-9s7zk37o
breast_cancer = pd.read_csv('breast cancer.csv')
breast_cancer

breast_cancer.info()

diagnosis = breast_cancer['diagnosis']
encoder = LabelEncoder()
diagnosis_encoded = encoder.fit_transform(diagnosis)
breast_cancer['diagnosis'] = diagnosis_encoded
breast_cancer

breast_cancer = breast_cancer.drop(['id','Unnamed: 32'], axis=1)

breast_cancer.info()

from scipy.stats import zscore

# Identify and remove outliers using z-score
z_scores = np.abs(zscore(breast_cancer.iloc[:, 2:]))
threshold = 3

# Find outliers
outlier_indices = np.where(z_scores > threshold)

# Remove outliers
breast_cancer = breast_cancer.drop(breast_cancer.index[outlier_indices[0]])

# Reset the index after removing outliers
breast_cancer = breast_cancer.reset_index(drop=True)

breast_cancer.describe()

"""**Correlation Matrix**"""

import matplotlib.pyplot as plt
import seaborn as sns

# Calculate the correlation matrix
correlation_matrix = breast_cancer.iloc[:, 2:].corr()
plt.figure(figsize=(20, 20))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

strong_positive_corr = correlation_matrix[correlation_matrix > 0.7]
strong_negative_corr = correlation_matrix[correlation_matrix < -0.7]

print("Strong Positive Correlations:")
print(strong_positive_corr.stack().drop_duplicates().sort_values(ascending=False))

print("\nStrong Negative Correlations:")
print(strong_negative_corr.stack().drop_duplicates().sort_values(ascending=True))

threshold = 0.5
highly_correlated_features = []
for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        if abs(correlation_matrix.iloc[i, j]) > threshold:
            feature_i = correlation_matrix.columns[i]
            feature_j = correlation_matrix.columns[j]
            highly_correlated_features.append((feature_i, feature_j))

# Extract the selected features
selected_features = set()
for feature_i, feature_j in highly_correlated_features:
    selected_features.add(feature_i)
    selected_features.add(feature_j)

selected_data = breast_cancer[list(selected_features) + ['diagnosis']]
selected_data.info()

"""**Build the MLP model**"""

import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

values = selected_data.drop(labels='diagnosis',axis=1)
target = selected_data.diagnosis

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(values, target, test_size=0.2)

# Perform feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build the MLP model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model with validation split
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1, validation_split=0.2)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test)
print("Test Loss:", loss)
print("Test Accuracy:", accuracy)

"""**Evaluate the accuracy of each model**"""

# Build the MLP model
model_lr_1 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
learning_rate_1 = 0.001
optimizer_1 = tf.keras.optimizers.Adam(learning_rate=learning_rate_1)
model_lr_1.compile(optimizer=optimizer_1, loss='binary_crossentropy', metrics=['accuracy'])

# Train the model with validation split
model_lr_1.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1, validation_split=0.2)

# Evaluate the model on the test set
loss_1, accuracy_1 = model_lr_1.evaluate(X_test, y_test)
print("Test Loss:", loss_1)
print("Test Accuracy:", accuracy_1)

# Build the MLP model
model_lr_2 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
learning_rate_2 = 0.001
optimizer_2 = tf.keras.optimizers.Adam(learning_rate=learning_rate_2)
model_lr_2.compile(optimizer=optimizer_2, loss='binary_crossentropy', metrics=['accuracy'])

# Train the model with validation split
model_lr_2.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1, validation_split=0.2)

# Evaluate the model on the test set
loss_2, accuracy_2 = model_lr_2.evaluate(X_test, y_test)
print("Test Loss:", loss_2)
print("Test Accuracy:", accuracy_2)

# Build the MLP model
modelـepochs_1 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
modelـepochs_1.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model with validation split
modelـepochs_1.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1, validation_split=0.2)

# Evaluate the model on the test set
loss_3, accuracy_3 = modelـepochs_1.evaluate(X_test, y_test)
print("Test Loss:", loss_3)
print("Test Accuracy:", accuracy_3)

# Build the MLP model
modelـepochs_2 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
modelـepochs_2.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model with validation split
modelـepochs_2.fit(X_train, y_train, epochs=20, batch_size=32, verbose=1, validation_split=0.2)

# Evaluate the model on the test set
loss_4, accuracy_4 = modelـepochs_2.evaluate(X_test, y_test)
print("Test Loss:", loss_4)
print("Test Accuracy:", accuracy_4)

# Print the accuracy of each model
print("Model 1 Accuracy:", accuracy_1 , "Model 1 Loss:", loss_1)
print("Model 2 Accuracy:", accuracy_2 , "Model 2 Loss:", loss_2)
print("Model 3 Accuracy:", accuracy_3 , "Model 3 Loss:", loss_3)
print("Model 4 Accuracy:", accuracy_4 , "Model 4 Loss:", loss_4)

"""**Confusion Matrix**"""

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

y_pred_prob = model_lr_2.predict(X_test)
threshold = 0.5
y_pred = np.where(y_pred_prob >= threshold, 1, 0)

# Compute confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plot the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print()
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print()