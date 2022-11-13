import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

fdf = st.session_state.fdf
pr = fdf.profile_report()
export = pr.to_html()

st_profile_report(pr)

st.download_button(label="Download HTML Report", data=export, file_name='Profile Report.html')
