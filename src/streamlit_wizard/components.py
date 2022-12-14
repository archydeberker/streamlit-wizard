import abc
from collections import defaultdict
from typing import List

import streamlit as st

from src.streamlit_wizard.style import inject_style


class Page:
    def __init__(self, name: str):
        """
        `name` is the id which we will use to store this page's state
        """
        self.name = name
        inject_style()

    @abc.abstractmethod
    def render(self) -> dict:
        """Render the page, returning any state in a dictionary which will be stored
        in the session state"""
        ...


class Wizard:
    def __init__(self, pages: List[Page], initial_idx: int = 0,
                 display_page_count: bool = True):

        self.pages = pages
        self.display_page_count = display_page_count
        inject_style()

        if len(set([page.name for page in pages])) != len(self.pages):
            raise ValueError(
                "Please give your pages unique names, otherwise we cannot store "
                "the state for each page reliably in a dict"
            )

        if "current_page_idx" not in st.session_state:
            st.session_state["current_page_idx"] = initial_idx

        if "page_state" not in st.session_state:
            st.session_state["page_state"] = defaultdict(lambda: dict())

    @property
    def total_pages(self) -> int:
        return len(self.pages)

    @property
    def current_page_idx(self):
        return st.session_state["current_page_idx"]

    @current_page_idx.setter
    def current_page_idx(self, new_page):
        if 0 <= new_page <= (len(self.pages) - 1):
            st.session_state["current_page_idx"] = new_page

        st.experimental_rerun()

    @property
    def current_page(self):
        return self.pages[self.current_page_idx]

    @property
    def on_final_page(self) -> bool:
        return self.current_page_idx == (self.total_pages - 1)

    def go_to_previous_page(self):
        self.current_page_idx -= 1

    def go_to_next_page(self):
        self.current_page_idx += 1

    def store_current_page_state(self, state: dict):
        st.session_state["page_state"][self.current_page.name] = state

    def render(self):
        with st.container():
            state = self.current_page.render()
            self.store_current_page_state(state)
            self.progress_bar()
            self.buttons()

    def buttons(self):
        col1, _, col2 = st.columns((1, 7, 1))
        previous = col1.button("Previous")

        if self.on_final_page:
            next_ = col2.button("Finish")
        else:
            next_ = col2.button("Next ")

        if previous:
            self.go_to_previous_page()

        if next_:
            self.go_to_next_page()

    def progress_bar(self):

        _, col1, _ = st.columns((2, 4, 2))
        if self.display_page_count:
            col1.markdown(
                f'<div class="custom_centred"> This is page {self.current_page_idx + 1} of {self.total_pages} <div>',
                unsafe_allow_html=True)

        col1.write("")
        col1.progress(((self.current_page_idx + 1) / self.total_pages))
