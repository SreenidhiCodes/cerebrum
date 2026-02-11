def is_permanent_memory(text: str) -> bool:
    t = text.lower()
    permanent_keywords = [
        "i prefer",
        "i like",
        "i speak",
        "i usually",
        "my preference",
        "i want answers in",
        "i am comfortable with"
    ]
    return any(k in t for k in permanent_keywords)


def is_task_related(text: str) -> bool:
    t = text.lower()
    task_keywords = [
        "hackathon",
        "project",
        "design",
        "architecture",
        "ppt",
        "presentation",
        "evaluation",
        "demo",
        "final year",
        "college project",
        "system"
    ]
    return any(k in t for k in task_keywords)


def is_forget_request(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in [
        "end",
        "stop",
        "finish",
        "close this",
        "end this task"
    ])


def is_audit_request(text: str) -> bool:
    t = text.lower()
    audit_keywords = [
        "what do you remember",
        "what did you store",
        "show memory",
        "show stored",
        "how is it stored",
        "memory audit",
        "stored data"
    ]
    return any(k in t for k in audit_keywords)

