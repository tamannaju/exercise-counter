# Exercise Counter

An AI-powered web application that counts exercise repetitions in real-time using computer vision. Supports both video file uploads and live webcam processing.

## 🚨 Having Issues? 🚨

**Getting errors when running the app?** → See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

**First time setup?** → See [QUICKSTART.md](QUICKSTART.md)

**Windows user?** → See [SETUP_WINDOWS.md](SETUP_WINDOWS.md)

## Features

- 🎥 **Video Upload Mode**: Upload exercise videos and get annotated results
- 📹 **Live Webcam Mode**: Real-time exercise counting using your webcam
- 🏋️ **Multiple Exercise Types**: Squat, Push-up, Pull-up, and Crunch detection
- 🤖 **AI-Powered**: Uses MediaPipe Pose for accurate body landmark detection
- 📊 **Visual Feedback**: Shows joint angles and rep counts on video

## Requirements

- Python 3.8 or higher (tested with Python 3.10+)
- Webcam (for live mode)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/tamannaju/exercise-counter.git
cd exercise-counter
```

Or clone a specific branch:
```bash
gh repo clone tamannaju/exercise-counter
cd exercise-counter
git checkout copilot/add-live-webcam-counting
```

### 2. Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- OpenCV (video processing)
- MediaPipe >=0.10.9 (pose detection - flexible version for cross-platform compatibility)
- NumPy, Pandas, Matplotlib (data processing)

**Note:** MediaPipe version constraint is flexible (>=0.10.9) to ensure compatibility across Windows, macOS, and Linux, as some specific versions may not be available on all platforms.

### 4. Run the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000`

## Usage

### Video Upload Mode

1. Navigate to `http://127.0.0.1:5000`
2. Select an exercise type (Squat, Push-up, Pull-up, or Crunch)
3. Upload a video file
4. Click "Process" to analyze the video
5. View the annotated result with rep count

### Live Webcam Mode

1. Click "Try Live Webcam Mode" on the home page
2. Select an exercise type from the dropdown
3. Click "Start Webcam" to begin
4. Position yourself so your full body is visible
5. Perform exercises and watch the count update in real-time
6. Click "Stop Webcam" when finished

## Supported Exercises

| Exercise | Tracked Joints | Detection Method |
|----------|---------------|------------------|
| **Squat** | Hip, Knee, Ankle | Knee angle < 90° (down), > 160° (up) |
| **Push-up** | Shoulder, Elbow, Wrist | Elbow angle < 100° (down), > 150° (up) |
| **Pull-up** | Shoulder, Elbow, Wrist | Elbow angle < 70° (up), > 150° (down) |
| **Crunch** | Shoulder, Hip, Knee | Hip angle < 60° (up), > 120° (down) |

## Project Structure

```
exercise-counter/
├── app.py                 # Flask web application
├── video_process.py       # Video file processing
├── live_process.py        # Live webcam processing
├── pose_detector.py       # MediaPipe pose detection wrapper
├── counter.py             # Exercise counter classes
├── utils.py               # Angle calculation utilities
├── templates/
│   ├── index.html        # Video upload page
│   └── live.html         # Live webcam page
├── static/
│   ├── input_videos/     # Uploaded videos (created automatically)
│   └── output_videos/    # Processed videos (created automatically)
└── requirements.txt       # Python dependencies
```

## Troubleshooting

### Import Errors

If you see errors like `ModuleNotFoundError: No module named 'flask'` or `No module named 'cv2'`:

**Solution:** Make sure you've activated your virtual environment and installed all dependencies:
```bash
# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### MediaPipe Version Errors

If you see: `ERROR: Could not find a version that satisfies the requirement mediapipe==X.X.X`

**Cause:** Specific MediaPipe versions may not be available on all platforms (Windows/macOS/Linux).

**Solution:** The requirements.txt now uses a flexible version constraint (`mediapipe>=0.10.9`) that works across all platforms. Simply run:
```bash
pip install -r requirements.txt
```

If you still have issues, you can install the latest available version:
```bash
pip install mediapipe
```

### Webcam Not Working

If the live webcam mode doesn't work:

1. **Check webcam permissions**: Ensure your browser has permission to access the webcam
2. **Check if webcam is in use**: Close other applications using the webcam
3. **Try a different browser**: Chrome/Edge usually work best for webcam features
4. **Check the console**: Open browser developer tools (F12) to see error messages

### Video Processing Errors

If video upload fails:

1. **Check video format**: Supported formats include MP4, AVI, MOV
2. **Check video size**: Very large files may take time to process
3. **Check pose visibility**: Best results with side-view videos showing full body

## Technical Details

### Pose Detection

- Uses **MediaPipe Pose** for detecting 33 body landmarks
- Processes at ~20-30 FPS depending on hardware
- Works best with:
  - Side-view camera angle
  - Good lighting conditions
  - Full body visible in frame
  - Minimal background clutter

### Exercise Counting Algorithm

1. Detect body landmarks using MediaPipe
2. Extract relevant joint coordinates (e.g., hip-knee-ankle for squats)
3. Calculate joint angle using vector geometry
4. Apply finite-state machine to track movement phases:
   - "Up" position (extended)
   - "Down" position (flexed)
5. Increment counter on complete cycle (down → up or up → down)

### Thread Safety

The live webcam processor uses thread locks to safely handle concurrent requests:
- Lock is held minimally (only for state checks and updates)
- Blocking I/O (frame capture, pose detection) happens outside locks
- Prevents thread starvation and ensures smooth streaming

## Known Limitations

- Works best for side-view videos/camera angles
- Performance decreases if joints are occluded
- Sensitive to lighting and camera distance
- Requires visible full body in frame

## Future Enhancements

- [ ] Multi-angle pose detection
- [ ] Form correction suggestions
- [ ] Workout session history
- [ ] Additional exercise types
- [ ] Mobile app support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- **MediaPipe** by Google for pose detection
- **OpenCV** for video processing
- **Flask** for web framework
