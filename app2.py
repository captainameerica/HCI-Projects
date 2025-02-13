import streamlit as st

st.set_page_config(page_title="Registration",
                   page_icon="🤫"
                   )
st.title("Party Registration")
st.header("Come celebrate DD 25th anniversary")
st.subheader("what up")
st.sidebar.title("Contact")
st.sidebar.subheader("We want you at the party 😈😈")
cntctOptns = st.sidebar.selectbox("How do you want to be contacted?",
                     options=["","email", "call", "text"])

if cntctOptns:
    st.sidebar.success(f"We will be {cntctOptns}ing u 😍")

with st.form("Registration", clear_on_submit=True):
    name = st.text_input("what is your name, unc?",placeholder="First and Last name")
    age = st.number_input("How old are you, unc? 😂",min_value=1,step=1)
    emailadrss = st.text_input("Enter email Address",placeholder="email@company.com")
    major = st.selectbox("what is your major",options=[
        "","CS","Gender Studies"
    ])
    level = st.selectbox("whats your degree", options=[
        "", "Undergraduate","Masters","Phd"
    ])
    subscribe = st.checkbox("would you like to hear about future parties")
    submit = st.form_submit_button("Submit!❤️")
    if