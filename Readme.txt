#Exercise Counter
This project detects human poses in videos using MediaPipe and counts squat,push_up, pull_up, crunch repetitions based on knee and enbow joint angles.
It outputs an annotated video, a CSV file with frame-wise angles and repetition counts, and a plot of knee/elbow angle over time.

## Features

- Pose detection using MediaPipe
- Automatic squat/push_up/pull_up, crunch repetition counting
- Knee/elbow/hip angle calculation
- Annotated output video with landmarks and rep count
- CSV export of angles and cumulative reps
- Angle-vs-frame plot visualization
- Modular code structure for easy extension to other exercises

## Repository Structure

exercise-counter/
│
├── notebooks/
│   └── run_video.ipynb
|   |___pose_detector.py
│   ├── counter.py
│   └── utils.py
├── data/
│   └── all motion videos
├── results/
│   ├── annotated_video.mp4
│   ├── reps.csv
│   └── angle_plot.png
├── requirements.txt
└── README.md

## Requirements

- Python 3.10
- OpenCV
- MediaPipe
- NumPy
- Pandas
- Matplotlib
- pose_landmark

## Methodology

1. Each video frame is read using OpenCV.
2. MediaPipe Pose detects 33 body landmarks.
3. for squat The right hip, knee, and ankle landmarks are extracted.Then the knee joint angle is computed using vector geometry.
4. for push_up and Pull_up soulder, elbow and wrist landmarks are extracted
5. A finite-state machine tracks squat movement:
   - Down position: angle < 90°
   - Up position: angle > 160° after going down
6. Each completed down→up cycle increments the squat counter.
5. A finite-state machine tracks elbow movement for push_up and pull_up:
   - Down position: angle < 100° / 70°
   - Up position: angle > 150° after going down
6. Each completed down→up cycle increments the push_up and Pull_up counter.
7. Results are visualized and saved.

## Known Limitations

- Works best for side-view videos.
- Performance decreases if the knee joint is occluded.
- Sensitive to camera angle and lighting.

##Assumptions:

- for best performance record the exercise video from side view


## Future Work
"Multi-view robust squat/push_up/pull_up detector

