from flask import Flask, render_template, request, Response, jsonify
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import os

from video_process import process_video
from live_process import LiveProcessor

app = Flask(__name__)

# ========= Upload limits =========
MAX_MB = 10  # Maximum file size in megabytes
app.config["MAX_CONTENT_LENGTH"] = MAX_MB * 1024 * 1024  # bytes

ALLOWED_EXTENSIONS = {"mp4", "mov", "avi", "mkv"}

def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Global live processor instance (one per server)
live_processor = LiveProcessor()

# Folder paths
UPLOAD_FOLDER = "static/input_videos"
OUTPUT_FOLDER = "static/output_videos"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ========= Error handler for big uploads (413) =========
@app.errorhandler(RequestEntityTooLarge)
def handle_file_too_large(e):
    return render_template(
        "index.html",
        error=f"File size is too large. Maximum allowed size is {MAX_MB} MB."
    ), 413


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Validate fields
        exercise_type = request.form.get("exercise")
        if not exercise_type:
            return render_template("index.html", error="Please select an exercise."), 400

        if "video" not in request.files:
            return render_template("index.html", error="No video file found in the request."), 400

        video = request.files["video"]
        if not video or not video.filename or video.filename.strip() == "":
            return render_template("index.html", error="Please choose a video file to upload."), 400

        # Safer filename
        filename = secure_filename(video.filename)

        # Validate extension (optional but recommended)
        if not allowed_file(filename):
            return render_template(
                "index.html",
                error="Invalid file type. Allowed formats: mp4, mov, avi, mkv."
            ), 400

        input_path = os.path.join(UPLOAD_FOLDER, filename)
        output_filename = "output_" + filename
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        # Save uploaded file
        try:
            video.save(input_path)
        except Exception:
            return render_template("index.html", error="Failed to save the uploaded file."), 500

        # Process video
        try:
            count = process_video(exercise_type, input_path, output_path)
        except Exception:
            # optional cleanup
            try:
                if os.path.exists(input_path):
                    os.remove(input_path)
            except Exception:
                pass
            return render_template("index.html", error="Video processing failed. Please try another video."), 500

        # Optional sanity check
        if not os.path.exists(output_path):
            return render_template("index.html", error="Output video was not generated."), 500

        return render_template("index.html", result=count, output_video=output_filename)

    return render_template("index.html")


@app.route("/live")
def live():
    return render_template("live.html")


@app.route("/video_feed/<exercise_type>")
def video_feed(exercise_type):
    live_processor.stop()

    if not live_processor.start(exercise_type):
        return "Failed to start webcam", 500

    return Response(
        live_processor.generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


@app.route("/stop_feed", methods=["GET", "POST"])
def stop_feed():
    live_processor.stop()
    return jsonify({"status": "stopped"})


@app.route("/get_count")
def get_count():
    count = live_processor.get_count()
    return jsonify({"count": count})


if __name__ == "__main__":
    app.run(debug=True)