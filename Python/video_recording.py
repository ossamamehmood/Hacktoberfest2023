
# Here ret is for wheather all the values are being returned and frmae is carrying all the data for the image needed 

import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

""" 
img=cv2.imread('936378.jpg')
cv2.imshow('electrothon',img)
cv2.waitKey(0) 
"""


