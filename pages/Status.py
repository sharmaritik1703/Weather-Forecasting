import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("Model.h5", 'rb'))

st.title("Weather Forecasting System")

if 'app_data' not in st.session_state:
    st.session_state.app_data = np.zeros(shape=(1, 7))

{'Overcast': 0,
 'Mostly Cloudy': 1,
 'Partly Cloudy': 2,
 'Clear': 3,
 'Foggy': 4,
 'Breezy and Overcast': 5,
 'Breezy and Mostly Cloudy': 6,
 'Breezy and Partly Cloudy': 7,
 'Dry and Partly Cloudy': 8,
 'Windy and Partly Cloudy': 9,
 'Light Rain': 10,
 'Breezy': 11,
 'Windy and Overcast': 12,
 'Humid and Mostly Cloudy': 13,
 'Drizzle': 14,
 'Breezy and Foggy': 15,
 'Windy and Mostly Cloudy': 16,
 'Dry': 17,
 'Humid and Partly Cloudy': 18,
 'Dry and Mostly Cloudy': 19,
 'Rain': 20,
 'Windy': 21}

precipitation = {'rain': 0, 'snow': 1}

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)


with col1:
    st.session_state.app_data[0, 0] = precipitation[st.selectbox(label='Precipitation Type', options=precipitation.keys())]

with col2:
    st.session_state.app_data[0, 1] = st.slider(label='Temperature (C)', min_value=-10.0, max_value=40.0)

with col3:
    st.session_state.app_data[0, 2] = st.slider(label='Humidity', min_value=0.0, max_value=1.0)

with col4:
    st.session_state.app_data[0, 3] = st.slider(label='Wind Speed (kmph)', min_value=0.0, max_value=30.0)

with col5:
    st.session_state.app_data[0, 4] = st.slider(label='Wind Bearing (degrees)', min_value=0, max_value=400)

with col6:
    st.session_state.app_data[0, 5] = st.slider(label='Visibility (km)', min_value=0, max_value=16)

st.session_state.app_data[0, 6] = st.slider(label='Pressure (Millibars)', min_value=1000.00, max_value=1040.00)

@st.cache_data
def predict():
    value = model.predict(st.session_state.app_data)[0]
    result: str = ""

    for key in status.keys():
        if status[key] == value:
            result = key

    st.progress(value=100)
    st.subheader(body=result)

st.button(label="See Status", on_click=predict)
