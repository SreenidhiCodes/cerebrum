TASK_KEYWORDS = [
    "hackathon",
    "competition",
    "project",
    "assignment",
    "ppt",
    "presentation",
    "exam",
    "submission",
    "deadline"
]


def is_task_related(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in TASK_KEYWORDS)


def should_create_temp_memory(text: str, has_active: bool) -> bool:
    return is_task_related(text) and not has_active

