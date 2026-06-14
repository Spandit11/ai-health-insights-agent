from langgraph.graph import (
StateGraph,
START,
END
)

from workflows.health_state import (
HealthState
)

from utils.skill_loader import (
load_skill
)

from services.ai_service import (
AIService
)

def analysis_node(
state: HealthState
):


    ai_service = AIService()

    skill = load_skill(
        "analysis_skill.md"
    )

    prompt = f"""


        {skill}

        Health Report:

        {state["report_text"]}
        """


    analysis = (
        ai_service.generate_response(
            prompt
        )
    )

    return {
        "analysis": analysis
    }

def risk_node(
state: HealthState
):


    ai_service = AIService()

    skill = load_skill(
        "risk_skill.md"
    )

    prompt = f"""
    ```

    {skill}

    Analysis Findings:

    {state["analysis"]}
    """


    risk_assessment = (
        ai_service.generate_response(
            prompt
        )
    )

    return {
        "risk_assessment":
        risk_assessment
    }

def recommendation_node(
state: HealthState
):

    ai_service = AIService()

    skill = load_skill(
        "recommendation_skill.md"
    )

    prompt = f"""
    ```

    {skill}

    Risk Assessment:

    {state["risk_assessment"]}
    """


    recommendations = (
        ai_service.generate_response(
            prompt
        )
    )

    return {
        "recommendations":
        recommendations
    }

    def summary_node(
        state: HealthState
        ):

        ai_service = AIService()

        skill = load_skill(
            "summary_skill.md"
        )

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

        
        summary = (
            ai_service.generate_response(
                prompt
            )
        )

        return {
            "summary":
            summary
        }

def summary_node(
    state: HealthState
    ):


    ai_service = AIService()

    skill = load_skill(
        "summary_skill.md"
    )

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


    summary = (
        ai_service.generate_response(
            prompt
        )
    )

    return {
        "summary": summary
    }

def build_workflow():


    graph = StateGraph(
        HealthState
    )

    graph.add_node(
    "analysis",
    analysis_node
    )

    graph.add_node(
    "risk",
    risk_node
    )

    graph.add_node(
    "recommendation",
    recommendation_node
    )

    graph.add_node(
    "summary",
    summary_node
    )

    graph.add_edge(
    START,
    "analysis"
    )

    graph.add_edge(
    "analysis",
    "risk"
    )

    graph.add_edge(
    "risk",
    "recommendation"
    )

    graph.add_edge(
    "recommendation",
    "summary"
    )

    graph.add_edge(
    "summary",
    END
    )

    return graph.compile()
