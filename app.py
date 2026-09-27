import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

notes_db = [
    {
        "id": 1,
        "title": "Cloud Computing Architecture Notes",
        "content": "Microservices architecture decouples applications into independent services.",
        "tags": ["Cloud", "Microservices"],
    }
]

@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify({"status": "success", "data": notes_db}), 200

@app.route('/api/analyze', methods=['POST'])
def analyze_note():
    data = request.get_json()
    content = data.get("content", "")
    word_count = len(content.split())
    return jsonify({
        "status": "success",
        "analysis": {
            "word_count": word_count,
            "estimated_reading_time_mins": round(word_count / 200, 2),
            "sentiment_detected": "Neutral"
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    