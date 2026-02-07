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

FORGET_KEYWORDS = [
    "forget this",
    "end this",
    "this is done",
    "you can forget",
    "no longer needed",
    "end this task"
]

def is_permanent_memory(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in PERMANENT_KEYWORDS)

def is_forget_request(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in FORGET_KEYWORDS)



def is_task_related(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in TASK_KEYWORDS)
