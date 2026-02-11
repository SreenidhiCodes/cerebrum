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
            font-family: Arial, sans-serif;
            background-color: #0f172a;
            color: white;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px;
        }
        h1 {
            color: #38bdf8;
        }
        #chatbox {
            width: 80%;
            max-width: 800px;
            height: 400px;
            background: #1e293b;
            padding: 20px;
            overflow-y: auto;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .user { color: #facc15; }
        .assistant { color: #4ade80; }
        input {
            width: 70%;
            padding: 10px;
            border-radius: 5px;
            border: none;
        }
        button {
            padding: 10px 15px;
            background-color: #38bdf8;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0ea5e9;
        }
    </style>
</head>
<body>

<h1>Cerebrum Memory Engine</h1>

<div id="chatbox"></div>

<input type="text" id="message" placeholder="Type your message..." />
<button onclick="sendMessage()">Send</button>

<script>
async function sendMessage() {
    const input = document.getElementById("message");
    const chatbox = document.getElementById("chatbox");

    const message = input.value;
    if (!message) return;

    chatbox.innerHTML += "<div class='user'><b>User:</b> " + message + "</div>";

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    chatbox.innerHTML += "<div class='assistant'><b>Assistant:</b> " + JSON.stringify(data) + "</div>";
    chatbox.scrollTop = chatbox.scrollHeight;

    input.value = "";
}
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




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

