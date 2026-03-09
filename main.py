import cv2    #open library
import time


video = cv2.VideoCapture(0)                                      # class ,used to capture video from a camera or read video files
time.sleep(1)                                                    # time delay 1 second, Pauses the current thread
first_frame = None                                               # first frame created to compare other frames

while True:

    check, frame = video.read()                                   # frames in BGR
    grey_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    grey_frame_gau = cv2.GaussianBlur(grey_frame, (21,21), 0)     #gaussian blur to blur grey frame/ 21,21 amount of blur/ 0 is standard deviation

    if first_frame is None:                                                    # we gave first_frame = not going to change after the while loop executes one time,
        first_frame = grey_frame_gau

    delta_frame = cv2.absdiff(first_frame, grey_frame_gau)                     # absolute difference method to create new frame after two previous frame

    thresh_frame = cv2.threshold(delta_frame, 60 , 255, cv2.THRESH_BINARY)[1]    # This process, known as thresholding, converts a grayscale image into a binary
                                                                                              # [] thresh frame is a list , extract [1] value
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)                            # coverts object to bright light and bg to black to fill holes in image
                                                                                              # configuration is None , iterations, the higher we go ,
                                                                                              # more processing will applied to the method
    cv2.imshow("my video", dil_frame)                                                 # to see frames

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL,  cv2.CHAIN_APPROX_SIMPLE)   # contour means shape of outer surface / RETR_EXTERNAL, used to retrieve only
                                                                                                 # extreme outer surfaces or contours / chain_approx_simple reduces the number of points
                                                                                                # stored for a contour, focusing on structural vertices (corners)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)                                                   # x ,y points of rectangle , w width, h height
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)                                 # x+w is rectangle  expand as per object ,(0, 255, 0) Green rectangle, 3 is width

    cv2.imshow("Video", frame) # original frame
    key = cv2.waitKey(1)                                          # waitkey is for delay frames capture

    if key == ord("q"):
        break

video.release()


