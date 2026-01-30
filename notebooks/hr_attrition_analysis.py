import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

# Load dataset
df = pd.read_csv('../data/raw_hr_data.csv')

print("Dataset loaded successfully")
print("Shape:", df.shape)
print(df.head())

# ----------------------------
# Data Cleaning
# ----------------------------

# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Drop constant / irrelevant columns
df.drop(['EmployeeCount', 'Over18', 'StandardHours'], axis=1, inplace=True)

# Convert Attrition to numeric
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

print("\nData cleaning completed")
print("Updated shape:", df.shape)

# Save cleaned dataset
df.to_csv('../data/cleaned_hr_attrition.csv', index=False)
print("Cleaned dataset saved")

# ----------------------------
# Overall Attrition Rate
# ----------------------------

attrition_rate = df['Attrition'].value_counts(normalize=True) * 100
print("\nOverall Attrition Rate (%):")
print(attrition_rate)

# ----------------------------
# Attrition by Department
# ----------------------------

plt.figure(figsize=(6,4))
sns.barplot(x='Department', y='Attrition', data=df)
plt.title('Attrition Rate by Department')
plt.tight_layout()
plt.show()

# ----------------------------
# Attrition by Job Role
# ----------------------------

plt.figure(figsize=(10,5))
sns.barplot(x='JobRole', y='Attrition', data=df)
plt.xticks(rotation=45)
plt.title('Attrition Rate by Job Role')
plt.tight_layout()
plt.show()

# ----------------------------
# Attrition vs Overtime
# ----------------------------

plt.figure(figsize=(5,4))
sns.barplot(x='OverTime', y='Attrition', data=df)
plt.title('Attrition by Overtime')
plt.tight_layout()
plt.show()


# ----------------------------
# Attrition vs Monthly Income
# ----------------------------

plt.figure(figsize=(6,4))
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
plt.xticks([0, 1], ['Stayed', 'Left'])
plt.title('Monthly Income vs Attrition')
plt.tight_layout()
plt.show()

# ----------------------------
# Attrition vs Job Satisfaction
# ----------------------------

plt.figure(figsize=(6,4))
sns.barplot(x='JobSatisfaction', y='Attrition', data=df)
plt.title('Job Satisfaction vs Attrition')
plt.tight_layout()
plt.show()

# ----------------------------
# Attrition vs Years at Company
# ----------------------------

plt.figure(figsize=(6,4))
sns.barplot(x='YearsAtCompany', y='Attrition', data=df)
plt.title('Attrition by Years at Company')
plt.tight_layout()
plt.show()
