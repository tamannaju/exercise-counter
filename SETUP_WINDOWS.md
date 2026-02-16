# Setup Guide for Windows

This guide provides step-by-step instructions for setting up the Exercise Counter application on Windows.

## Prerequisites

1. **Python 3.8+** installed on your system
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"

2. **Git** (optional, for cloning)
   - Download from [git-scm.com](https://git-scm.com/download/win)

## Step-by-Step Setup

### 1. Open Command Prompt or PowerShell

Press `Win + R`, type `cmd`, and press Enter.

### 2. Navigate to Your Desired Directory

```cmd
cd C:\Users\YourUsername\PycharmProjects
```

### 3. Clone or Download the Repository

**Option A: Using Git**
```cmd
git clone https://github.com/tamannaju/exercise-counter.git
cd exercise-counter
```

**Option B: Using GitHub CLI**
```cmd
gh repo clone tamannaju/exercise-counter
cd exercise-counter
git checkout copilot/add-live-webcam-counting
```

**Option C: Download ZIP**
- Download ZIP from GitHub
- Extract to your desired location
- Navigate to the folder in Command Prompt

### 4. Create Virtual Environment

```cmd
python -m venv .venv
```

### 5. Activate Virtual Environment

```cmd
.venv\Scripts\activate
```

You should see `(.venv)` at the beginning of your command prompt.

### 6. Upgrade pip (Optional but Recommended)

```cmd
python -m pip install --upgrade pip
```

### 7. Install Dependencies

```cmd
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- opencv-python (video processing)
- mediapipe (AI pose detection)
- numpy, pandas, matplotlib (data processing)

**Note:** Installation may take 5-10 minutes depending on your internet speed.

### 8. Verify Installation

```cmd
python -c "import flask, cv2, mediapipe; print('All dependencies installed successfully!')"
```

If you see "All dependencies installed successfully!", you're ready to go!

### 9. Run the Application

```cmd
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### 10. Open in Browser

Open your web browser and go to: `http://127.0.0.1:5000`

## Common Issues and Solutions

### Issue 1: "python is not recognized"

**Problem:** Python is not in your PATH.

**Solution:**
1. Reinstall Python and check "Add Python to PATH"
2. Or add Python manually to PATH:
   - Search for "Environment Variables" in Windows
   - Add Python installation directory to PATH

### Issue 2: "No module named 'flask'" (or other modules)

**Problem:** Dependencies not installed or virtual environment not activated.

**Solution:**
```cmd
# Make sure virtual environment is activated
.venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue 3: "Failed to start webcam"

**Problem:** Webcam is in use or permissions denied.

**Solution:**
1. Close other applications using webcam (Zoom, Teams, etc.)
2. Grant browser permissions to access webcam
3. Try a different browser (Chrome recommended)
4. Check Windows Privacy Settings:
   - Settings > Privacy > Camera
   - Enable "Allow apps to access your camera"

### Issue 4: Virtual environment activation fails in PowerShell

**Problem:** PowerShell script execution policy prevents activation.

**Solution:**
```powershell
# Run PowerShell as Administrator and execute:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activating again:
.venv\Scripts\Activate.ps1
```

### Issue 5: MediaPipe version not found

**Problem:** Error like "Could not find a version that satisfies the requirement mediapipe==0.10.21"

**Cause:** Specific MediaPipe versions may not be available on Windows or other platforms.

**Solution:**
The requirements.txt now uses a flexible version (>=0.10.9) for cross-platform compatibility:
```cmd
pip install -r requirements.txt
```

If you still encounter issues:
```cmd
# Install latest available version
pip install mediapipe

# Or install with verbose output to see what's available
pip install -v mediapipe
```

### Issue 6: Installation hangs on mediapipe

**Problem:** Large package download or network issues.

**Solution:**
```cmd
# Try installing with verbose output
pip install -v mediapipe

# Or specify timeout
pip install --timeout 300 mediapipe
```

### Issue 7: ImportError after installation

**Problem:** Wrong Python version or environment.

**Solution:**
```cmd
# Check Python version (should be 3.8+)
python --version

# Verify you're in the virtual environment
where python
# Should point to .venv\Scripts\python.exe

# Try reinstalling in clean environment
deactivate
rmdir /s .venv
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Using PyCharm

If you're using PyCharm:

1. **Open Project**: File > Open > Select exercise-counter folder

2. **Configure Interpreter**:
   - File > Settings > Project > Python Interpreter
   - Click gear icon > Add
   - Select "Virtual Environment" > Existing
   - Browse to `.venv\Scripts\python.exe`

3. **Run Configuration**:
   - Right-click `app.py`
   - Select "Run 'app'"
   - Or use the green play button

4. **Terminal**:
   - Use PyCharm's built-in terminal
   - Virtual environment activates automatically

## Testing the Application

### Test Video Upload

1. Navigate to `http://127.0.0.1:5000`
2. Select exercise type: "Squat"
3. Click "Upload Video" and select a video file
4. Click "Process"
5. Wait for processing (may take time depending on video length)
6. View annotated result

### Test Live Webcam

1. Click "Try Live Webcam Mode"
2. Select exercise type
3. Click "Start Webcam"
4. Allow browser to access webcam
5. Perform exercise
6. Watch real-time count updates
7. Click "Stop Webcam" when done

## Deactivating Virtual Environment

When you're done:

```cmd
deactivate
```

## Next Steps

- Read [README.md](README.md) for feature details
- Try different exercise types
- Record your own exercise videos for testing
- Explore the code to understand how it works

## Getting Help

If you encounter issues not covered here:

1. Check the error message carefully
2. Search for the error on Google/Stack Overflow
3. Open an issue on GitHub with:
   - Python version: `python --version`
   - OS version: `winver`
   - Full error message
   - Steps to reproduce

## Quick Reference

```cmd
# Activate environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Deactivate environment
deactivate
```

---

**Pro Tip:** Keep your virtual environment activated while developing. This ensures all dependencies are available and prevents conflicts with other Python projects.
