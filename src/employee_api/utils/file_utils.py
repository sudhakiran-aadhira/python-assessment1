from typing import Any


def extract_nested_email(
    data: dict[str, Any]
) -> str | None:

    return (
        data
        .get("employee", {})
        .get("profile", {})
        .get("contact", {})
        .get("email")
    )