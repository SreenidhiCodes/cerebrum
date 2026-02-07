from model.memorymanager import TemporaryMemoryManager
from model.permanentmemorymanager import PermanentMemoryManager
from model.memoryclassifier import is_permanent_memory, is_task_related
from model.retriever import retrieve_relevant_memories


def process_input(user_text: str):
    temp_manager = TemporaryMemoryManager()
    perm_manager = PermanentMemoryManager()

     
    if is_forget_request(user_text) and temp_manager.has_active_memory():
        temp_manager.end_active_memory()
        print("[System] Temporary memory ended")
        return
    
    if is_permanent_memory(user_text):
        perm_manager.add_memory(user_text)
        print("[System] Stored as PERMANENT memory")
        return

   
        
    if is_task_related(user_text):
        if not temp_manager.has_active_memory():
            mem_id = temp_manager.create_new_memory(user_text)
            print(f"[System] New temporary memory created: #{mem_id}")
        else:
            active_id = temp_manager.data["active_memory_id"]
            last_entry = temp_manager.data["memories"][active_id]["content"][-1]

            if is_same_topic(user_text, last_entry):
                temp_manager.append_to_active(user_text)
                print("[System] Appended to active temporary memory")
            else:
                mem_id = temp_manager.create_new_memory(user_text)
                print(f"[System] New temporary memory created: #{mem_id}")

