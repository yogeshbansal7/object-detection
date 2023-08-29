import cv2
# 0 signifies that we start our web cam
cam = cv2.VideoCapture(0)

# droidcam_url = "http://192.168.37.72:4747/video"
# cam = cv2.VideoCapture(droidcam_url)

cv2.namedWindow("Python webcam")

image_counter = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing...")
        break

    elif k%256 == 32:
        img_name = "opencv_frame_{}.png".format(image_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        image_counter += 1

cam.release()
cam.destroyAllWindows()