from services.ai_service import AIService
from config.prompts import (
    HEALTH_ANALYSIS_PROMPT
)


class AnalysisAgent:

    def __init__(self):

        self.ai_service = AIService()

    def analyze(self, report_text):

        prompt = HEALTH_ANALYSIS_PROMPT.format(
            report_text=report_text
        )

        return self.ai_service.generate_response(
            prompt
        )