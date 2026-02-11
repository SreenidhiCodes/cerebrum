from model.permanentmemorymanager import PermanentMemoryManager
from model.memorymanager import TemporaryMemoryManager


def retrieve_relevant_memories(current_turn):
    """
    Retrieve memories relevant at the current turn.

    Final Retrieval Policy:
    1. ALWAYS recall all Permanent Memories (P)
    2. ALSO recall Active Temporary Memory (T) if it exists

    Guarantees:
    - No memory hallucination
    - No inferred memory
    - Fully auditable by turn number
    """

    recalled = []

    perm = PermanentMemoryManager()
    temp = TemporaryMemoryManager()

    
    for mem in perm.get_all():
        mem["last_used_turn"] = current_turn
        recalled.append({
            "memory_id": mem["memory_id"],
            "type": "permanent",
            "key": mem["key"],
            "value": mem["value"],
            "origin_turn": mem["origin_turn"],
            "last_used_turn": mem["last_used_turn"]
        })

    
    perm._save()

    
    active_id = temp.data.get("active_memory_id")

    if active_id:
        active_mem = temp.data["memories"].get(active_id)
        if active_mem:
            active_mem["last_used_turn"] = current_turn
            temp._save()

            recalled.append({
                "memory_id": active_mem["memory_id"],
                "type": "temporary",
                "content": active_mem["content"],
                "origin_turn": active_mem["origin_turn"],
                "last_used_turn": active_mem["last_used_turn"]
            })

    return recalled

