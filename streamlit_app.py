import streamlit
import requests
import pandas
streamlit.header('🍌🥭 Fruityvice Fruit Advice! 🥝🍇')
streamlit.header('Breakfast Menu')
streamlit.text('🍞 bread jam | 🥣 omega 3 Blueberry')
streamlit.text('🐔 egg omelette | 🥑 avacado')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

# my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
