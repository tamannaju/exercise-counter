# Quick Start Guide

## ⚠️ STOP! Read This First ⚠️

**Before running `python app.py`, you MUST install dependencies first!**

## Common Errors (All mean: install dependencies!)

If you see ANY of these errors:

**Error 1 - Incomplete traceback:**
```
Traceback (most recent call last):
  File "...\app.py", line 3, in <module>
```
*(Error cuts off - this means dependencies aren't installed)*

**Error 2 - ModuleNotFoundError:**
```
Traceback (most recent call last):
  File "...\app.py", line 3, in <module>
    from video_process import process_video
  ...
ModuleNotFoundError: No module named 'flask'
```

**Error 3 - MediaPipe import error:**
```
ModuleNotFoundError: No module named 'mediapipe'
```

**Error 4 - OpenCV import error:**
```
ModuleNotFoundError: No module named 'cv2'
```

**All of these mean:** You haven't installed the required dependencies yet!

## The Solution (3 Steps)

### Step 1: Activate Virtual Environment

**Windows:**
```cmd
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

You should see `(.venv)` at the start of your command prompt.

### Step 2: Install Dependencies ⚠️ CRITICAL STEP!

**This step is MANDATORY! The app will not run without it!**

```cmd
pip install -r requirements.txt
```

Wait for installation to complete (may take 5-10 minutes).

You should see:
```
Successfully installed flask-3.x.x opencv-python-4.x.x mediapipe-0.10.x ...
```

This installs Flask, OpenCV, MediaPipe, and all other required packages.

**Verify installation worked:**
```cmd
python -c "import flask, cv2, mediapipe; print('✓ All dependencies installed!')"
```

If you see "✓ All dependencies installed!", you're ready to proceed!

### Step 3: Run the App

```cmd
python app.py
```

Open your browser to: `http://127.0.0.1:5000`

---

## First Time Setup?

If you don't have a virtual environment yet:

```cmd
# Create virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

---

## Still Having Issues?

See the detailed guides:
- [README.md](README.md) - Full documentation
- [SETUP_WINDOWS.md](SETUP_WINDOWS.md) - Windows-specific guide

## Common Fixes

**"Could not find a version that satisfies the requirement mediapipe==X.X.X"**
- MediaPipe versions vary by platform
- Solution: The requirements.txt now uses a flexible version (>=0.10.9)
- This ensures compatibility across Windows, macOS, and Linux

**"python is not recognized"**
- Add Python to PATH during installation
- Or use full path: `C:\Python310\python.exe`

**"Cannot activate virtual environment"**
- Make sure you're in the project directory
- Use correct slash: `\` for Windows, `/` for Unix

**"pip is not recognized"**
- Try: `python -m pip install -r requirements.txt`

**"Access denied" or "Permission error"**
- Run as Administrator
- Or use: `pip install --user -r requirements.txt`

---

**Need more help?** Open an issue on GitHub with:
- Your Python version: `python --version`
- Your OS
- The complete error message
