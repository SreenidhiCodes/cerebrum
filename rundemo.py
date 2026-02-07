from model.main import process_input

conversation = [
    "I am participating in the Neuro Challenge hackathon",
    "It requires a PPT submission",
    "The deadline is next week",
    "Now help me prepare for my exam"
]

for msg in conversation:
    print(f"\nUser: {msg}")
    process_input(msg)

