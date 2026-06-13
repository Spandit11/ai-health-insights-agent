import streamlit as st


def render_chat_page():

    st.subheader("💬 Chat With Report")

    if "chat_agent" not in st.session_state:

        st.warning(
            "Please upload a report first."
        )

        return

    question = st.text_input(
        "Ask a question about your report"
    )

    if st.button("Ask") and question:

        with st.spinner("Searching report..."):

            response = (
                st.session_state["chat_agent"]
                .ask(question)
            )

        st.markdown("### Answer")

        st.write(response)