import cv2 as cv

cap = cv.VideoCapture('/home/likcos/Vídeos/cancer3/CoilocitosLB1227/c2.mp4')

while True:
    ret, img = cap.read()

    cv.imshow('resultado', img)
    
    #cv.imshow('gris', gris)
    
    k = cv.waitKey(1)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()