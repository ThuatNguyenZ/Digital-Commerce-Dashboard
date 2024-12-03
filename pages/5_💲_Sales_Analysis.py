import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="Sales Analysis",
    page_icon="💲",
)

st.title("E-commerce sales performance")

my_file = 'Data process\product_data_nivea_khu-mui-co-the.xlsx'

df_nivea = pd.read_excel(my_file)

df_nivea['current_date'] = pd.to_datetime(df_nivea['current_date'])

plt.figure(figsize=(12, 6))
sns.lineplot(x='current_date', y='price', data=df_nivea)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Nivea Product Price Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

st.pyplot(plt)

price_trends = df_nivea.groupby('current_date')['price'].mean()
st.write("### Average Price Trends", price_trends)