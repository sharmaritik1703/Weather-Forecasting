import streamlit as st
import pandas as pd

st.title("Weather Forecasting")
st.markdown("A machine learning algorithm to predict the weather status using entered parameters.")

df = pd.read_csv("weather_test.csv")
df.drop(["Unnamed: 0", "date"], axis=1, inplace=True)

st.subheader("Features")
with st.expander(label="👇👇 "):
  st.dataframe(data=df.columns, width=250, height=380)
