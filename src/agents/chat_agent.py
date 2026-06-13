from services.ai_service import AIService
from services.vector_service import (
    VectorService
)

from config.prompts import (
    CHAT_PROMPT
)


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

        chunks = (
            self.vector_service.search(
                question
            )
        )

        context = "\n\n".join(
            chunks
        )

        prompt = CHAT_PROMPT.format(
            context=context,
            question=question
        )

        return self.ai_service.generate_response(
            prompt
        )