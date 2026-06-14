from pathlib import Path


def load_skill(
    skill_name: str
) -> str:

    skill_path = (
        Path(__file__)
        .parent.parent
        / "skills"
        / skill_name
    )

    return skill_path.read_text(
        encoding="utf-8"
    )