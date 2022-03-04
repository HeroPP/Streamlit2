import streamlit as st
from teamleaderApiV1.client import Client
import pandas as pd

data_load_state = st.text("haha")
tl = Client(
    api_group=st.secrets["teamleader_v1"]["api_group"],
    api_secret=st.secrets["teamleader_v1"]["api_secret"],
)

df = pd.DataFrame(tl.companies.list())
st.write(df)
