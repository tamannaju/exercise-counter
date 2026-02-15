import mediapipe as mp
import cv2
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from pose_detector import PoseDetector
from counter import SquatCounter, PushupCounter, PullupCounter, CrunchCounter
from utils import calculate_angle

def process_video(exercise_type, input_path, output_path):
    if exercise_type == "squat":
        counter = SquatCounter()
        joint_ids = (24, 26, 28)  # hip, knee, ankle
        exercise_name = "Squats"

    elif exercise_type == "pushup":
        counter = PushupCounter()
        joint_ids = (12, 14, 16)  # shoulder, elbow, wrist
        exercise_name = "Pushups"

    elif exercise_type == "pullup":
        counter = PullupCounter()
        joint_ids = (12, 14, 16)  # shoulder, elbow, wrist
        exercise_name = "Pullups"

    elif exercise_type == "crunch":
        counter = CrunchCounter()
        joint_ids = (12, 24, 26)  # shoulder, hip, knee
        exercise_name = "Crunchs"
    else:
        raise ValueError("Invalid mode")

    
    # Initialize pose model 
    pose = PoseDetector()

    cap = cv2.VideoCapture(str(input_path))

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps ==0:
        fps=20

    writer = cv2.VideoWriter(
        str(output_path),
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height),
    )


    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

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
            counter.update(angle)


            # Draw knee angle
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

        # Squat counter overlay
        cv2.rectangle(frame, (0,0), (260,80), (0,0,0), -1)
        cv2.putText(
            frame,
            f"{exercise_name}: {counter.count}",
            (10,55),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0,255,255),
            3,
        )

        writer.write(frame)


    cap.release()
    writer.release()
    pose.close()

    return counter.count


