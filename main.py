import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Jay Ravalani")
    content = """
    Data engineering enthusiast with a Bachelor's in Information Technology, specializing in ETL pipelines and big data analytics.
    Proficient in Python, SQL, and AWS, with hands-on experience in developing data-driven solutions using Apache Airflow and PySpark.
    Recent graduate of IBM's Data Engineering Specialization, eager to apply technical skills and analytical mindset to solve complex data challenges in a professional setting.
    """
    st.info(content)

st.write("Below you can find some of the apps I have build in Python. Feel free to contact me!")

col3, col4 = st.columns(2)


df = pd.read_csv("data.csv", sep=";")
with col3:
    for index, x in df[:10].iterrows():
        st.header(x["title"])

with col4:
    for index, x in df[10:].iterrows():
        st.header(x["title"])
