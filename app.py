from flask import Flask, request, jsonify
from model import predict_emotion
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_response(emotion):
    responses = {
        "Happy": "That's great to hear! Keep it up 😊",
        "Sad": "I'm sorry you're feeling sad. Try talking to someone you trust.",
        "Angry": "Take a deep breath. Maybe a short break will help.",
        "Anxious": "It's okay to feel anxious. Try slow breathing exercises."
    }
    return responses.get(emotion, "I'm here to listen.")

def map_mental_state(emotion):
    mapping = {
        "Sad": "Possible Depression",
        "Anxious": "Anxiety",
        "Angry": "Stress",
        "Happy": "Stable"
    }
    return mapping.get(emotion, "Unknown")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text")

    emotion = predict_emotion(text)
    mental_state = map_mental_state(emotion)
    response = get_response(emotion)

    return jsonify({
        "emotion": emotion,
        "mental_state": mental_state,
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)