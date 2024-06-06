import streamlit as st
import pandas as pd

st.write('Hello World !')

# Session state:
# In streamlit, Session State is a way to share variables between reruns, for each user session.
# Stremalit gives the ability to store and persist the state, also ability to manipulate the state

# if 'key' not in st.session_state:
#     st.session_state['key'] = 'value'
#     st.session_state.key = 'value'



if "ship_key" not in st.session_state:
    st.session_state.ship_key = ''
    st.session_state.bill_key = ''

ship_ad = st.text_input("**Enter shipping Address**", key="ship_key")
chk = st.checkbox("Billing address same as shipping?", key="chk_key")
st.markdown("#")

if (chk is True) and ship_ad:
    bill_ad = st.text_input("**Enter billing address**", key="bill_key", value=st.session_state.ship_key)
    st.write(st.session_state.bill_key)
else:
    bill_ad = st.text_input("**Enter billing address**", key="bill_key")
    st.write(st.session_state.bill_key)


