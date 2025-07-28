import streamlit as st

if st.button("Home"):
    st.switch_page("index.py")
if st.button("Page 1"):
    st.switch_page("pages/st_demo.py")
if st.button("Dashboard"):
    st.switch_page("pages/dashboard.py")

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,  
a soft return is used for the next line.  

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)