import streamlit as st
import os
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from babel.numbers import format_currency

st.set_page_config(
    page_title="Sales Analysis",
    page_icon="💲",
)

st.title("E-commerce sales performance")

path = os.path.dirname(__file__)
my_file = path+'/../all_data.csv'
all_df = pd.read_csv(my_file)
datetime_columns = ["order_approved_at", "order_delivered_customer_date"]
all_df.sort_values(by="order_approved_at", inplace=True)
all_df.reset_index(inplace=True)

def tingkat_penjualan_2016(df):
    df_tingkat_penjualan_2016 = all_df[all_df.order_year == 2016]

    tingkat_penjualan_2016 = df_tingkat_penjualan_2016.groupby(by='order_month').agg({
        "order_id": "nunique",
        "order_month_name" : pd.Series.mode,
        "payment_value" : "sum"
    }).sort_values(by="order_month").reset_index()
    
    return tingkat_penjualan_2016

def tingkat_penjualan_2017(df):
    df_tingkat_penjualan_2017 = all_df[all_df.order_year == 2017]

    tingkat_penjualan_2017 = df_tingkat_penjualan_2017.groupby(by='order_month').agg({
        "order_id": "nunique",
        "order_month_name" : pd.Series.mode,
        "payment_value" : "sum"
    }).sort_values(by="order_month").reset_index()
    
    return tingkat_penjualan_2017

def tingkat_penjualan_2018(df):
    df_tingkat_penjualan_2018 = all_df[all_df.order_year == 2018]

    tingkat_penjualan_2018 = df_tingkat_penjualan_2018.groupby(by='order_month').agg({
        "order_id": "nunique",
        "order_month_name" : pd.Series.mode,
        "payment_value" : "sum"
    }).sort_values(by="order_month").reset_index()
    
    return tingkat_penjualan_2018

with st.sidebar:
    selected = option_menu(
        menu_title="Year",
        options=["2016","2017","2018"],
    )
    
if selected == "2016":
    tingkat_penjualan_2016 = tingkat_penjualan_2016(all_df)
    col1, col2 = st.columns(2)

    with col1:
        total_orders = tingkat_penjualan_2016.order_id.sum()
        st.metric("Total orders", value=total_orders)
    
    with col2:
        total_revenue = format_currency(tingkat_penjualan_2016.payment_value.sum(), "AUD ", locale='es_CO') 
        st.metric("Total Revenue", value=total_revenue)
    
    with st.container():
            
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=tingkat_penjualan_2016["order_month_name"],
            y=tingkat_penjualan_2016["order_id"],
            mode='lines+markers',
            marker=dict(
                color='red',
                size=8,
            ),
            line=dict(
                width=3,
            ),
        ))

        for x, y in zip(tingkat_penjualan_2016["order_month_name"], tingkat_penjualan_2016["order_id"]):
            fig.add_annotation(
                x=x,
                y=y+15,
                text=str(y),
                font=dict(
                    size=12,
                ),
                showarrow=False,
                textangle=0,
            )        
        
        fig.update_layout(
            title="Sales Performance 2016",
            xaxis=dict(
                title="Order Month",
                titlefont=dict(
                    size=14,
                ),
                tickfont=dict(
                    size=14,
                ),
            ),
            yaxis=dict(
                title="Number of orders",
                titlefont=dict(
                    size=14,
                ),
                tickfont=dict(
                    size=14,
                ),
            ),
            width=650,
            height=400,
        )
                
        st.plotly_chart(fig)
        
        with st.expander("AI first", expanded=False):
            st.write("AI analysis 2016 ....")
        with st.expander("AI next", expanded=False):
            st.write("AI analysis 2016 ....")

if selected == "2017":
    tingkat_penjualan_2017 = tingkat_penjualan_2017(all_df)
    col1, col2 = st.columns(2)

    with col1:
        total_orders = tingkat_penjualan_2017.order_id.sum()
        st.metric("Total orders", value=total_orders)
    
    with col2:
        total_revenue = format_currency(tingkat_penjualan_2017.payment_value.sum(), "AUD", locale='es_CO') 
        st.metric("Total Revenue", value=total_revenue)

    fig = go.Figure()

    with st.container():
        fig.add_trace(go.Scatter(
            x=tingkat_penjualan_2017["order_month_name"],
            y=tingkat_penjualan_2017["order_id"],
            mode='lines+markers',
            marker=dict(
                color='red',
                size=8,
            ),
            line=dict(
                width=3,
            ),
        ))

        for x, y in zip(tingkat_penjualan_2017["order_month_name"], tingkat_penjualan_2017["order_id"]):
            fig.add_annotation(
                x=x,
                y=y+150,
                text=str(y),
                font=dict(
                    size=12,
                ),
                showarrow=False,
                textangle=0,
            )

        fig.update_layout(
            title="Sales Performance 2017",
            xaxis=dict(
                title="Order Month",
                titlefont=dict(
                    size=14,
                ),
                tickfont=dict(
                    size=14,
                ),
            ),
            yaxis=dict(
                title="Number of orders",
                titlefont=dict(
                    size=14,
                ),
                tickfont=dict(
                    size=14,
                ),
            ),
            width=650,
            height=400,
        )

        st.plotly_chart(fig)
        
        with st.expander("AI first", expanded=False):
            st.write("AI analysis 2017....")
        with st.expander("AI next", expanded=False):
            st.write("AI analysis 2017....")

if selected == "2018":
    tingkat_penjualan_2018 = tingkat_penjualan_2018(all_df)
    col1, col2 = st.columns(2)

    with col1:
        total_orders = tingkat_penjualan_2018.order_id.sum()
        st.metric("Total orders", value=total_orders)
    
    with col2:
        total_revenue = format_currency(tingkat_penjualan_2018.payment_value.sum(), "AUD", locale='es_CO') 
        st.metric("Total Revenue", value=total_revenue)

    fig = go.Figure()

    with st.container():
        fig.add_trace(go.Scatter(
            x=tingkat_penjualan_2018["order_month_name"],
            y=tingkat_penjualan_2018["order_id"],
            mode='lines+markers',
            marker=dict(
                color='red',
                size=8,
            ),
            line=dict(
                width=3,
            ),
        ))

        for x, y in zip(tingkat_penjualan_2018["order_month_name"], tingkat_penjualan_2018["order_id"]):
            fig.add_annotation(
                x=x,
                y=y+150,
                text=str(y),
                font=dict(
                    size=12,
                ),
                showarrow=False,
                textangle=0,
            )

        fig.update_layout(
            title="Sales Performance 2018",
            xaxis=dict(
                title="Order Month",
                titlefont=dict(
                    size=14,
                ),
                tickfont=dict(
                    size=14,
                ),
            ),
            yaxis=dict(
                title="Number of orders",
                titlefont=dict(
                    size=14,
                ),
                tickfont=dict(
                    size=14,
                ),
            ),
            width=650,
            height=400,
        )

        st.plotly_chart(fig)

        with st.expander("AI first", expanded=False):
            st.write("AI analysis 2018....")
        with st.expander("AI next", expanded=False):
            st.write("AI analysis 2018....")