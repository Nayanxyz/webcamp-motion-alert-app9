import cv2    #open library
import time


video = cv2.VideoCapture(0)                                      # class for video
time.sleep(1)                                                    # time delay 1 second

while True:

    check, frame = video.read()                                   # frames in BGR
    cv2.imshow("my video", frame)                        # to see frames

    key = cv2.waitKey(1)                                          # waitkey is for delay frames capture

    if key == ord("q"):
        break

video.release()


