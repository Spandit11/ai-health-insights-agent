from typing import TypedDict


class HealthState(TypedDict):

    report_text: str

    metrics: dict

    validated_metrics: dict

    analysis: str

    risk_assessment: str

    recommendations: str

    summary: str