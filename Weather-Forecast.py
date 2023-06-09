import streamlit as st
import pandas as pd

st.title("Weather Forecast")
st.subheader("A machine learning algorithm to predict the weather status using entered parameters.")

st.subheader("Accepted Parameters")
df = pd.read_csv("weather_test.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)

st.dataframe(data=df.columns, width=100, height=500)
