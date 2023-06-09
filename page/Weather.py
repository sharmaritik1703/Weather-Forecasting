import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.set_page_config(page_icon="⚙️")

st.title("Weather Forecasting")
st.markdown("A machine learning algorithm to predict the weather status using entered parameters.")

model = pickle.load(open('weather.pkl', 'rb'))
directions = {'E': 0, 'W': 1, 'N': 2, 'S': 3, 'NE': 4, 'SE': 5, 'NW': 6, 'SW': 7}

if 'data' not in st.session_state:
    st.session_state.data = np.zeros(shape=(1, 10))

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, col8 = st.columns(2)
col9, col10 = st.columns(2)

with col1:
    st.session_state.data[0, 0] = st.slider(label="Average Temperature", min_value=-3.7, max_value=30.0)

with col2:
    st.session_state.data[0, 1] = st.slider(label="Min. Temperature", min_value=-7.0, max_value=24.0)

with col3:
    st.session_state.data[0, 2] = st.slider(label="Max. Temperature", min_value=0.0, max_value=37.3)

with col4:
    st.session_state.data[0, 3] = st.slider(label="Precipitation", min_value=0.0, max_value=26.0)

with col5:
    st.session_state.data[0, 4] = st.slider(label="Avg. Wind Speed", min_value=1.0, max_value=5.2)

with col6:
    st.session_state.data[0, 5] = st.slider(label="Max. Wind Speed", min_value=2.0, max_value=13.3)

with col7:
    wsd = st.selectbox(label="Max. Wind Speed Direction", options=directions.keys())
    st.session_state.data[0, 6] = directions[wsd]

with col8:
    st.session_state.data[0, 7] = st.slider(label="Max. Inst. Wind Speed ", min_value=2.0, max_value=21.5)

with col9:
    msd = st.selectbox(label="Max. Inst. Wind Speed Direction", options=directions.keys())
    st.session_state.data[0, 8] = directions[msd]

with col10:
    st.session_state.data[0, 9] = st.slider(label="Min. Atmospheric Pressure", min_value=1000.00, max_value=1026.00)

main = pd.read_csv("weather_test.csv")
df = pd.DataFrame(data=st.session_state.data, columns=main.columns[2:])

def save():
    df.to_csv("user-data.csv")

st.button(label="Save", on_click=save)
