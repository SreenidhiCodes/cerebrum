import json
import os

PERM_MEMORY_PATH = "memorystore/permanentmemory.json"


class PermanentMemoryManager:
    def __init__(self):
        self._ensure_storage()
        self._load()

    def _ensure_storage(self):
        if not os.path.exists("memorystore"):
            os.makedirs("memorystore")

        if not os.path.exists(PERM_MEMORY_PATH):
            with open(PERM_MEMORY_PATH, "w") as f:
                json.dump({
                    "counter": 0,
                    "memories": []
                }, f, indent=4)

    def _load(self):
        with open(PERM_MEMORY_PATH, "r") as f:
            self.data = json.load(f)

        # Safety check
        if "counter" not in self.data:
            self.data["counter"] = 0
        if "memories" not in self.data:
            self.data["memories"] = []

    def _save(self):
        with open(PERM_MEMORY_PATH, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_memory(self, text, origin_turn):
        key, value = self._extract_preference(text)
        if not key:
            return None, None

        for mem in self.data["memories"]:
            if mem["key"] == key:
                old_turn = mem["origin_turn"]
                mem["value"] = value
                mem["last_used_turn"] = origin_turn
                self._save()
                return mem["memory_id"], old_turn

        self.data["counter"] += 1
        mem_id = f"P{self.data['counter']}"

        memory = {
            "memory_id": mem_id,
            "type": "permanent",
            "key": key,
            "value": value,
            "origin_turn": origin_turn,
            "last_used_turn": origin_turn
        }

        self.data["memories"].append(memory)
        self._save()
        return mem_id, None

    def mark_used(self, memory_id, turn_id):
        for mem in self.data["memories"]:
            if mem["memory_id"] == memory_id:
                mem["last_used_turn"] = turn_id
                self._save()
                return True
        return False

    def get_all(self):
        return self.data.get("memories", [])

    def _extract_preference(self, text):
        t = text.lower()

        if any(p in t for p in ["prefer telugu", "speak telugu", "telugu language"]):
            return "language", "Telugu"

        if any(p in t for p in ["prefer english", "speak english", "english language"]):
            return "language", "English"

        if "short answers" in t or "keep it short" in t:
            return "response_style", "short"

        if "detailed answers" in t or "explain in detail" in t:
            return "response_style", "detailed"

        return None, None

