from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os, uuid, tempfile
from moviepy.editor import VideoFileClip, AudioFileClip
from gtts import gTTS
import whisper

app = Flask(__name__)
CORS(app)
model = whisper.load_model("small")

@app.route("/")
def home():
    return jsonify({"status":"DubNaija AI Live!"})

@app.route("/dub", methods=["POST"])
def dub_video():
    return jsonify({"message":"Real dub go start soon!"})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)