import json
import os
from datetime import datetime, timedelta

TEMP_MEMORY_PATH = "memorystore/temporarymemory.json"
TEMP_EXPIRY_DAYS = 30


class TemporaryMemoryManager:
    def __init__(self):
        self._load()

    def _load(self):
        with open(TEMP_MEMORY_PATH, "r") as f:
            self.data = json.load(f)

    def _save(self):
        with open(TEMP_MEMORY_PATH, "w") as f:
            json.dump(self.data, f, indent=4)

    def has_active_memory(self):
        return self.data["active_memory_id"] is not None

    def create_new_memory(self, initial_text):
        self.data["counter"] += 1
        mem_id = f"T{self.data['counter']}"

        self.data["active_memory_id"] = mem_id
        self.data["memories"][mem_id] = {
            "content": [initial_text],
            "created_at": datetime.utcnow().isoformat(),
            "expires_at": (
                datetime.utcnow() + timedelta(days=TEMP_EXPIRY_DAYS)
            ).isoformat()
        }

        self._save()
        return mem_id

    def append_to_active(self, text):
        mem_id = self.data["active_memory_id"]
        if not mem_id:
            return None

        self.data["memories"][mem_id]["content"].append(text)
        self._save()
        return mem_id

    def end_active_memory(self):
        self.data["active_memory_id"] = None
        self._save()

    def cleanup_expired(self):
        now = datetime.utcnow()
        expired = []

        for mem_id, mem in self.data["memories"].items():
            if datetime.fromisoformat(mem["expires_at"]) < now:
                expired.append(mem_id)

        for mem_id in expired:
            del self.data["memories"][mem_id]
            if self.data["active_memory_id"] == mem_id:
                self.data["active_memory_id"] = None

        self._save()

