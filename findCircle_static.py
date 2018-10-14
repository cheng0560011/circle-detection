
import cv2
import numpy as np


img = cv2.imread('haro.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert here, don't use cv2.imgread('<imgname>', <flag>)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,20, param1=50, param2=80, minRadius=0, maxRadius=200)
#circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=100,minRadius=0,maxRadius=200)

if circles is not None: # in case nothing find will return None to circles
    for i in circles[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(0,0,255),2)


cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


