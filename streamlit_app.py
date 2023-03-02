import streamlit

streamlit.title("Hey there! My name is Eugene, I'm a Junior Data Analytics Engineer")

streamlit.header('My Courses')
streamlit.text('01. EPAM: Data Analytics Engineering')
streamlit.text('02. IT Academy: FUNDAMENTALS OF BI ANALYTICS')
streamlit.text('03. DataYoga: QLIK SENSE MARATHON: DATA VISUALIZATION')


streamlit.title("My Parrents New Healthy Dinner")

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avokado Toasts')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
   
