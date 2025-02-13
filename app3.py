import streamlit as st

st.title("Temp Converter")

def convertFtoC(temp):
    return(float(temp)-32.) *5./9.

def convertCtoF(temp):
    return (float(temp)*9./5.)+32.

temp_input = st.slider("Select a temperature value",min_value=-100,max_value=200,value=32)

conv_type = st.radio("select a conversion type",options =[ "F to C",
                     "C to F"])
if conv_type == "F to C":
    output = convertFtoC(temp_input)
    st.metric(label="Converted Temperature",value=f"{output:.2f} C")


elif conv_type == "C to F":
    output = convertCtoF(temp_input)
    st.metric(label="Converted Temperature",value=f"{output:.2f} F")

if "history" not in st.session_state:
    st.session_state.history = []

st.session_state.history.append((temp_input,conv_type,output))
print(st.session_state.history)

st.divider()
history_data = st.session.state.history

rev = list(reversed(st.session_state.history))
st.subheader("Conversion History")

for i,(t,c,o) in enumerate(rev,1):
    st.write(f"{i}, {t} ({c}) -> {output}")

