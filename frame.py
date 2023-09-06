import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)

frames_list = []
start_time = time.time()

while True:
    ret, frame = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    frame = frame.transpose(2, 1, 0)

    frames_list.append(frame)

    current_time = time.time()
    if current_time - start_time >= 1:
        break

frames_array = np.array(frames_list)

print("Frame shape is : ", frame.shape)
print("Frames shape : ", frames_array.shape)

cam.release()
cv2.destroyAllWindows()