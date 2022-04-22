import streamlit

streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥗Omega 3 & Blueberry oatmeal')
streamlit.text('🌮Kale, Spinach, & Rocket Smoothie')
streamlit.text('🦪Hard-boiled Free-range Egg')
streamlit.text('🍞Avacodo Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list =my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list)
#let's put a pick list here so that user can pick what they want to pick

streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

##fruits_to_show = my_fruit_list.loc[fruits_selected]

#streamlit.dataframe(my_fruit_list)
##streamlit.dataframe(fruits_to_show)
