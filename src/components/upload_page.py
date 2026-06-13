import streamlit as st

from utils.validators import validate_pdf
from utils.pdf_extractor import extract_text_from_pdf
from agents.analysis_agent import AnalysisAgent

def render_upload_page():

    st.subheader("📄 Upload Health Report")

    uploaded_file = st.file_uploader(
        "Choose a PDF report",
        type=["pdf"]
    )

    if uploaded_file:

        is_valid, message = validate_pdf(
            uploaded_file
        )

        if not is_valid:

            st.error(message)
            return

        st.success(message)

        if st.button("Extract Text"):

            with st.spinner(
                "Extracting text..."
            ):

                extracted_text = (
                    extract_text_from_pdf(
                        uploaded_file
                    )
                )
                st.session_state["report_text"] = (
                 extracted_text
                )

            st.success(
                "Text extracted successfully"
            )

            st.text_area(
                "Extracted Text",
                extracted_text,
                height=400
            )
                
        if "report_text" in st.session_state:

         if st.button("🤖 Analyze Report"):

            with st.spinner(
                "Analyzing report..."
            ):

                agent = AnalysisAgent()

                analysis = agent.analyze(
                    st.session_state["report_text"]
                )

            st.subheader(
                "AI Health Insights"
            )

            st.markdown(analysis)