import streamlit as st
import os
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.graph_objects as go

st.set_page_config(
    page_title="Product Analysis",
    page_icon="🛍️",
)

with st.sidebar:
    selected = option_menu(
        menu_title="Product",
        options=["Top-selling product","Worst-selling product",],
    )

path = os.path.dirname(__file__)
my_file = path+'/../all_data.csv'
all_df = pd.read_csv(my_file)
datetime_columns = ["order_approved_at", "order_delivered_customer_date"]
all_df.sort_values(by="order_approved_at", inplace=True)
all_df.reset_index(inplace=True)

def df_large_product_sales(df):

    df_large_product_sales = all_df.groupby(by="product_name").agg({
        "payment_value": "sum",
    }).nlargest(10, "payment_value").round().reset_index()

    return df_large_product_sales

def df_samall_product_sales(df):

    df_samall_product_sales = all_df.groupby(by="product_name").agg({
        "payment_value": "sum",
    }).nsmallest(10, "payment_value").round().reset_index()

    return df_samall_product_sales

if selected == "Top-selling product":

    st.title("Top-selling Product Over 2016 - 2018")

    df_product_sales = df_large_product_sales(all_df)

    with st.container():
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=df_product_sales['product_name'],
            y=df_product_sales['payment_value'],
            marker=dict(
                color='rgb(173, 216, 230)',  # Set color here
            ),
        ))
        
        for i, v in enumerate(df_product_sales['payment_value']):
            fig.add_annotation(
                x=df_product_sales['product_name'][i],
                y=v,
                text=str(v),
                font=dict(
                    size=10,
                    color='white',  # Set text color here
                ),
                showarrow=False,
                textangle=0,
                align='center',
                yshift=10
            )

        fig.update_layout(
            title='Top 10 Best Selling Products',
            xaxis=dict(
                title='Product Name',
                tickangle=45,
                tickfont=dict(
                    size=12,
                ),
                automargin=True,
            ),
            yaxis=dict(
                title='Total Sales',
                tickformat='plain',
                tickfont=dict(
                    size=12,
                ),
            ),
            width=700,
            height=500,
            showlegend=False,
        )
        
        st.plotly_chart(fig)

        with st.expander("AI first", expanded=False):
            st.write("AI analysis Top-selling ....")
        with st.expander("AI next", expanded=False):
            st.write("AI analysis Top-selling ....")

if selected == "Worst-selling product":
    st.title("Worst-selling Product Over 2016 - 2018")
    df_product_sales = df_samall_product_sales(all_df)
    with st.container():

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=df_product_sales['product_name'],
            y=df_product_sales['payment_value'],
            marker=dict(
                color='rgb(173, 216, 230)',  # Set color here
            ),
        ))

        for i, v in enumerate(df_product_sales['payment_value']):
            fig.add_annotation(
                x=df_product_sales['product_name'][i],
                y=v+5,
                text=str(v),
                font=dict(
                    size=10,
                    color='white',  # Set text color here
                ),
                showarrow=False,
                textangle=0,
                align='center',
                yshift=10
            )

        fig.update_layout(
            title='Top 10 Worst Selling Products',
            xaxis=dict(
                title='Product Name',
                tickangle=45,
                tickfont=dict(
                    size=12,
                ),
                automargin=True,
            ),
            yaxis=dict(
                title='Total Sales',
                tickformat='plain',
                tickfont=dict(
                    size=12,
                ),
            ),
            width=750,
            height=500,
            showlegend=False,
        )

        st.plotly_chart(fig)
        
        with st.expander("AI first", expanded=False):
            st.write("AI analysis Worst-selling ....")
        with st.expander("AI next", expanded=False):
            st.write("AI analysis Worst-selling ....")