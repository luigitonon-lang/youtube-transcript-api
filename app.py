from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.get("/")
def home():
    return "Transcript API OK"

@app.get("/transcript")
def transcript():
    video_id = request.args.get("video_id")

    if not video_id:
        return jsonify({"error": "Missing video_id"}), 400

    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(
            video_id,
            languages=["it", "en"]
        )

        text = " ".join([x["text"] for x in transcript_list])

        return jsonify({
            "video_id": video_id,
            "transcript": text,
            "status": "TRANSCRIPT_OK"
        })

    except Exception as e:
        return jsonify({
            "video_id": video_id,
            "transcript": "",
            "status": "TRANSCRIPT_ERROR",
            "error": str(e)
        }), 200
