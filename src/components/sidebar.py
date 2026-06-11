import streamlit as st

def render_sidebar():

    with st.sidebar:

        st.header("Navigation")

        page = st.radio(
            "Select",
            [
                "Home",
                "About"
            ]
        )

        return page