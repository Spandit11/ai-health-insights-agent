import streamlit as st

from utils.validators import validate_pdf
from utils.pdf_extractor import extract_text_from_pdf
from agents.analysis_agent import AnalysisAgent
from services.database_service import DatabaseService
from agents.chat_agent import ChatAgent

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
                if "chat_agent" not in st.session_state:

                   chat_agent = ChatAgent()

                chat_agent.build_knowledge_base(
                        extracted_text
                    )

                st.session_state["chat_agent"] = chat_agent

                st.success(
                            "Report processed successfully. You can now chat with your report."
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
                db = DatabaseService()

            db.save_analysis(
                user_email=st.session_state.user_email,
                file_name=uploaded_file.name,
                report_text=st.session_state["report_text"],
                analysis_output=analysis
            )

            st.subheader(
                "AI Health Insights"
            )

            st.markdown(analysis)