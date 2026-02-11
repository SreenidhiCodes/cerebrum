from flask import Flask, request, jsonify
from model.main import process_input
import traceback
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "system": "Cerebrum Memory Engine",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({
                "error": "Request must contain JSON with 'message' field"
            }), 400

        user_input = data["message"]

        result = process_input(user_input)

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
