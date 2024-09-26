# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('dataset.csv')

# View the first few rows of the dataset
print(df.head())

# Check the shape of the dataset
print(df.shape)

# Check for missing values
print(df.isnull().sum())

# Data types of each column
print(df.dtypes)

# Summary statistics
print(df.describe())

# Distribution of numerical columns
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
sns.boxplot(data=df[numerical_cols])
plt.show()
# Distribution of categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    sns.countplot(x=col, data=df)
    plt.title(col)
    plt.show()

# Correlation analysis
corr = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()
