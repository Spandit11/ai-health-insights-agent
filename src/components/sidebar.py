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

        st.divider()
        st.caption("Version 1.0.0")

        return page