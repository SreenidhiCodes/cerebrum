from flask import Flask, request, jsonify, render_template_string
from model.main import process_input

app = Flask(__name__)


CHAT_UI = """
<!DOCTYPE html>
<html>
<head>
    <title>Cerebrum Memory Engine</title>
    <style>
        body {
            background-color: #000000;
            color: #00ff88;
            font-family: Consolas, monospace;
            margin: 0;
            padding: 20px;
        }

        h1 {
            color: #00ff88;
            text-align: center;
            margin-bottom: 20px;
        }

        #chatbox {
            background-color: #0a0a0a;
            border: 1px solid #00ff88;
            height: 400px;
            overflow-y: auto;
            padding: 15px;
            margin-bottom: 15px;
            white-space: pre-wrap;
        }

        .user {
            color: #00ffff;
            margin-bottom: 8px;
        }

        .assistant {
            color: #00ff88;
            margin-bottom: 15px;
        }

        #inputArea {
            display: flex;
        }

        input {
            flex: 1;
            background-color: #000000;
            color: #00ff88;
            border: 1px solid #00ff88;
            padding: 10px;
            font-family: Consolas, monospace;
            font-size: 14px;
        }

        button {
            background-color: #000000;
            color: #00ff88;
            border: 1px solid #00ff88;
            padding: 10px 20px;
            cursor: pointer;
            font-family: Consolas, monospace;
        }

        button:hover {
            background-color: #003322;
        }
    </style>
</head>
<body>

<h1>CEREBRUM MEMORY ENGINE</h1>

<div id="chatbox"></div>

<div id="inputArea">
    <input type="text" id="message" placeholder="Type command..." />
    <button onclick="sendMessage()">EXECUTE</button>
</div>

<script>
async function sendMessage() {
    const input = document.getElementById("message");
    const chatbox = document.getElementById("chatbox");

    const message = input.value;
    if (!message) return;

    chatbox.innerHTML += "<div class='user'>> User: " + message + "</div>";

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    chatbox.innerHTML += "<div class='assistant'>> Assistant: " + JSON.stringify(data, null, 2) + "</div>";
    chatbox.scrollTop = chatbox.scrollHeight;

    input.value = "";
}

document.getElementById("message").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});
</script>

</body>
</html>
"""



@app.route("/")
def home():
    return render_template_string(CHAT_UI)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_input = data["message"]
    result = process_input(user_input)

    return jsonify(result)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


