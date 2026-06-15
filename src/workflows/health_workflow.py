import json

from langgraph.graph import (
    StateGraph,
    START,
    END
)

from workflows.health_state import HealthState
from utils.skill_loader import load_skill
from services.ai_service import AIService
from services.health_validator import HealthValidator

def metric_extraction_node(state: HealthState):
    ai_service = AIService()
    skill = load_skill("metric_extraction_skill.md")
    prompt = f"""

    {skill}

    Health Report:

    {state["report_text"]}
    """

    response = ai_service.generate_response(prompt)



    try:
        cleaned_response = (
            response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )
        metrics = json.loads(cleaned_response)
    except Exception as e:
        print(f"JSON Parse Error: {e}")
        metrics = {
            "hba1c": None,
            "ldl": None,
            "fasting_glucose": None,
        }

    return {"metrics": metrics}

def validation_node(
    state: HealthState
):

    validator = HealthValidator()

    validated_metrics = (
        validator.validate(
            state["metrics"]
        )
    )

    return {
        "validated_metrics":
        validated_metrics
    }

def analysis_node(state: HealthState):
    ai_service = AIService()
    skill = load_skill("analysis_skill.md")
    prompt = f"""
    {skill}

    Validated Metrics:

    {state["validated_metrics"]}
    """

    analysis = ai_service.generate_response(prompt)
    return {"analysis": analysis}


def risk_node(state: HealthState):
    ai_service = AIService()
    skill = load_skill("risk_skill.md")
    prompt = f"""

    {skill}

    Analysis Findings:

    {state["analysis"]}
    """

    risk_assessment = ai_service.generate_response(prompt)
    return {"risk_assessment": risk_assessment}


def recommendation_node(state: HealthState):
    ai_service = AIService()
    skill = load_skill("recommendation_skill.md")
    prompt = f"""
    ```

    {skill}

    Risk Assessment:

    {state["risk_assessment"]}
    """

    recommendations = ai_service.generate_response(prompt)
    return {"recommendations": recommendations}


def summary_node(state: HealthState):
    ai_service = AIService()
    skill = load_skill("summary_skill.md")
    prompt = f"""
    ```

    {skill}

    Analysis:

    {state["analysis"]}

    Risk Assessment:

    {state["risk_assessment"]}

    Recommendations:

    {state["recommendations"]}
    """

    summary = ai_service.generate_response(prompt)
    return {"summary": summary}


def build_workflow():
    graph = StateGraph(HealthState)

    graph.add_node("metric_extraction", metric_extraction_node)
    graph.add_node("validation",validation_node)
    graph.add_node("analysis", analysis_node)
    graph.add_node("risk", risk_node)
    graph.add_node("recommendation", recommendation_node)
    graph.add_node("summary", summary_node)

    graph.add_edge(START, "metric_extraction")
    graph.add_edge("metric_extraction","validation")
    graph.add_edge("validation","analysis")
    graph.add_edge("analysis", "risk")
    graph.add_edge("risk", "recommendation")
    graph.add_edge("recommendation", "summary")
    graph.add_edge("summary", END)

    return graph.compile()
