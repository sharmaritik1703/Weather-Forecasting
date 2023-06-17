import streamlit as st
import pandas as pd
from PIL import Image
import pickle
from Data import df

model = pickle.load(open('model.pkl', 'rb'))

image1 = Image.open("sunny.jpg")
image2 = Image.open("cloudy.jpg")
image3 = Image.open("rainy.jpg")

st.title("See Weather: ")
st.markdown("Click on **Forecast** to see weather.")

st.subheader("Input")
df = st.data_editor(data=df)

def predict():
    value = model.predict(df)
    
    if value[0] == 0:
        image = image1
        weather = "Sunny"
    elif value[0] == 1:
        image = image2
        weather = "Cloudy"
    else:
        image = image3
        weather = "Rainy"

    st.image(image=image)
    st.subheader(f"{weather} day")


st.button(label="Forecast", on_click=predict)
