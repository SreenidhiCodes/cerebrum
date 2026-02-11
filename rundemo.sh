#!/bin/bash


echo "CEREBRUM MEMORY ENGINE - END TO END DEMO"

echo ""

echo "[1] Resetting Memory Store..."

rm -f memorystore/permanentmemory.json
rm -f memorystore/temporarymemory.json
rm -f memorystore/session.json

mkdir -p memorystore

echo '{ "counter": 0, "memories": [] }' > memorystore/permanentmemory.json
echo '{ "counter": 0, "active_memory_id": null, "memories": {} }' > memorystore/temporarymemory.json
echo '{ "current_turn": 0 }' > memorystore/session.json

echo "Memory reset complete."
echo ""
echo "[2] Running 48-Turn Conversation Demo..."
echo ""

python - <<EOF
from model.main import process_input

conversation = [
"I prefer Telugu for explanations.",
"Let us start the hackathon project discussion.",
"We need to decide the problem statement first.",
"The problem should be related to AI or systems, right?",
"I’m thinking about building a memory system for chatbots.",
"Something that remembers important things but not everything.",
"Most chatbots forget context after some time.",
"And some store too much unnecessary information.",
"We need a balance between the two.",
"Let us define what permanent memory means.",
"Permanent memory should be like user preferences.",
"For example, language choice or response style.",
"Temporary memory can be about the current task.",
"Like this hackathon discussion.",
"So hackathon becomes one temporary session.",
"Inside that, architecture, PPT, demo all belong together.",
"We should not create new memory IDs for every message.",
"Only when the topic really changes.",
"How do we detect topic continuity?",
"Keyword-based classification should be enough.",
"Keyword-based classification should be enough.",
"Judges will prefer transparency over black-box models.",
"We should also track turn numbers.",
"Turn numbers help explain why something was recalled.",
"For example, 'This was stored at Turn 2'.",
"For example, 'This was stored at Turn 2'.",
"What about forgetting temporary memory?",
"We can end it when the user says 'end' or 'stop'.",
"Or automatically expire after some days.",
"Let us add a 30-day expiry.",
"Now let us think about output design.",
"We should not dump JSON every time.",
"That would overwhelm the user.",
"Instead, just say which memory ID was used.",
"Like 'P1 recalled' or 'T1 recalled'.",
"Only show full data when the user explicitly asks.",
"For example what did you store?",
"That triggers audit mode just like above.",
"Audit mode should show structured json.",
"Including origin turn and last used turn.",
"This will impress the judges.",
"Now think about scalability.",
"JSON is fine for 500-1000 turns.",
"Database can be future work.",
"We should clearly mention that in the PPT.",
"Let us name the system Cerebrum.",
"Can you explain this?",
"Why did you recall what you recalled?"
]

for msg in conversation:
    print("User:", msg)
    result = process_input(msg)
    print("Assistant:", result)
    print()
EOF

echo ""

echo "DEMO COMPLETE"

