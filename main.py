import components
import streamlit as st


st.markdown("<style>" + open("static/style.css").read() + "</style>", unsafe_allow_html=True)


intro = components.IntroPage()
data = components.FirstPageOfQuestions()

wizard = components.Wizard(pages=[intro, data])

wizard.render()