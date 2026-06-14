from services.ai_service import AIService
from services.vector_service import VectorService

from config.prompts import CHAT_PROMPT


class ChatAgent:

    def __init__(self):

        self.ai_service = AIService()

        self.vector_service = VectorService()

    def build_knowledge_base(
        self,
        report_text
    ):

        self.vector_service.build_index(
            report_text
        )

    def ask(
        self,
        question
    ):

        search_result = (
            self.vector_service.search(
                question
            )
        )

        retrieved_chunks = (
            search_result["results"]
        )

        score = (
            search_result["score"]
        )
        print(f"Retrieval Score: {score}")
        # Confidence Threshold
        if score > 2.0:

            return {
                "answer":
                "I could not find this information in the uploaded report.",
                "sources": []
            }

        context = "\n\n".join(
            [
                chunk["content"]
                for chunk in retrieved_chunks
            ]
        )

        prompt = CHAT_PROMPT.format(
            context=context,
            question=question
        )

        answer = (
            self.ai_service.generate_response(
                prompt
            )
        )

        return {
            "answer": answer,
            "sources": [
                chunk["chunk_id"]
                for chunk in retrieved_chunks
            ]
        }