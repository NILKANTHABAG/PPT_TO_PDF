import cv2
import time

def save_frame(frame, output_path):
    cv2.imwrite(output_path, frame)
    print(f"Saved frame at {output_path}")

def capture_frames(video_path, output_directory, interval_minutes):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file.")
        return

    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    interval_frames = int(frame_rate * 60 * interval_minutes)
    frame_counter = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_counter += 1
        if frame_counter % interval_frames == 0:
            output_path = f"{output_directory}/frame_{frame_counter}.jpg"
            save_frame(frame, output_path)

    cap.release()

# Example usage
# change the image directory where video is there
video_path = r"E:\test\1.mp4" 
# give the adress where you want to save the images
output_directory = r"E:\test\photo"
# at how much interval you want to capture the photo
interval_minutes = 1

capture_frames(video_path, output_directory, interval_minutes)
