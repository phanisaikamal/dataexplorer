import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

st.set_page_config(initial_sidebar_state="collapsed")

dataset = st.file_uploader("Choose a CSV file to upload")

start_btn = st.button("Start Exploration")

while dataset is not None and start_btn:
    st.session_state.df = pd.read_csv(dataset, delimiter=",")
    switch_page("data preview")
