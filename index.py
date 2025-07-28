import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Centered Header", page_icon=":dart:", layout="wide")
# Centered header using HTML inside Markdown
st.markdown("<h1 style='text-align: center;'>:bar_chart: My Streamlit Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>An interactive data exploration app</h3>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

st.header("home page")
st.title("home page")

fig = go.Figure(
        data=go.Bar(y=[2, 3, 1], # replace with your own data source
                    marker_color="red"))
fig

if st.button("Home"):
    st.switch_page("index.py")
if st.button("Page 1"):
    st.switch_page("pages/st_demo.py")
if st.button("Dashboard"):
    st.switch_page("pages/dashboard.py")