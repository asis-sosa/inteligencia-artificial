import numpy as np
import cv2 as cv

rostro = cv.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv.VideoCapture('/home/likcos/x1/compux1/dwhelper/caras.mp4')
x=y=w=h= 0
img=imgr=0
count = 0
while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in rostros:
        m1 = int(h/2)
        n1 = int(w/2)
        #frame = cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        #frame = cv.circle(frame, (x+n1,y+m1), int(w/2) , (255, 0 ,0), 2 )
        img = frame[y:y+h,x:x+w]
        imgr = cv.resize(img, (100,100))
        count = count + 1   
    
    name = '/home/likcos/pruebacaras/luna/luna'+str(count)+'.jpg'
    cv.imwrite(name, imgr)
    cv.imshow('rostros', frame)
    #cv.imshow('cara', img)
    
    k = cv.waitKey(1)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()