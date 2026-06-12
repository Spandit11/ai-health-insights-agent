import streamlit as st

from auth.auth_service import AuthService
from auth.session_manager import login_user


def render_login():

    st.subheader("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        try:

            auth = AuthService()

            auth.sign_in(email, password)

            login_user(email)

            st.success("Login successful")

            st.rerun()

        except Exception as ex:

            st.error(str(ex))


def render_signup():

    st.subheader("Create Account")

    email = st.text_input(
        "Signup Email",
        key="signup_email"
    )

    password = st.text_input(
        "Signup Password",
        type="password",
        key="signup_password"
    )

    if st.button("Create Account"):

        try:

            auth = AuthService()

            auth.sign_up(email, password)

            st.success(
                "Account created successfully"
            )

        except Exception as ex:

            st.error(str(ex))