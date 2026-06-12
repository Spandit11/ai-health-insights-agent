from supabase import create_client
import streamlit as st


class AuthService:

    def __init__(self):

        self.client = create_client(
            st.secrets["SUPABASE_URL"],
            st.secrets["SUPABASE_ANON_KEY"]
        )

    def sign_up(self, email, password):

        return self.client.auth.sign_up(
            {
                "email": email,
                "password": password
            }
        )

    def sign_in(self, email, password):

        return self.client.auth.sign_in_with_password(
            {
                "email": email,
                "password": password
            }
        )

    def sign_out(self):

        self.client.auth.sign_out()