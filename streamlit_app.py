import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("Birthday Card for Elaine")
st.write(
    "This is an Alert \n \n Elaine if you are reading this you are too old now! \n \nCongradulations you are one second older than the second before and since you are a slow reader you just lost so many second you could have done so much more just reading this. \n \nThank you for wasting your prescious time by reading this on your birthday \n Happy Birthday I guess from Lily and Fooj!")
st.balloons()
death_note = st.button("Press for your gift from Lily")
if death_note:
    st.write(
        "To eliminate your worst enemies and your closest allies \nSincerely, anonymous")
Fooj_note = st.button("Press for your gift from Fooj")
if Fooj_note:
    st.write("I wish you the very best! You are so talented, kind and sweet and I am sure you will achieve great things in your life. Do not forget me when you get all old and wrinkly. ")
