from supabase import create_client
import streamlit as st


class DatabaseService:

    def __init__(self):

        self.client = create_client(
            st.secrets["SUPABASE_URL"],
            st.secrets["SUPABASE_ANON_KEY"]
        )

    def save_analysis(
        self,
        user_email,
        file_name,
        report_text,
        analysis_output
    ):

        self.client.table(
            "analyses"
        ).insert(
            {
                "user_email": user_email,
                "file_name": file_name,
                "report_text": report_text,
                "analysis_output": analysis_output
            }
        ).execute()

    def get_user_analyses(
        self,
        user_email
    ):

        result = (
            self.client
            .table("analyses")
            .select("*")
            .eq("user_email", user_email)
            .order(
                "created_at",
                desc=True
            )
            .execute()
        )

        return result.data