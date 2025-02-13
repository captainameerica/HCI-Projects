from datetime import datetime

import streamlit as st
st.set_page_config(layout="wide")
st.title("My First Web App for HCI")
st.header("CAP 4104 - Human-Computer Interaction")
st.subheader("Prof. Geig Reis")
st.subheader("Hello huzz bruzz chuzz")

st.divider()

st.write("Registration Form")

first_name = st.text_input("Enter first name")
last_name = st.text_input("Enter last name")
yrofbrth = st.number_input("Enter year of birth")
fiuStrtyr = st.number_input("Enter first year at FIU")

current_year = datetime.date.today().year
age = current_year - yrofbrth
years_at_fiu = current_year - fiuStrtyr

if first_name and last_name and yrofbrth and fiuStrtyr:
    st.success(f"{first_name}, you are {age} years old, and you have "
               f" been working at FIU for {years_at_fiu} years.")