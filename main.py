import streamlit as st

import components
import example_pages

st.markdown(
    "<style>" + open("static/style.css").read() + "</style>", unsafe_allow_html=True
)

intro = example_pages.IntroPage(name="intro")
data = example_pages.FirstPageOfQuestions(name="questions")

wizard = components.Wizard(pages=[intro, data])

wizard.render()
