import json
import os
from datetime import datetime, timedelta

TEMP_MEMORY_PATH = "memorystore/temporarymemory.json"
TEMP_EXPIRY_DAYS = 30


class TemporaryMemoryManager:
    def __init__(self):
        self._ensure_storage()
        self._load()

    def _ensure_storage(self):
        if not os.path.exists("memorystore"):
            os.makedirs("memorystore")

        if not os.path.exists(TEMP_MEMORY_PATH):
            with open(TEMP_MEMORY_PATH, "w") as f:
                json.dump({
                    "counter": 0,
                    "active_memory_id": None,
                    "memories": {}
                }, f, indent=4)

    def _load(self):
        with open(TEMP_MEMORY_PATH, "r") as f:
            self.data = json.load(f)

    def _save(self):
        with open(TEMP_MEMORY_PATH, "w") as f:
            json.dump(self.data, f, indent=4)

    def has_active_memory(self):
        mem_id = self.data.get("active_memory_id")
        if not mem_id:
            return False

        memory = self.data["memories"].get(mem_id)
        if not memory:
            return False

        if datetime.utcnow() > datetime.fromisoformat(memory["expires_at"]):
            self.end_active_memory()
            return False

        return True

    def create_new_memory(self, initial_text, origin_turn):
        self.data["counter"] += 1
        mem_id = f"T{self.data['counter']}"

        self.data["active_memory_id"] = mem_id
        self.data["memories"][mem_id] = {
            "memory_id": mem_id,
            "type": "temporary",
            "content": [initial_text],
            "origin_turn": origin_turn,
            "created_at": datetime.utcnow().isoformat(),
            "expires_at": (
                datetime.utcnow() + timedelta(days=TEMP_EXPIRY_DAYS)
            ).isoformat(),
            "last_used_turn": origin_turn
        }

        self._save()
        return mem_id

    def append_to_active(self, text, turn_id):
        mem_id = self.data.get("active_memory_id")
        if not mem_id:
            return None

        memory = self.data["memories"].get(mem_id)
        if not memory:
            return None

        memory["content"].append(text)
        memory["last_used_turn"] = turn_id

        self._save()
        return mem_id

    def end_active_memory(self):
        self.data["active_memory_id"] = None
        self._save()

    def get_active_memory(self):
        mem_id = self.data.get("active_memory_id")
        if not mem_id:
            return None
        return self.data["memories"].get(mem_id)
