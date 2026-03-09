import streamlit as st
import cv2
from datetime import datetime

st.title("Motion Detector")

start = st.button("start camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)
    close = st.button("close")

    while True:
        check , frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        day = datetime.now()
        current_day = day.strftime("%A")


        cv2.putText(img= frame, text=current_day,org=(25,50) ,fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=1.5, color=(0,0,0), thickness=1, lineType=cv2.LINE_AA)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        cv2.putText(img=frame, text= current_time, org=(25,100),fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=1.5, color=(0,0,0,), thickness=1,lineType=cv2.LINE_AA)

        streamlit_image.image(frame)

        if close:
            break