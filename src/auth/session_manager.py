import streamlit as st


def initialize_session():

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if "user_email" not in st.session_state:
        st.session_state.user_email = None


def login_user(email):

    st.session_state.authenticated = True
    st.session_state.user_email = email


def logout_user():

    st.session_state.authenticated = False
    st.session_state.user_email = None