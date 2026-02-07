from model.permanentmemorymanager import PermanentMemoryManager
from model.memorymanager import TemporaryMemoryManager


def retrieve_relevant_memories():
    perm = PermanentMemoryManager()
    temp = TemporaryMemoryManager()

    memories = []

    # Permanent memories
    for mem in perm.get_all_memories():
        memories.append(f"[PERMANENT] {mem['content']}")

    # Active temporary memory
    if temp.has_active_memory():
        mem_id = temp.data["active_memory_id"]
        content = temp.data["memories"][mem_id]["content"]
        memories.append(f"[TEMPORARY #{mem_id}] " + " | ".join(content))

    return memories

