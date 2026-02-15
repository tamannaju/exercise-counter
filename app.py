from flask import Flask, render_template, request, Response, jsonify
import os
from video_process import process_video
from live_process import LiveProcessor

app = Flask(__name__)

# Global live processor instance (one per server)
live_processor = LiveProcessor()

# Folder paths
UPLOAD_FOLDER = "static/input_videos"
OUTPUT_FOLDER = "static/output_videos"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Get exercise type from dropdown
        exercise_type = request.form["exercise"]

        # Get uploaded video
        video = request.files["video"]

        input_path = os.path.join(UPLOAD_FOLDER, video.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "output_" + video.filename)

        # Save uploaded file
        video.save(input_path)

        # Process video
        count = process_video(exercise_type, input_path, output_path)

        return render_template(
            "index.html",
            result=count,
            output_video="output_" + video.filename
        )

    return render_template("index.html")


@app.route("/live")
def live():
    """Render the live webcam page."""
    return render_template("live.html")


@app.route("/video_feed/<exercise_type>")
def video_feed(exercise_type):
    """
    MJPEG stream endpoint for live webcam feed.
    Starts the webcam and processes frames in real-time.
    """
    # Stop any existing stream first
    live_processor.stop()
    
    # Start new stream with the selected exercise type
    if not live_processor.start(exercise_type):
        return "Failed to start webcam", 500
    
    return Response(
        live_processor.generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


@app.route("/stop_feed", methods=["GET", "POST"])
def stop_feed():
    """Stop the live webcam stream and release resources."""
    live_processor.stop()
    return jsonify({"status": "stopped"})


@app.route("/get_count")
def get_count():
    """Get the current exercise count as JSON."""
    count = live_processor.get_count()
    return jsonify({"count": count})


if __name__ == "__main__":
    app.run(debug=True)
