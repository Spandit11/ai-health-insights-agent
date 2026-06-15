import streamlit as st

from utils.validators import validate_pdf
from utils.pdf_extractor import extract_text_from_pdf
from agents.analysis_agent import AnalysisAgent
from services.database_service import DatabaseService
from agents.chat_agent import ChatAgent
from workflows.health_workflow import build_workflow


def render_upload_page():
    st.subheader("📄 Upload Health Report")

    uploaded_file = st.file_uploader("Choose a PDF report", type=["pdf"])

    if uploaded_file:
        is_valid, message = validate_pdf(uploaded_file)

        if not is_valid:
            st.error(message)
            return

        st.success(message)

        if st.button("Extract Text"):
            with st.spinner("Extracting text..."):
                extracted_text = extract_text_from_pdf(uploaded_file)
                st.session_state["report_text"] = extracted_text

                if "chat_agent" not in st.session_state:
                    st.session_state["chat_agent"] = ChatAgent()

                chat_agent = st.session_state["chat_agent"]
                chat_agent.build_knowledge_base(extracted_text)

                st.success("Report processed successfully. You can now chat with your report.")

            st.success("Text extracted successfully")
            st.text_area("Extracted Text", extracted_text, height=400)

        if "report_text" in st.session_state:
            if st.button("🤖 Analyze Report"):
                with st.spinner("Analyzing report..."):
                    workflow = build_workflow()
                    result = workflow.invoke({
                        "report_text": st.session_state["report_text"]
                    })
                    st.session_state["workflow_result"] = result
                    db = DatabaseService()
                    db.save_analysis(
                        user_email=st.session_state.user_email,
                        file_name=uploaded_file.name,
                        report_text=st.session_state["report_text"],
                        analysis_output=result["summary"],
                    )

            if "workflow_result" in st.session_state:
                result = st.session_state["workflow_result"]

                st.subheader("📊 Analysis")
                st.markdown(result["analysis"])

                st.subheader("⚠️ Risk Assessment")
                st.markdown(result["risk_assessment"])

                st.subheader("💡 Recommendations")
                st.markdown(result["recommendations"])

                st.subheader("📝 Summary")
                st.markdown(result["summary"])

                st.subheader("📈 Validated Metrics")
                st.json(result["validated_metrics"])
