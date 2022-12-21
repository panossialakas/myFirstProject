import pandas as pd
import matplotlib.pyplot as plt

# 1st step: load file to analyze
data = pd.read_csv('finance_liquor_sales.csv')

# total number of bottles sold
total = data['bottles_sold'].sum(numeric_only=True)

# insert percentage column of sales for each transaction
data.insert(24, 'percentage_of_sales_per_store', data['bottles_sold']/total)

# group data with sum for zip, store name and item_description to find most popular
# with sum aggregation we find the percentage of sales per store for each item
# as_index = False, for easier visualization of data
df = data.groupby(['zip_code', 'store_name', 'item_description'], as_index=False, group_keys=True).sum(numeric_only=True)
# print(df.shape)
# print(df['bottles_sold'].sort_values(ascending=False))

# visualize data
df.plot(kind='scatter', x='zip_code', y='bottles_sold', s=50, c=[int(i) for i in range(72)], colormap='jet', colorbar=True, title='Bottles Sold per Zip Code')
df.plot(kind='scatter', x='store_name', y='bottles_sold', s=50, c=[int(i) for i in range(72)], colormap='jet', colorbar=True, title='Bottles Sold per Store')
plt.xticks(rotation=90)
df.plot.barh(x='store_name', y='percentage_of_sales_per_store', title='Percentage of Sales per Store')
plt.show()


