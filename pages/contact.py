import streamlit as st
import smtplib
from email.message import EmailMessage
import config



st.header('Contact Me')

def send_email(user_massage_box):
    print("send_email function has started")
    username = config.key_user_sender
    password = config.key_pass

    receiver = config.key_user_reciever
    email_message = EmailMessage()
    email_message["Subject"] = "New Clint"
    email_message.set_content("Hey, New Clint for ya.")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(username, receiver, user_message_box)
        server.quit()
    print("Email was Sent")



with st.form(key='email_form'):
    user_email = st.text_input('Enter your Email here')
    raw_message = st.text_area("Enter Message here")
    user_message_box = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""

    sumbit_button = st.form_submit_button('Enter')

    if sumbit_button:
        send_email(user_message_box)
        st.info('Email Sent')