from model.memorymanager import TemporaryMemoryManager
from model.memoryclassifier import should_create_temp_memory


def process_input(user_text: str):
    manager = TemporaryMemoryManager()

    if should_create_temp_memory(user_text, manager.has_active_memory()):
        mem_id = manager.create_new_memory(user_text)
        print(f"[System] New temporary memory created: #{mem_id}")

    elif manager.has_active_memory():
        manager.append_to_active(user_text)
        print("[System] Appended to active temporary memory")

    else:
        print("[System] No memory stored")

