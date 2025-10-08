import pandas as pd
import os
import glob


folder_path = os.path.join(os.path.dirname(__file__), "data")
print("📂 Looking in folder:", folder_path)
all_files = glob.glob(os.path.join(folder_path, "*.csv"))
print("🔍 Found files:", all_files)
all_data = []
for file in all_files:
    print("📘 Reading:", file)
    df = pd.read_csv(file)
    all_data.append(df)

if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    print("✅ Combined DataFrame shape:", combined_df.shape)
    print("🪄 Columns found:", combined_df.columns.tolist())
else:
    print("⚠️ No CSV files found in:", folder_path)
import matplotlib.pyplot as plt

combined_df = combined_df.dropna(subset=['Order Date', 'Price Each', 'Quantity Ordered'])

combined_df = combined_df[combined_df['Order Date'].str[0:2] != 'Or']


combined_df['Order Date'] = pd.to_datetime(combined_df['Order Date'], errors='coerce')
combined_df['Quantity Ordered'] = pd.to_numeric(combined_df['Quantity Ordered'], errors='coerce')
combined_df['Price Each'] = pd.to_numeric(combined_df['Price Each'], errors='coerce')


combined_df['Month'] = combined_df['Order Date'].dt.month
combined_df['Sales'] = combined_df['Quantity Ordered'] * combined_df['Price Each']
monthly_sales = combined_df.groupby('Month')['Sales'].sum()

print("📆 Monthly Sales:")
print(monthly_sales)
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linewidth=2)
plt.title('Monthly Sales Trend - 2019', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.grid(True)
plt.show()
