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

    st.write(
        """
        Upload and analyze health reports using AI.

        Upcoming Features:
        - PDF Upload
        - Report Analysis
        - RAG Chat
        - Health Recommendations
        """
    )

elif page == "About":

    st.subheader("About")

    st.write(
        """
        AI Health Insights Agent is an AI-powered platform
        for analyzing health reports and providing educational insights.
        """
    )

render_footer()