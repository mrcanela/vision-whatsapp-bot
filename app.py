from flask import Flask, request, jsonify
import logging, json

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/webhook/whatsapp", methods=["POST"])
def whatsapp_webhook():
    data = request.get_json()
    print("\n📩 Mensagem recebida:\n", json.dumps(data, indent=2, ensure_ascii=False))

    sender = data["body"]["payload"]["from"]
    msg = data["body"]["payload"]["body"]
    print(f"➡️  De {sender}: {msg}")

    return jsonify({"status": "ok"}), 200

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5678)
