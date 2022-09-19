import abc
from typing import List

import streamlit as st


class Page:

    @abc.abstractmethod
    def render(self):
        ...

class IntroPage(Page):
    def render(self):
        st.title("Intro")
        st.write("This is the intro page")

class FirstPageOfQuestions(Page):
    def render(self):
        st.write("We will have some questions here")



class Wizard:
    def __init__(self, pages: List[Page], initial_idx: int = 0):
        self.pages = pages

        if 'current_page' not in st.session_state:
            st.session_state['current_page'] = initial_idx

    @property
    def total_pages(self) -> int:
        return len(self.pages)

    @property
    def current_page(self):
        return st.session_state['current_page']

    @current_page.setter
    def current_page(self, new_page):
        if new_page <= (len(self.pages)-1):
            st.session_state['current_page'] = new_page
        else:
            raise ValueError("You're beyond the final page!")

        st.experimental_rerun()

    def go_to_previous_page(self):
        self.current_page -= 1

    def go_to_next_page(self):
        self.current_page += 1


    def render(self):
        with st.container():
            self.pages[self.current_page].render()
            self.progress_bar()
            self.buttons()

    def buttons(self):
        col1, _, col2 = st.columns((1, 7, 1))
        previous = col1.button("Previous")
        next_ = col2.button("Next ")

        if previous:
            self.go_to_previous_page()

        if next_:
            self.go_to_next_page()

    def progress_bar(self):

        _, col1, _ = st.columns((2,4,2))
        col1.progress(((self.current_page+1) / self.total_pages))