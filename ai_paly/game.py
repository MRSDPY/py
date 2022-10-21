import cv2

capture = cv2.VideoCapture(0)

while capture.isOpened():
    state, frame = capture.read()

    if state == True:
        cv2.imshow("Hi", frame)

        key = cv2.waitKey(0)

        if key == ord("q"):
            cv2.destroyAllWindows()
            capture.release()
