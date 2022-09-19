import streamlit as st

from components import Page


class IntroPage(Page):
    def render(self) -> dict:
        st.title("Intro")
        st.write("This is the intro page")
        accept = st.radio("Do you understand that", options=['Yes', "No", "Can you repeat the question"])
        return dict(accept=accept)


class FirstPageOfQuestions(Page):
    def render(self) -> dict:
        st.title('Question Page')
        st.write("We will have some questions here")

        # We can access the other page state via session storage if we know what it is called
        # This is presumably not a very robust solution

        did_they_accept = st.session_state["page_state"]['intro']['accept']
        st.write(f"On the previous page you selected {did_they_accept}")
        fave_bean = st.selectbox("What is your favourite jelly bean colour", ['Red', 'Orange', 'Green'])
        return dict(fave_bean=fave_bean)
