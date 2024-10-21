import streamlit as st
import time
from send_email import send_email


# Function to clear the message after a delay
def clear_message_after_delay(delay_seconds=5):
    time.sleep(delay_seconds)
    st.rerun()  # Rerun the app to clear the message


st.header('Contact Me')

with st.form(clear_on_submit=True, key='email_form'):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area('Your message')

    # Properly format the message
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
    """

    button = st.form_submit_button('Submit')

    if button:
        send_email(message)
        st.info("Your email was sent successfully")

        # Start a delay to clear the message after a few seconds
        clear_message_after_delay(delay_seconds=5)
