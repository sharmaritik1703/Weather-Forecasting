import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model.pkl', 'rb'))

df = pd.read_csv("user-data.csv")
df.drop('Unnamed: 0', axis=1, inplace=True)

st.title("See Weather: ")
st.markdown("Click on **Forecast** to see weather.")

st.subheader("Input")
df = st.data_editor(data=df)

def predict():
    rain_status = {0: "No Rain", 1: "Low Rain", 2: "High Rain"}
    value = model.predict(df)[0]
    weather = rain_status[value]
    st.subheader(weather)

st.button(label="Forecast", on_click=predict)
