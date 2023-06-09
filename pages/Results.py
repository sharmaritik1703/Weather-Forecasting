from Data import model
import streamlit as st
import pandas as pd
from PIL import Image

image1 = Image.open("sunny.jpg")
image2 = Image.open("cloudy.jpg")
image3 = Image.open("rainy.jpg")

st.title("See Weather: ")
st.markdown("Click on **Forecast** to see weather.")
df = pd.read_csv("user-data.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)

st.subheader("Input")
df = st.data_editor(data=df)

def predict():
    outputs = {0: "Sunny", 1: "Cloudy", 2: "Rainy"}
    value = model.predict(df)
    weather = outputs[value[0]]

    if value[0] == 0:
        image = image1
    elif value[0] == 1:
        image = image2
    else:
        image = image3

    st.image(image=image)
    st.subheader(f"{weather} day")


st.button(label="Forecast", on_click=predict)
