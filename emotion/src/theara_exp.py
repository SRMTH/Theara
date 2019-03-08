#!/usr/bin/env python3
import keyboard
import cv2 
import numpy as np 
import time

print (cv2.__version__)
def blush():
    cap = cv2.VideoCapture('blush.gif') 

    while(cap.isOpened()): 
        ret, frame = cap.read() 
        if ret == True: 
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(100) == ord('q'): 
                break
        else: 
            break

def angry():
    cap = cv2.VideoCapture('angry.gif') 

    while(cap.isOpened()): 
        ret, frame = cap.read() 
        if ret == True: 
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(100) == ord('q'): 
                break
        else: 
            break

def cry():
    cap = cv2.VideoCapture('cry.gif') 

    while(cap.isOpened()): 
        ret, frame = cap.read() 
        if ret == True: 
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(100) == ord('q'): 
                break
        else: 
            break

def happy():
    cap = cv2.VideoCapture('happy.gif') 

    while(cap.isOpened()): 
        ret, frame = cap.read() 
        if ret == True: 
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(100) == ord('q'): 
                break
        else: 
            break

def judgy():
    cap = cv2.VideoCapture('judgy.gif') 

    while(cap.isOpened()): 
        ret, frame = cap.read() 
        if ret == True: 
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(100) == ord('q'): 
                break
        else: 
            break

def blink():
    cap = cv2.VideoCapture('normal.gif') 

    while(cap.isOpened()):
        ret, frame = cap.read() 
        if ret == True: 
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(70) == ord('q'): 
                break
        else: 
            break

def initial():
    img=cv2.imread('/home/gunjan/theara_ws/src/emotion/src/initial.PNG')
    cv2.imshow('Frame', img)
    cv2.waitKey(5)

c=[0,0,0,0,0]
total=1
exp="none"
while True:
    if exp=='blush':
        if c[0]==0:
            blush()
            time.sleep(1)
        else:
            if total%100==0:
                blink()
            else:
                initial()
        c[0]+=1
    
    elif exp=='angry':
        if c[1]==0:
            angry()
            time.sleep(1)
        else:
            if total%100==0:
                blink()
            else:
                initial()
        c[1]+=1
    
    elif exp=='cry':
        if c[2]==0:
            cry()
            time.sleep(1)
        else:
            if total%100==0:
                blink()
            else:
                initial()
        c[2]+=1

    elif exp=='judgy':
        if c[3]==0:
            judgy()
            time.sleep(1)
        else:
            if total%100==0:
                blink()
            else:
                initial()
        c[3]+=1

    elif exp=='happy':
        if c[4]==0:
            happy()
            time.sleep(1)
        else:
            if total%100==0:
                blink()
            else:
                initial()
        c[4]+=1
    
    elif (total%100)==0:
        blink()

    else:
        initial()

    total+=1
    print(total)

    if keyboard.is_pressed('b'):
        exp='blush'
        c[1:]=[0]*4
    elif keyboard.is_pressed('l'):
        exp='blink'
    elif keyboard.is_pressed('a'):
        exp='angry'
        c[0],c[2:]=0,[0]*3
    elif keyboard.is_pressed('c'):
        exp='cry'
        c[:2],c[3:]=[0]*2,[0]*2
    elif keyboard.is_pressed('j'):
        exp='judgy'
        c[:3],c[4]=[0]*3,0
    elif keyboard.is_pressed('h'):
        exp='happy'
        c[:4]=[0]*4

    if keyboard.is_pressed('q'): 
        break

cap.release() 
cv2.destroyAllWindows() 
