import streamlit
import pandas
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('Breakfast Menu')
streamlit.text('🍞 bread jam | 🥣 omega 3 Blueberry')
streamlit.text('🐔 egg omelette | 🥑 avacado')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
