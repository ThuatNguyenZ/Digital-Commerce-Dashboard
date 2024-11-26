import streamlit as st
import os
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.graph_objects as go

st.set_page_config(
    page_title="Order and Purchase",
    page_icon="🛒",
)

with st.sidebar:
    selected = option_menu(
        menu_title="Order and Purchase",
        options=["Order Delivery Status","Payment Type","Purchase Time"],
    )