

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

    transposed_frame = cv2.transpose(frame) 
    #transpose(1, 0, 2) transposes the image

    frames_list.append(transposed_frame)

    current_time = time.time()

    if current_time - start_time >= 1:
        print("1 second has passed")
        break

    cv2.imshow("Webcam Frame", frame)

frames_array = np.array(frames_list)
np.save('frames_array.npy', frames_array)

print("shape is : ")
print(transposed_frame.shape)  # Print the shape of the transposed frame

cam.release()
cv2.destroyAllWindows()
