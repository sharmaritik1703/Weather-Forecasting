import streamlit as st
import pandas as pd

st.title("Weather Forecasting")
st.markdown("""
$\\textrm{A machine learning algorithm to predict the weather status using entered parameters}$.

- $\\textrm{Go to top left corner}$.
- $\\textrm{Enter the value of features in Data page}$.
- $\\textrm{See the weather status in Results page}$.
""")

df = pd.read_csv("weather_test.csv")
df.drop(["Unnamed: 0", "date"], axis=1, inplace=True)

st.subheader("Features")
with st.expander(label="The accepted features are given here: 👇👇 "):
  st.dataframe(data=df.columns, width=250, height=380)
