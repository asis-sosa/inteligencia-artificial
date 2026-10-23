import numpy as np
import cv2 as cv
import math 

#rostro = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv.VideoCapture('/home/likcos/Vídeos/ultimo.mp4')
i = 0
frame3=None
while True:
    ret, frame = cap.read()
    frame3=frame[300:310, 320:330]
    frame2 = cv.resize(frame, (28, 30), interpolation=cv.INTER_AREA)
    if(i%5==0):
        cv.imwrite('/home/likcos/recorte/data/'+str(i)+'.jpg', frame2)

    cv.imshow('salida', frame)
    cv.imshow('salida3', frame3)
    
    i = i+1
    k = cv.waitKey(1)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()