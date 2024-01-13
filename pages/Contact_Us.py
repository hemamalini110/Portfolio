import streamlit as sl
from send_email import send_email
sl.header("Contact Me")

with sl.form(key="email_form"):
    user_email = sl.text_input("Your email address")
    raw_message = sl.text_area("Your message")
    SUBJECT= f"New email from {user_email}"

    message = 'Subject: {}\n\n{}'.format(SUBJECT, raw_message)
    submit_btn =sl.form_submit_button("Submit")
    if submit_btn:
        send_email(message)
        sl.info("Email sent Successfully")