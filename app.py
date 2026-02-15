from flask import Flask, render_template, request
import os
from video_process import process_video

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
