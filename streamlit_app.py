import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title("Zomato Restaurant Rating Prediction")

st.write("Enter restaurant details below")

# User inputs
online_order = st.number_input("Online Order")
book_table = st.number_input("Book Table")
votes = st.number_input("Votes")
location = st.number_input("Location")
restaurant_type = st.number_input("Restaurant Type")
cuisines = st.number_input("Cuisines")
cost = st.number_input("Cost")
menu_item = st.number_input("Menu Item")

# Prediction
if st.button("Predict Rating"):

    features = np.array([[online_order,
                          book_table,
                          votes,
                          location,
                          restaurant_type,
                          cuisines,
                          cost,
                          menu_item]])

    prediction = model.predict(features)

    st.success(f"Predicted Rating: {round(prediction[0],1)}")
