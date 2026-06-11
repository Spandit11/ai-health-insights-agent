import streamlit as st

from components.header import render_header
from components.footer import render_footer
from components.sidebar import render_sidebar

st.set_page_config(
    page_title="AI Health Insights Agent",
    page_icon="🩺",
    layout="wide"
)

page = render_sidebar()

render_header()

if page == "Home":

    st.subheader("Welcome")

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

render_footer()