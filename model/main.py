import json
from model.memoryclassifier import (
    is_permanent_memory,
    is_task_related,
    is_forget_request,
    is_audit_request
)
from model.permanentmemorymanager import PermanentMemoryManager
from model.memorymanager import TemporaryMemoryManager
from model.retriever import retrieve_relevant_memories

SESSION_PATH = "memorystore/session.json"


def get_next_turn():
    with open(SESSION_PATH, "r") as f:
        data = json.load(f)

    data["current_turn"] += 1

    with open(SESSION_PATH, "w") as f:
        json.dump(data, f, indent=4)

    return data["current_turn"]


def process_input(user_text: str):
    turn_id = get_next_turn()

    perm = PermanentMemoryManager()
    temp = TemporaryMemoryManager()

    if is_forget_request(user_text) and temp.has_active_memory():
        temp.end_active_memory()
        return {
            "turn": turn_id,
            "event": "temporary_memory_ended"
        }

    if is_audit_request(user_text):
        recalled = retrieve_relevant_memories(turn_id)
        return {
            "turn": turn_id,
            "audit": recalled
        }

    if is_permanent_memory(user_text):
        mem_id, _ = perm.add_memory(user_text, turn_id)
        return {
            "turn": turn_id,
            "event": "permanent_memory_stored",
            "memory_id": mem_id
        }

    if is_task_related(user_text):
        if not temp.has_active_memory():
            mem_id = temp.create_new_memory(user_text, turn_id)
            return {
                "turn": turn_id,
                "event": "temporary_memory_started",
                "memory_id": mem_id
            }
        else:
            mem_id = temp.append_to_active(user_text, turn_id)
            note = ""
            active = temp.get_active_memory()
            if active.get("reason") == "overflow":
                note = "continuation of previous task memory (overflow)"
            return {
                "turn": turn_id,
                "event": "temporary_memory_updated",
                "memory_id": mem_id,
                "note": note
            }

    recalled = retrieve_relevant_memories(turn_id)
    if recalled:
        ids = " | ".join(
            f"{m['memory_id']}" for m in recalled
        )
        return {
            "turn": turn_id,
            "event": "memory_recalled",
            "details": f"Turn {turn_id} → {ids} recalled"
        }

    return {
        "turn": turn_id,
        "event": "no_memory_action"
    }

                print("[System] Appended to active temporary memory")
            else:
                mem_id = temp_manager.create_new_memory(user_text)
                print(f"[System] New temporary memory created: #{mem_id}")

