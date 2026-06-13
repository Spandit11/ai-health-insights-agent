import streamlit as st

from components.header import render_header
from components.footer import render_footer
from components.sidebar import render_sidebar

from auth.session_manager import (
    initialize_session,
    logout_user
)

from components.auth_pages import (
    render_login,
    render_signup
)
from components.upload_page import (
    render_upload_page
)
from components.history_page import (
    render_history_page
)
from components.chat_page import (
    render_chat_page
)
# MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="AI Health Insights Agent",
    page_icon="🩺",
    layout="wide"
)

# Initialize session
initialize_session()

# ==========================
# Authentication Gate
# ==========================
if not st.session_state.authenticated:

    st.title("🩺 AI Health Insights Agent")

    tab1, tab2 = st.tabs(
        [
            "Login",
            "Sign Up"
        ]
    )

    with tab1:
        render_login()

    with tab2:
        render_signup()

    st.stop()

# ==========================
# Main Application
# ==========================
page = render_sidebar()

render_header()

if page == "Home":

    st.subheader("Welcome")

    st.success(
        f"Logged in as {st.session_state.user_email}"
    )

    if st.button("Logout"):

        logout_user()

        st.rerun()

    st.write("Upload and analyze health reports using AI.")

    # Status Cards
    col1, col2 = st.columns(2)

    with col1:
        st.info("📄 PDF Upload")

    with col2:
        st.info("🤖 AI Analysis")

    col3, col4 = st.columns(2)

    with col3:
        st.info("💬 RAG Chat")

    with col4:
        st.info("📈 Health Recommendations")

    # Roadmap
    with st.expander("🚀 Project Roadmap"):

        st.markdown("""
        **Phase 1** ✅ Foundation

        **Phase 2** 🔄 Authentication

        **Phase 3** 🔄 PDF Processing

        **Phase 4** 🔄 AI Analysis

        **Phase 5** 🔄 RAG Chat

        **Phase 6** 🔄 Multi-Agent Workflow
        """)
elif page == "Chat With Report":

    render_chat_page()
elif page == "About":

    st.subheader("About")

    st.write("""
    AI Health Insights Agent is an AI-powered platform for analyzing
    health reports and providing educational insights.

    Planned Technologies:
    - Streamlit
    - Groq
    - Supabase
    - LangChain
    - FAISS
    - Agentic AI
    """)

elif page == "Upload Report":
    render_upload_page()

elif page == "Analysis History":
   render_history_page()
render_footer()