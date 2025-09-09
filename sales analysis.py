# sales_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('sales_data.csv')

# Show first few rows
print(df.head())

# Basic stats
print(df.describe())

# Total sales by region
sales_by_region = df.groupby('Region')['Sales'].sum()
print(sales_by_region)

# Plot
sales_by_region.plot(kind='bar')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
