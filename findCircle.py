
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, background = cap.read()
background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

while True :
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = gray-background
    # masked it before find circle
    # set boundary for haro classic green
    # reference (BGR)=(0,255,68)

    #lower = np.array([0, 30, 70], dtype="uint8")
    #upper = np.array([30, 120, 255], dtype="uint8")

    #mask = cv2.inRange(frame,lower,upper)
    #maskedImage = cv2.bitwise_and(frame,frame,mask = mask)
    #maskedImage = cv2.cvtColor(maskedImage, cv2.COLOR_BGR2GRAY)    
    
    # find circle
    if ret :
        #maskedImage = cv2.cvtColor(maskedImage, cv2.COLOR_BGR2GRAY)
        #cv2.blur(maskedImage,(11,11))
        #circles = cv2.HoughCircles(maskedImage,cv2.cv.CV_HOUGH_GRADIENT,10,300,param1=50,param2=200,minRadius=100,maxRadius=150)

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert videofram 2 gray image
        cv2.GaussianBlur(gray, (5, 5), 0)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 5, 300, param1=50, param2=300, minRadius=50, maxRadius=60)

        #circles = None
        if circles is not None:
            count = 0
            circles = np.uint16(np.around(circles))
        
            for i in circles[0,:]:
                cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
                cv2.circle(frame,(i[0],i[1]),2,(0,0,255),10)
                font = cv2.FONT_HERSHEY_SIMPLEX
                txt = ('[' + str(i[0]) + ',' + str(i[1]) + ']')
                cv2.putText(frame, txt, (100,100+count*50), font, 1, (255,0,0), 1)
                count = count+1


    cv2.imshow('detected', frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllwindows()
   

