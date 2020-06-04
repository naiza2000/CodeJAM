from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np
backSub = cv.createBackgroundSubtractorKNN()
capture = cap = cv.VideoCapture("1.mp4")

ret, frame = capture.read()



if not capture.isOpened:
    print('Unable to open: ' + args.input)
    exit(0)
count = 0   
yo = "A"

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
        
        if (yo=="A"):
            
            cv.imwrite("image"+str(count)+str(yo)+".jpg", crop)
            yo="B"
            continue
        if (yo=="B"):
            cv.imwrite("image"+str(count)+str(yo)+".jpg", crop)
            yo="A"
    count+=1   
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        
        break
 

 
