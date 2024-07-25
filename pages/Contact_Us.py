import streamlit as st
from send_mail import send_mail

st.header("Contact Me")

with st.form(key="email_forms"):
    st.subheader("Email Address:")
    user_email = st.text_input(" ", placeholder="abc@google.com")
    st.subheader("Message")
    raw_message = st.text_area(" ", placeholder="Hello World")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
    """
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        print("Submit button was pressed!")
        send_mail(message)
        st.info("Your email was send successfully!")
