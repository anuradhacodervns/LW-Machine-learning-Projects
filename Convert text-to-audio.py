from flask import Flask, request, jsonify
from flask_cors import CORS  
import pyttsx3

app = Flask(__name__)
CORS(app)  

@app.route('/api/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        text_speech = pyttsx3.init()
        text_speech.say(text)
        text_speech.runAndWait()
        return jsonify({"message": "Text has been spoken!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


