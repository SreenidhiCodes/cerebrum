from model.permanentmemorymanager import PermanentMemoryManager
from model.memorymanager import TemporaryMemoryManager


def retrieve_relevant_memories(current_turn):
    """
    Retrieval Policy:
    1. Always recall all Permanent Memories (P)
    2. Recall Active Temporary Memory (T) if valid
    3. Update last_used_turn safely via manager APIs
    """

    recalled = []

    perm = PermanentMemoryManager()
    temp = TemporaryMemoryManager()

   
    for mem in perm.get_all():
        perm.mark_used(mem["memory_id"], current_turn)

        recalled.append({
            "memory_id": mem["memory_id"],
            "type": "permanent",
            "origin_turn": mem["origin_turn"],
            "last_used_turn": current_turn
        })

    
    if temp.has_active_memory():
        active_mem = temp.get_active_memory()

        if active_mem:
            active_mem["last_used_turn"] = current_turn
            temp._save()

            recalled.append({
                "memory_id": active_mem["memory_id"],
                "type": "temporary",
                "origin_turn": active_mem["origin_turn"],
                "last_used_turn": current_turn
            })

    return recalled

