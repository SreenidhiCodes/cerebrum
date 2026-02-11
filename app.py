from flask import Flask, request, jsonify
from model.main import process_input
import os
import json
import datetime

app = Flask(__name__)

LOG_FILE = "memorystore/demo_logs.json"
SESSION_FILE = "memorystore/session.json"




def initialize_files():
    os.makedirs("memorystore", exist_ok=True)

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

    if not os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "w") as f:
            json.dump({"current_turn": 0}, f, indent=4)


initialize_files()




@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "system": "CEREBRUM",
        "status": "running",
        "message": "Minimal Explainable Memory Architecture API"
    })




@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Please provide 'message' field"}), 400

    user_text = data["message"]

    # Process through core memory engine
    response = process_input(user_text)

    # Log conversation (BONUS FEATURE)
    log_interaction(user_text, response)

    return jsonify(response)




@app.route("/logs", methods=["GET"])
def get_logs():
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    return jsonify({
        "total_interactions": len(logs),
        "logs": logs
    })



@app.route("/memory", methods=["GET"])
def memory_state():
    state = {}

    for file in os.listdir("memorystore"):
        path = os.path.join("memorystore", file)
        with open(path, "r") as f:
            state[file] = json.load(f)

    return jsonify(state)




@app.route("/reset", methods=["POST"])
def reset():
    # Reset session
    with open(SESSION_FILE, "w") as f:
        json.dump({"current_turn": 0}, f, indent=4)

    # Clear logs
    with open(LOG_FILE, "w") as f:
        json.dump([], f)

    return jsonify({
        "status": "reset_complete",
        "message": "System memory and logs cleared"
    })




def log_interaction(user_text, response):
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    logs.append({
        "timestamp": str(datetime.datetime.now()),
        "user": user_text,
        "system_response": response
    })

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
