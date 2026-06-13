import streamlit as st

from services.database_service import (
    DatabaseService
)


def render_history_page():

    st.subheader(
        "📚 Analysis History"
    )

    db = DatabaseService()

    analyses = db.get_user_analyses(
        st.session_state.user_email
    )

    if not analyses:

        st.info(
            "No analyses found."
        )

        return

    for analysis in analyses:

        with st.expander(
            f"{analysis['file_name']} | {analysis['created_at']}"
        ):

            st.markdown(
                analysis["analysis_output"]
            )