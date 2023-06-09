import streamlit as st
import pandas as pd

st.title("Weather Forecasting")
st.markdown("A machine learning algorithm to predict the weather status using entered parameters.")

st.subheader("Accepted Parameters")
df = pd.read_csv("weather_test.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)

with st.expander(label=""):
  st.dataframe(data=df.columns, width=300, height=450)
