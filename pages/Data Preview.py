import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.title("Data Preview")
df = st.session_state.df
AgGrid(df)

filtered_df = st.multiselect("Select columns to profile", options=list(df.columns), default=list(df.columns))

st.session_state.fdf = df[filtered_df]

profile_btn = st.button("Profile Data")

while profile_btn:
    switch_page("data profile report")
