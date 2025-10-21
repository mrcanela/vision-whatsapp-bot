from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/webhook/whatsapp", methods=["POST"])
def whatsapp_webhook():
    data = request.get_json()
    print("\n📩 Nova mensagem recebida:\n", json.dumps(data, indent=2, ensure_ascii=False))
    return jsonify({"status": "ok"}), 200

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5678)
