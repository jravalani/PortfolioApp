import streamlit as st

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