# -*- coding: utf-8 -*-
"""housing analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kqq2MRynZrlLZn1h9pL9Qgb4bhXihwXg

# Import Libraries
"""

# Import essential libraries
import pandas as pd  # For data manipulation
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For data visualization
import seaborn as sns  # For advanced visualizations

# Import libraries for machine learning and evaluation
from sklearn.model_selection import train_test_split  # For splitting the dataset
from sklearn.linear_model import LinearRegression  # For linear regression
from sklearn.metrics import mean_squared_error, r2_score  # For model evaluation

"""# Loading the Data"""

# Load the data into a pandas DataFrame
df = pd.read_csv("housing.csv")

# Check the overall shape of the dataset
df.shape

# Display the first few rows to understand the structure of the dataset
df.head()

"""#Exploratory Data Analysis (EDA)

**Understand the Data**
"""

# Check for missing values
df.isnull().sum()

# Get data types of each column
df.dtypes

# Statistical Summary
df.describe()

"""**Visualize Distributions**"""

# Distribution of the target variable (MEDV)
plt.figure(figsize=(8, 5))
sns.histplot(df['MEDV'], kde=True, bins=30, color='blue')
plt.title("Distribution of MEDV (Target Variable)")
plt.xlabel("MEDV")
plt.ylabel("Frequency")
plt.show()

# Visualize relationships between important features and MEDV
selected_features = ['RM', 'LSTAT', 'PTRATIO', 'MEDV']
sns.pairplot(df[selected_features], diag_kind='kde')
plt.show()

"""**Correlation Analysis**"""

# Correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# Focus on correlations with the target variable (MEDV)
correlation = df.corr()['MEDV'].sort_values(ascending=False)
correlation

"""# Data Preprocessing

**Feature Selection**
"""

# Select features based on correlation and domain knowledge
features = ['RM', 'LSTAT', 'PTRATIO']  # Adjust based on your analysis
X = df[features]  # Independent variables
y = df['MEDV']  # Dependent variable (target)

"""**Splitting Data into Training and Testing Sets**"""

# Split the data into training and testing sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

"""# Model Selection and Training

**Initialize and Train the Model**
"""

# Initialize the linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Display model coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
print("\nFeature-Coefficient Mapping:")
for feature, coef in zip(features, model.coef_):
    print(f"{feature}: {coef}")

"""# Model Evaluation

**Predictions**
"""

# Predict on the test set
y_pred = model.predict(X_test)

"""**Metrics**"""

# Calculate Mean Squared Error and R-squared
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Performance Metrics:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.2f}")

"""**Visualization of Predictions**"""

# Plot actual vs predicted values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='blue', label='Predictions')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', lw=2, label='Perfect Prediction')
plt.title("Actual vs Predicted MEDV")
plt.xlabel("Actual MEDV")
plt.ylabel("Predicted MEDV")
plt.legend()
plt.show()

"""# Compare Model Performance"""

from sklearn.linear_model import Ridge, Lasso

# Ridge Regression
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
ridge_pred = ridge.predict(X_test)
ridge_mse = mean_squared_error(y_test, ridge_pred)
ridge_r2 = r2_score(y_test, ridge_pred)

# Lasso Regression
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
lasso_pred = lasso.predict(X_test)
lasso_mse = mean_squared_error(y_test, lasso_pred)
lasso_r2 = r2_score(y_test, lasso_pred)

print("Comparison of Models:")
print(f"Linear Regression: MSE={mse:.2f}, R2={r2:.2f}")
print(f"Ridge Regression: MSE={ridge_mse:.2f}, R2={ridge_r2:.2f}")
print(f"Lasso Regression: MSE={lasso_mse:.2f}, R2={lasso_r2:.2f}")

