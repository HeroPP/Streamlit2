import streamlit as st
from teamleaderApiV1.client import Client
import pandas as pd
from teamleader import Client as TL2

tl2 = TL2(
    client_id=st.secrets["teamleader_v2"]["client_id"],
    client_secret=st.secrets["teamleader_v2"]["client_secret"],
    teamleader_token_file_name=st.secrets["teamleader_v2"][
        "teamleader_token_file_name"
    ],
)
df2 = pd.DataFrame(tl2.companies.list())
st.write(df2)

data_load_state = st.text("haha")
tl = Client(
    api_group=st.secrets["teamleader_v1"]["api_group"],
    api_secret=st.secrets["teamleader_v1"]["api_secret"],
)

df = pd.DataFrame(tl.companies.list())
st.write(df)
