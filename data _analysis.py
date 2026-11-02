Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# MODULE 04: PYTHON DATA & APIs
# Project: Python Data Analysis Application

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from google.colab import files

# 1. Upload Dataset
print("Upload your CSV dataset")
uploaded = files.upload()

file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name)

print("\nDataset Loaded Successfully!")
print(df.head())

# 2. Dataset Information
print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

# 3. Data Cleaning
print("\nMissing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()
df = df.fillna(df.select_dtypes(include=np.number).mean())

print("\nCleaned Dataset:")
print(df.head())

# 4. Data Analysis
print("\nStatistical Analysis:")
print(df.describe())

print("\nColumn Names:")
print(df.columns.tolist())

# 5. Data Visualization
numeric_data = df.select_dtypes(include=np.number)

if not numeric_data.empty:
    numeric_data.hist(figsize=(12, 8))
    plt.suptitle("Data Analysis Graphs")
    plt.tight_layout()
    plt.show()

...     plt.figure(figsize=(10, 6))
...     sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
...     plt.title("Correlation Heatmap")
...     plt.show()
... 
... # 6. REST API Data Fetching
... url = "https://jsonplaceholder.typicode.com/users"
... 
... response = requests.get(url, timeout=15)
... 
... if response.status_code == 200:
...     api_data = response.json()
...     api_df = pd.json_normalize(api_data)
... 
...     print("\nAPI Data Successfully Retrieved!")
...     print(api_df.head())
... 
...     api_df.to_csv("api_data.csv", index=False)
... else:
...     print("API request failed:", response.status_code)
... 
... # 7. Generate Analysis Report
... with open("analysis_report.txt", "w") as report:
...     report.write("PYTHON DATA ANALYSIS REPORT\n")
...     report.write("===========================\n")
...     report.write(f"Total Rows: {df.shape[0]}\n")
...     report.write(f"Total Columns: {df.shape[1]}\n")
...     report.write("\nDataset Summary:\n")
...     report.write(df.describe().to_string())
...     report.write("\n\nMissing Values:\n")
...     report.write(df.isnull().sum().to_string())
... 
... # 8. Save Cleaned Dataset
... df.to_csv("cleaned_dataset.csv", index=False)
... 
... print("\nPROJECT COMPLETED SUCCESSFULLY!")
... print("Analysis report generated.")
... print("Cleaned dataset saved.")
... 
