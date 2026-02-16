# Troubleshooting Guide

## 🚨 Getting an Error? Start Here! 🚨

### Step-by-Step Diagnosis

#### 1. Is this your first time running the app?

**YES** → You need to install dependencies first!
```cmd
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

**NO** → Continue to step 2

---

#### 2. Did you activate your virtual environment?

Check your command prompt. Do you see `(.venv)` at the beginning?

**NO** → Activate it now:
```cmd
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

**YES** → Continue to step 3

---

#### 3. Did you install dependencies?

Test if dependencies are installed:
```cmd
python -c "import flask, cv2, mediapipe; print('✓ Dependencies installed')"
```

**Got an error?** → Install dependencies:
```cmd
pip install -r requirements.txt
```

**Success?** → Continue to step 4

---

#### 4. Did you pull the latest code?

Make sure you have the latest fixes:
```cmd
git pull origin copilot/add-live-webcam-counting
```

Then reinstall dependencies:
```cmd
pip install -r requirements.txt
```

---

## Common Error Messages

### Error: "Traceback... line 3, in <module>"

**Problem:** Dependencies not installed.

**Solution:**
```cmd
pip install -r requirements.txt
```

---

### Error: "ModuleNotFoundError: No module named 'flask'"

**Problem:** Flask not installed.

**Solution:**
```cmd
pip install -r requirements.txt
```

---

### Error: "ModuleNotFoundError: No module named 'cv2'"

**Problem:** OpenCV not installed.

**Solution:**
```cmd
pip install -r requirements.txt
```

---

### Error: "ModuleNotFoundError: No module named 'mediapipe'"

**Problem:** MediaPipe not installed.

**Solution:**
```cmd
pip install -r requirements.txt
```

---

### Error: "Could not find a version that satisfies the requirement mediapipe==X.X.X"

**Problem:** Specific MediaPipe version not available on your platform.

**Solution:** Already fixed! Pull latest code:
```cmd
git pull origin copilot/add-live-webcam-counting
pip install -r requirements.txt
```

---

## Virtual Environment Issues

### "Cannot activate virtual environment"

**Windows PowerShell:** Try this first:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\Activate.ps1
```

**Still not working?** Use Command Prompt instead of PowerShell:
```cmd
.venv\Scripts\activate.bat
```

---

### "Virtual environment doesn't exist"

Create it:
```cmd
python -m venv .venv
```

Then activate and install:
```cmd
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

---

## Still Stuck?

1. **Check you're in the right directory:**
   ```cmd
   cd path/to/exercise-counter
   ```

2. **Verify Python version (need 3.8+):**
   ```cmd
   python --version
   ```

3. **Try a fresh installation:**
   ```cmd
   # Remove old virtual environment
   rmdir /s .venv  # Windows
   rm -rf .venv  # macOS/Linux
   
   # Create new one
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   
   # Install dependencies
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Check detailed guides:**
   - [QUICKSTART.md](QUICKSTART.md) - Quick 3-step guide
   - [README.md](README.md) - Full documentation
   - [SETUP_WINDOWS.md](SETUP_WINDOWS.md) - Windows-specific help

5. **Open a GitHub issue** with:
   - Your Python version: `python --version`
   - Your OS
   - The complete error message
   - What you've tried so far

---

## Quick Reference

```cmd
# Windows Quick Start
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py

# macOS/Linux Quick Start
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

**Access app at:** http://127.0.0.1:5000
