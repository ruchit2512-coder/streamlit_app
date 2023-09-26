import streamlit
import requests
import pandas
import snowflake.connector


streamlit.header('🍌🥭 Build Your Own Smoothy! 🥝🍇')
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



def get_fruityvise_data(this_fruit_choice) :
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header('🍌🥭 Fruityvice Fruit Advice! 🥝🍇')
try :
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice :
    streamlit.error('please select a food to get the information')
  else :
    back_from_function = get_fruityvise_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e :
  streamlit.error()


streamlit.header('Fruit Load List Contains :')

def get_fruit_load_list() :
  with my_cnx.cursor() as my_cur :
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('get fruit load list') :
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows =  get_fruit_load_list()
  streamlit.dataframe(my_data_rows)



  



streamlit.write('The user entered ',add_my_fruit)

def insert_row_snowflake(new_fruit) :
  with my_cnx.cursor() as my_cur :
    my_cur.execute("insert into fruit_load_list values(' from streamlit')")
    return "thanks for adding" + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like information about?')
if streamlit.button('Add fruit to the list') :
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows =  insert_row_snowflake(add_my_fruit)
  streamlit.txet(my_data_rows)

# # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# # streamlit.text(fruityvice_response.json())
# # my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur.execute("select * from fruit_load_list")
# my_data_row = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
# streamlit.dataframe(my_data_row)




