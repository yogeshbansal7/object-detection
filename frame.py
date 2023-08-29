import cv2
import time
import numpy as np

cam = cv2.VideoCapture(0)

start_time = time.time()

frames_list = []

while True:
    ret, frame = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    
    # frame = cv2.resize(frame, (640, 480)) # Resize frame to 640x480

    frames_list.append(frame)

    current_time = time.time()

    if current_time - start_time >= 1:
        print("1 second has passed")
        break

    cv2.imshow("Webcam Frame", frame)

frames_array = np.array(frames_list)
np.save('frames_array.npy', frames_array)

print("Shape is:")
print(frame.shape) 

cam.release()
cv2.destroyAllWindows()
