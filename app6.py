import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Dashboard",
                   layout= "wide")

st.title("Water Quality Data Dashboard")
st.subheader("Visualization TOol for Biscayne Bay Water Quality using Aquatic Robots")

st.sidebar.file_uploader("Choose a csv file")
st.sidebar.info("If no CSV file is uploaded, a default one will be displayed.")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("biscayne_bay_dataset_oct_2021-1.csv")

scatterPlot, linePlot, maps, threeDPlot, tables = st.tabs([
    "Correlation",
    "Line Chart",
    "Map",
    "3D Chart",
    "Tables"
])

with scatterPlot:
    st.subheader("Scatter Plots for the Water Parameters")
    fig = px.scatter(df,
                     x="Salinity (ppt)",
                     y="temperature (C)",
                     color = "ODO (mg/L")
    st.plotly_chart(fig)


