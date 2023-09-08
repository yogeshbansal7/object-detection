import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)

frames_list = []
start_time = time.time()

while True:
    ret, frm = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    frame = frm.transpose(2, 1, 0)

    frames_list.append(frame)

    current_time = time.time()
    if current_time - start_time >= 1:
        break

frames_array = np.array(frames_list)
    
print("Original shape is: ", frm.shape)
print("Frame shape is : ", frame.shape)
print("Frames shape : ", frames_array.shape)
print("Frames per second : ", len(frames_array))

cam.release()
cv2.destroyAllWindows()