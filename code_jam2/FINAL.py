from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np
import math
backSub = cv.createBackgroundSubtractorKNN()
capture = cap = cv.VideoCapture("1.mp4")


ret, frame = capture.read()
# Define the codec and create VideoWriter object 
fourcc = cv.VideoWriter_fourcc(*'XVID') 
out = cv.VideoWriter('outputtemp.avi', fourcc, 20.0, (640,352))
bot2_detected =0
bot1_detected=0
bot1 = cv.imread('bot1.jpg')
bot2 = cv.imread('bot2.jpg')
bot1 = cv.cvtColor(bot1, cv.COLOR_BGR2GRAY) 
bot2 = cv.cvtColor(bot2, cv.COLOR_BGR2GRAY) 
cx1=cx2=cy1=cy2=0
while True:
    ret, frame = capture.read()
    if frame is None:
        break
    fgMask = backSub.apply(frame)
    contours, _ = cv.findContours(fgMask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=cv.contourArea)[-2:]
    
    for cnt in contours:
        x,y,w,h = cv.boundingRect(cnt)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        crop = frame[y:y+h,x:x+w]
        crop = cv.cvtColor(crop, cv.COLOR_BGR2GRAY) 
        cx = x+int(w/2)
        cy = y+int(h/2)
        
        if not bot1_detected:
            if crop.shape == bot1.shape:
                difference = cv.subtract(crop, bot1)
                if cv.countNonZero(difference) <= len(difference[0])*len(difference[1])/2 :
                    cv.putText(frame,"bot1", (x,y),cv.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
                    bot1_detected=1
                    cx1 = cx
                    cy1 = cy

                   
        elif not bot2_detected:
            if crop.shape == bot2.shape:
                difference = cv.subtract(crop, bot2)
                if cv.countNonZero(difference) <= len(difference[0])*len(difference[1])/2 :
                    cv.putText(frame,"bot2", (x,y),cv.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
                    bot2_detected=1
                    cx2 = cx
                    cy2 = cy    
                
                  
        else:
            dist1 = math.sqrt(float((cx - cx1)**2) + float((cy - cy1)**2))
            dist2 = math.sqrt(float((cx - cx2)**2) + float((cy - cy2)**2))
            if dist1<dist2:
                cx1 = cx
                cy1 = cy
                cv.putText(frame,"bot1", (x,y),cv.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
            else:
                cx2 = cx
                cy2 = cy
                cv.putText(frame,"bot2", (x,y),cv.FONT_HERSHEY_PLAIN,3,(0,255,0),3)

    out.write(frame)    
    cv.imshow('Contours', frame)
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break