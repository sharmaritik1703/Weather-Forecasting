import streamlit as st
import pandas as pd

st.title("Weather Forecast")
st.markdown("A machine learning algorithm to predict the weather status using entered parameters.")

st.subheader("Accepted Parameters")
df = pd.read_csv("weather_test.csv")

st.dataframe(df.columns)
