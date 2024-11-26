import streamlit as st
import os
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="E-Commerce Data Analysis",
    page_icon="📊",
)

st.title("DASHBOARD E-COMMERCE CUSTOMER AND SALES ANALYSIS")

with st.sidebar:
    selected = option_menu(
        menu_title="DASHBOARD",
        options=["About Projects","Dataset Overview"],
    )

if selected == "About Projects":
    path = os.path.dirname(__file__)
    my_file = path+'/images/img1.png'
    image = Image.open(my_file)
    # resized_image = image.resize((650, 350))
    st.image(image, caption='E-Comerce Analysis Dashboard')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("This project is an interactive dashboard built with Streamlit. The dashboard uses the Vietnam E-commerce Public Dataset as a data source. This dataset contains information about e-commerce transactions in Vietnam and provides an overview of online purchasing trends and patterns in the country.")
    with col2:
        st.write("In this dashboard, interesting data visualizations are created. This visualization will help understand different aspects of e-commerce sales in Vietnam, including information about the cities with the largest number of sellers, the most popular product categories, and purchase trends over a certain period of time.")
    with col3:
        st.write("Additionally, the dashboard is equipped with interactive features that allow you to explore the data in more depth.")
        st.write("The purpose of this project is to provide an interactive and informative dashboard for researching and extracting information from the E-Commerce Public Dataset dataset.")

  
if selected == "Dataset Overview":
    st.write("The dataset used is the E-Commerce Public Dataset.")
    st.write("This dataset consists of information collected from e-commerce transactions in Vietnam over a certain period of time. The dataset consists of several related files and provides a comprehensive insight into the e-commerce industry in Vietnam.")