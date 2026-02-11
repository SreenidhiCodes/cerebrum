from flask import Flask, request, jsonify
from model.main import process_input
import traceback

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "system": "Cerebrum Memory Engine",
        "status": "running"
    })

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({
                "error": "No message provided"
            }), 400

        result = process_input(user_input)

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
