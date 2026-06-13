import streamlit as st


def render_chat_page():

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    st.subheader("💬 Chat With Report")

    st.info(
        "⚠️ Educational purposes only. Consult a healthcare professional for medical advice."
    )

    if "chat_agent" not in st.session_state:

        st.warning(
            "Please upload a report first."
        )

        return

    question = st.text_input(
        "Ask a question about your report"
    )

    if st.button(
        "Ask",
        key="ask_btn"
    ) and question:

        with st.spinner(
            "Searching report..."
        ):

            result = (
                st.session_state["chat_agent"]
                .ask(question)
            )

            response = result["answer"]

            sources = result["sources"]

            st.session_state[
                "chat_history"
            ].append(
                {
                    "question": question,
                    "answer": response,
                    "sources": sources
                }
            )

    # Display Chat History
    if st.session_state["chat_history"]:

        st.markdown("### Conversation")

        for item in reversed(
            st.session_state["chat_history"]
        ):

            st.markdown(
                f"**You:** {item['question']}"
            )

            st.markdown(
                f"**AI:** {item['answer']}"
            )

            st.caption(
                f"Sources: {item['sources']}"
            )

            st.divider()

    # Clear Chat Button
    if st.button(
        "Clear Chat",
        key="clear_chat_btn"
    ):

        st.session_state[
            "chat_history"
        ] = []

        st.rerun()