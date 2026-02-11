def normalize(text: str) -> str:
    return text.strip().lower()


def is_permanent_memory(text: str) -> bool:
    t = normalize(text)

    permanent_patterns = [
        "i prefer",
        "i like",
        "i speak",
        "my language is",
        "i want answers in",
        "i am comfortable with",
        "please respond in",
        "my preference is"
    ]

    return any(p in t for p in permanent_patterns)


def is_task_related(text: str) -> bool:
    t = normalize(text)

    task_keywords = [
        "hackathon",
        "project",
        "architecture",
        "design",
        "ppt",
        "presentation",
        "evaluation",
        "demo",
        "implementation",
        "system design"
    ]

    return any(k in t for k in task_keywords)


def is_forget_request(text: str) -> bool:
    t = normalize(text)

    forget_phrases = [
        "end this",
        "end the task",
        "stop this task",
        "close this task",
        "finish this discussion",
        "end session"
    ]

    return any(f in t for f in forget_phrases)


def is_audit_request(text: str) -> bool:
    t = normalize(text)

    audit_keywords = [
        "what do you remember",
        "what did you store",
        "show memory",
        "show stored data",
        "memory audit",
        "how is it stored",
        "show stored json"
    ]

    return any(k in t for k in audit_keywords)

