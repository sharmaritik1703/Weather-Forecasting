import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_icon="⚙️")

st.title("Data Input")
directions = {'E': 0, 'W': 1, 'N': 2, 'S': 3, 'NE': 4, 'SE': 5, 'NW': 6, 'SW': 7}

if 'data' not in st.session_state:
    st.session_state.data = np.zeros(shape=(1, 10))

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, col8 = st.columns(2)
col9, col10 = st.columns(2)

with col1:
    st.session_state.data[0, 0] = st.slider(label="Average Temperature", min_value=-8.00, max_value=30.00)

with col2:
    st.session_state.data[0, 1] = st.slider(label="Max. Temperature", min_value=-5.00, max_value=40.00)

with col3:
    st.session_state.data[0, 2] = st.slider(label="Min. Temperature", min_value=-13.00, max_value=24.50)

with col4:
    st.session_state.data[0, 3] = st.slider(label="Precipitation", min_value=0.00, max_value=166.00)

with col5:
    st.session_state.data[0, 4] = st.slider(label="Avg. Wind Speed", min_value=0.10, max_value=6.00)

with col6:
    st.session_state.data[0, 5] = st.slider(label="Max. Wind Speed", min_value=0.80, max_value=12.70)

with col7:
    wsd = st.selectbox(label="Max. Wind Speed Direction", options=directions.keys())
    st.session_state.data[0, 6] = directions[wsd]

with col8:
    st.session_state.data[0, 7] = st.slider(label="Max. Inst. Wind Speed ", min_value=1.80, max_value=21.50)

with col9:
    msd = st.selectbox(label="Max. Inst. Wind Speed Direction", options=directions.keys())
    st.session_state.data[0, 8] = directions[msd]

with col10:
    st.session_state.data[0, 9] = st.slider(label="Min. Atmospheric Pressure", min_value=1009.00, max_value=1030.00)

main = pd.read_csv("weather_test.csv")
df = pd.DataFrame(data=st.session_state.data, columns=main.columns[2:])

def save():
    df.to_csv("user-data.csv")

st.button(label="Save", on_click=save)
