from model.main import process_input

print("\n---(Long-Form) Cerebrum Memory Demo---")
print("Type your messages below.")
print("Type 'exit' or 'quit' to end the demo.\n")
print("[System] Temporary memories auto-expire after 30 days unless ended earlier.\n")

while True:
    user_input = input("User: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("\n[System] Demo ended.")
        break

    process_input(user_input)
    
    memories = retrieve_relevant_memories()
    if memories:
        print("[System] Active Memories:")
        for mem in memories:
            print("   ", mem)
