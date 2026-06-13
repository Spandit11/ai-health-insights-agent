import streamlit as st

def render_sidebar():

    with st.sidebar:

        st.success(
            f"👤 {st.session_state.user_email}"
        )

        st.header("Navigation")

        page = st.radio(
            "Select",
            [
        "Home",
        "Upload Report",
        "About"
            ]
        )

        st.divider()
        st.caption("Version 1.0.0")

        return page