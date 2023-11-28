import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3* Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toeast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import fruit list from source csv file
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# set up multi-select pick list
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# display fruits list
streamlit.dataframe(my_fruit_list)
