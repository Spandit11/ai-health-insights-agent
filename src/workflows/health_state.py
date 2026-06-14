from typing import TypedDict


class HealthState(TypedDict):

    report_text: str

    analysis: str

    risk_assessment: str

    recommendations: str

    summary: str