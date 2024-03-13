#!/usr/bin/env python3

import cv2
import time
from simple_facerec import SimpleFacerec
from play_sound import PlaySound
#Load Camera
camera_capture = cv2.VideoCapture(0)

#Encode faces from a folder
simple_face_recognizer = SimpleFacerec()
simple_face_recognizer.load_encoding_images("images/")

#Load Audio
play_sound = PlaySound()

while True:
    ret, frame = camera_capture.read()

    #Detect faces
    face_locations, face_names = simple_face_recognizer.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1= face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        separator = " "
        trimmed_name = name.split(separator, 1)[0]
        cv2.putText(frame, trimmed_name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
#         play_sound.lookup_greeting(trimmed_name.lower())
#         play_sound.send_welcome_message()
#         time.sleep(300)
        break
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

camera_capture.release()
cv2.destroyAllWindows()