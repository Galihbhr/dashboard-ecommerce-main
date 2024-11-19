import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv(r"C:\Users\Galih\Documents\coding\dashboard\dashboard-ecommerce-main\data\all_df.csv")
st.header('Ecommerce Dashboard :sparkles:')


st.subheader('Top 10 Product')
# col1, col2 = st.columns(2)
# Mengelompokkan data berdasarkan kategori produk dan menghitung jumlah item terjual
product_sold_df = all_df.groupby('product_category_name_english')['order_item_id'].sum().sort_values(ascending=False)
# Mengambil 10 produk teratas berdasarkan jumlah item terjual
top_10_products = product_sold_df.head(10)

# with col1:
    # Menampilkan 10 produk teratas di Streamlit sebagai tabel
st.write("Tabel Top 10 Products Sold:")
st.table(top_10_products.reset_index().rename(columns={
    'product_category_name_english': 'Product Category',
    'order_item_id': 'Total Sold'
}))

st.write('Grafik Top 10 Product')
#  grafik:
fig, ax = plt.subplots(figsize=(100, 50))

sns.barplot(
    x=top_10_products.values, 
    y=top_10_products.index, 
    palette="viridis"
)
    
    # Customize the plot
ax.set_title("Top 10 Product", loc="center", fontsize=150)
ax.set_ylabel('Nama Product', loc= 'center', fontsize=150)
ax.set_xlabel('jumlah product', loc= 'center', fontsize=150)
ax.tick_params(axis='y', labelsize=100)
ax.tick_params(axis='x', labelsize=100)

    # Show the Streamlit app
st.pyplot(fig)

st.subheader('Penjualan pertahun')

# Konversi kolom 'order_purchase_timestamp' menjadi datetime
all_df['order_purchase_timestamp'] = pd.to_datetime(all_df['order_purchase_timestamp'])

# Tambahkan kolom year_month
all_df['year_month'] = all_df['order_purchase_timestamp'].dt.to_period('M')

# Cetak hasil untuk memastikan
print(all_df[['order_purchase_timestamp', 'year_month']].head())

# Mengelompokkan data berdasarkan tahun dan bulan, menghitung jumlah entri per kombinasi
monthly_counts = all_df.groupby('year_month')['order_item_id'].count()
monthly_counts_df = monthly_counts.reset_index()
monthly_counts_df.columns = ['year_month', 'order_item_id']

# Pastikan kolom 'year_month' diubah ke format datetime
monthly_counts_df['year_month'] = pd.to_datetime(monthly_counts_df['year_month'].astype(str))

fig, ax = plt.subplots(figsize=(100, 50))
sns.barplot(x='year_month', y='order_item_id', data=monthly_counts_df)
    # Customize the plot
ax.set_title("Penjualan", loc="center", fontsize=150)
ax.set_ylabel('Jumlah', loc= 'center', fontsize=150)
ax.set_xlabel('Tahun-Bulan', loc= 'center', fontsize=150)
ax.tick_params(axis='y', labelsize=100)
ax.tick_params(axis='x', labelsize=50, rotation=45)

    # Show the Streamlit app
st.pyplot(fig)