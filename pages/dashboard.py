# supabase.table("tablename").select("*").execute()
import streamlit as st
import pandas as pd
import numpy as np
# import altair as alt
import plotly
import os
from dotenv import load_dotenv
load_dotenv() 
from supabase import create_client, Client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

data = (supabase.table("prep_num").select("*").execute()).data

chart_data = pd.DataFrame(data)

st.line_chart(chart_data, x="year", y="prep_num")




data2 = (supabase.table("prep_num").select("*").execute()).data
# print(data)
preps = []
years = []

for record in data2:
    preps.append(record['prep_num'])
    years.append( str(record['year']) ) # str() converts the record to a string so you don't have to update the database column

chart_data2 = pd.DataFrame({'x': years, 'y': preps})

# st.altair_chart(alt.Chart(chart_data2).mark_line().encode(
#     x='x',
#     y='y'
# ))

display = plotly.graph_objects.Figure(
        data=plotly.graph_objects.Bar(y=preps, x=years, 
                    marker_color="blue"))

display

option = st.selectbox(
    "This is a demo select chart",
    ("Chart 1", "Chart 2"),
)

if (option == "Chart 1"):
    st.line_chart(chart_data, x="year", y="prep_num")
elif (option == "Chart 2"):
    print("temporary")
    # st.altair_chart(alt.Chart(chart_data2).mark_line().encode(
    #     x='x',
    #     y='y'
    # ))

if st.button("Home"):
    st.switch_page("index.py")
if st.button("Page 1"):
    st.switch_page("pages/st_demo.py")
if st.button("Dashboard"):
    st.switch_page("pages/dashboard.py")