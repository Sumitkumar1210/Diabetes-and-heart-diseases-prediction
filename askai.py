from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

META_API_KEY = "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"
META_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def chat_with_meta(user_message):
    headers = {
        "Authorization": f"Bearer {META_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": user_message}]
    }
    response = requests.post(META_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"

@app.route("/ask_ai", methods=["POST"])
def ask_ai():
    data = request.json
    user_question = data.get("question", "")
    if not user_question:
        return jsonify({"error": "Question is empty"}), 400

    response = chat_with_meta(user_question)
    return jsonify({"AI Response": response})

if __name__ == "__main__":
    app.run(debug=True)
