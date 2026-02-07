import json
from datetime import datetime

PERM_MEMORY_PATH = "memorystore/permanentmemory.json"


class PermanentMemoryManager:
    def __init__(self):
        self._load()

    def _load(self):
        with open(PERM_MEMORY_PATH, "r") as f:
            self.data = json.load(f)

    def _save(self):
        with open(PERM_MEMORY_PATH, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_memory(self, content):
        memory = {
            "content": content,
            "created_at": datetime.utcnow().isoformat(),
            "confidence": 1.0
        }

        self.data["memories"].append(memory)
        self._save()

    def get_all_memories(self):
        return self.data["memories"]
