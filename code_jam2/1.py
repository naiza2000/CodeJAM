from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np
backSub = cv.createBackgroundSubtractorKNN()
capture = cap = cv.VideoCapture("sentry3.mkv")

ret, frame = capture.read()
# Define the codec and create VideoWriter object 
fourcc = cv.VideoWriter_fourcc(*'XVID') 
out = cv.VideoWriter('output1.avi', fourcc, 20.0, (1440,810))

if not capture.isOpened:
    print('Unable to open: ' + args.input)
    exit(0)
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
    
   
    
    out.write(frame)    
    cv.imshow('Contours', frame)
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
 

 
