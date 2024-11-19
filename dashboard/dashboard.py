import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("https://raw.githubusercontent.com/Galihbhr/dashboard-ecommerce-main/refs/heads/main/dashboard/all_df.csv")
st.header('Ecommerce Dashboard :sparkles:')

# Top 10 Product
st.subheader('Top 10 Product')

product_sold_df = all_df.groupby('product_category_name_english')['order_item_id'].sum().sort_values(ascending=False)
top_10_products = product_sold_df.head(10)

st.write("Tabel Top 10 Products Sold:")
st.table(top_10_products.reset_index().rename(columns={
    'product_category_name_english': 'Product Category',
    'order_item_id': 'Total Sold'
}))

st.write('Grafik Top 10 Product')
fig, ax = plt.subplots(figsize=(15, 8))

sns.barplot(
    x=top_10_products.values, 
    y=top_10_products.index
)

ax.set_title("Top 10 Product", ha="center", fontsize=20)
ax.set_ylabel('Nama Product', fontsize=15)
ax.set_xlabel('Jumlah Product', fontsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', labelsize=10)

st.pyplot(fig)

# Penjualan pertahun
st.subheader('Penjualan per Tahun')

all_df['order_purchase_timestamp'] = pd.to_datetime(all_df['order_purchase_timestamp'])
all_df['year_month'] = all_df['order_purchase_timestamp'].dt.to_period('M')

monthly_counts = all_df.groupby('year_month')['order_item_id'].count()
monthly_counts_df = monthly_counts.reset_index()
monthly_counts_df.columns = ['year_month', 'order_item_id']
monthly_counts_df['year_month'] = pd.to_datetime(monthly_counts_df['year_month'].astype(str))

fig, ax = plt.subplots(figsize=(15, 8))
sns.barplot(x='year_month', y='order_item_id', data=monthly_counts_df)

ax.set_title("Penjualan", ha="center", fontsize=20)
ax.set_ylabel('Jumlah', fontsize=15)
ax.set_xlabel('Tahun-Bulan', fontsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', labelsize=10, rotation=30)

st.pyplot(fig)
