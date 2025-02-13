import streamlit as st
import requests
from aiohttp.web_routedef import options

st.title("Crypto Monitoring")
st.header("Find the latest Crypto price updates")

crypto = st.selectbox("Choose a cryptocurrency", options=
["", "Bitcoin","Litecoin","Ripple"])

if crypto == "Bitcoin":
    st.write("like 100k")