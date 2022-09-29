from pathlib import Path

import streamlit as st

this_file = Path(__name__)

style = """
div.css-1n76uvr.e1tzin5v0{
    border-radius: 10px;
    padding: 10px;
    border: 1px solid darkgray;
}

div.custom_centred {
    text-align: center;
}
"""


def inject_style():
    """Reads a local stylesheet and injects it"""
    st.markdown(
        "<style>" + style + "</style>", unsafe_allow_html=True
    )
