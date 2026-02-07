PERMANENT_KEYWORDS = [
    "i prefer",
    "i like",
    "always",
    "from now on",
    "my name is",
    "i am a",
    "never"
]

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


def is_permanent_memory(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in PERMANENT_KEYWORDS)


def is_task_related(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in TASK_KEYWORDS)
