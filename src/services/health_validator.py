import json
from pathlib import Path

class HealthValidator:

    def __init__(self):

        data_path = (
            Path(__file__)
            .parent.parent
            / "data"
            / "health_reference.json"
        )

        with open(
            data_path,
            "r"
        ) as f:

            self.reference = json.load(
                f
            )

def validate(
    self,
    metrics
):

    result = {}

    hba1c = metrics.get(
        "hba1c"
    )

    if hba1c is not None:

        if hba1c <= self.reference[
            "hba1c"
        ][
            "normal_max"
        ]:

            status = "Normal"

        elif hba1c <= self.reference[
            "hba1c"
        ][
            "prediabetic_max"
        ]:

            status = "Pre-Diabetic"

        else:

            status = "Diabetic"

        result["hba1c"] = {
            "value": hba1c,
            "status": status
        }

    fasting_glucose = metrics.get(
        "fasting_glucose"
    )

    if fasting_glucose is not None:

        if fasting_glucose <= self.reference[
            "fasting_glucose"
        ][
            "normal_max"
        ]:

            status = "Normal"

        elif fasting_glucose <= self.reference[
            "fasting_glucose"
        ][
            "prediabetic_max"
        ]:

            status = "Pre-Diabetic"

        else:

            status = "Diabetic"

        result[
            "fasting_glucose"
        ] = {
            "value":
            fasting_glucose,
            "status":
            status
        }

    ldl = metrics.get(
        "ldl"
    )

    if ldl is not None:

        if ldl <= self.reference[
            "ldl"
        ][
            "optimal_max"
        ]:

            status = "Optimal"

        elif ldl <= self.reference[
            "ldl"
        ][
            "borderline_max"
        ]:

            status = "Borderline High"

        else:

            status = "High"

        result["ldl"] = {
            "value": ldl,
            "status": status
        }

    return result
