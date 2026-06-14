import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "src"
    )
)

from workflows.health_workflow import (
    build_workflow
)

workflow = build_workflow()

result = workflow.invoke(
    {
        "report_text":
        """
        HbA1c: 5.9%

        LDL: 165 mg/dL

        Fasting Glucose: 108 mg/dL
        """
    }
)

print("\n=== ANALYSIS ===\n")
print(
result["analysis"]
)

print("\n=== RISKS ===\n")
print(
result["risk_assessment"]
)
