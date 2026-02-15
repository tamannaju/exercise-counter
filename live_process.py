import cv2
import threading
from pose_detector import PoseDetector
from counter import SquatCounter, PushupCounter, PullupCounter, CrunchCounter
from utils import calculate_angle


class LiveProcessor:
    """
    Handles live webcam processing for exercise counting.
    Thread-safe implementation for concurrent access.
    """
    
    def __init__(self):
        self.cap = None
        self.pose = None
        self.counter = None
        self.exercise_type = None
        self.joint_ids = None
        self.exercise_name = None
        self.is_running = False
        self.lock = threading.Lock()
        
    def start(self, exercise_type):
        """Initialize webcam and pose detector for the given exercise type."""
        with self.lock:
            if self.is_running:
                return False
                
            self.exercise_type = exercise_type
            
            # Initialize counter and joint IDs based on exercise type
            if exercise_type == "squat":
                self.counter = SquatCounter()
                self.joint_ids = (24, 26, 28)  # hip, knee, ankle
                self.exercise_name = "Squats"
            elif exercise_type == "pushup":
                self.counter = PushupCounter()
                self.joint_ids = (12, 14, 16)  # shoulder, elbow, wrist
                self.exercise_name = "Pushups"
            elif exercise_type == "pullup":
                self.counter = PullupCounter()
                self.joint_ids = (12, 14, 16)  # shoulder, elbow, wrist
                self.exercise_name = "Pullups"
            elif exercise_type == "crunch":
                self.counter = CrunchCounter()
                self.joint_ids = (12, 24, 26)  # shoulder, hip, knee
                self.exercise_name = "Crunches"
            else:
                return False
            
            # Initialize webcam and pose detector
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                return False
                
            self.pose = PoseDetector()
            self.is_running = True
            return True
    
    def generate_frames(self):
        """
        Generator that yields processed frames as JPEG images.
        Each frame has pose detection, angle calculation, and overlays.
        """
        while True:
            # Check if we should continue (quick lock check)
            with self.lock:
                if not self.is_running or self.cap is None:
                    break
                cap = self.cap
                pose = self.pose
                counter = self.counter
                joint_ids = self.joint_ids
                exercise_name = self.exercise_name
            
            # Read frame outside lock (blocking I/O)
            ret, frame = cap.read()
            if not ret:
                break
            
            width = frame.shape[1]
            height = frame.shape[0]
            
            # Run pose detection (potentially slow)
            results = pose.detect(frame)
            
            angle = None
            
            if results.pose_landmarks:
                lm = results.pose_landmarks.landmark
                
                p1 = lm[joint_ids[0]]
                p2 = lm[joint_ids[1]]
                p3 = lm[joint_ids[2]]
                
                pt1 = [p1.x * width, p1.y * height]
                pt2 = [p2.x * width, p2.y * height]
                pt3 = [p3.x * width, p3.y * height]
                
                angle = calculate_angle(pt1, pt2, pt3)
                
                # Update counter with lock
                with self.lock:
                    if self.counter is not None:
                        self.counter.update(angle)
                        current_count = self.counter.count
                    else:
                        current_count = 0
                
                # Draw angle text
                cv2.putText(
                    frame,
                    f"Angle: {int(angle)}",
                    (int(pt2[0]), int(pt2[1]-15)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2,
                )
                
                # Draw joints
                for p in [p1, p2, p3]:
                    cv2.circle(frame, (int(p.x*width), int(p.y*height)), 6, (0,0,255), -1)
            else:
                # Get count even if no pose detected
                with self.lock:
                    current_count = self.counter.count if self.counter is not None else 0
            
            # Draw counter overlay
            cv2.rectangle(frame, (0,0), (260,80), (0,0,0), -1)
            cv2.putText(
                frame,
                f"{exercise_name}: {current_count}",
                (10,55),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0,255,255),
                3,
            )
            
            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
                
            frame_bytes = buffer.tobytes()
            
            # Yield frame in MJPEG format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    
    def get_count(self):
        """Get current exercise count (thread-safe)."""
        with self.lock:
            if self.counter is None:
                return 0
            return self.counter.count
    
    def stop(self):
        """Stop the webcam stream and release resources."""
        with self.lock:
            self.is_running = False
            if self.cap is not None:
                self.cap.release()
                self.cap = None
            if self.pose is not None:
                self.pose.close()
                self.pose = None
            self.counter = None
