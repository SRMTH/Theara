#!/usr/bin/env python
import rospy
import cv2 
import numpy as np 
import time
from std_msgs.msg import String 

def blush():
    cap = cv2.VideoCapture('/home/gunjan/theara_ws/src/emotion/src/love.mp4') 

    while(cap.isOpened()): 
        ret, frame = cap.read() 
        if ret == True: 
            frame = cv2.resize(frame,(int(854),int(480)))
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(20) == ord('q'): 
                break
        else: 
            break

'''if c==0:
    cv2.imwrite("/home/gunjan/theara_ws/src/emotion/src/ini.png",frame) 
    print ("saved!!!!!!!!!!!!!!!!!!!!!!!!!!11")
    c+=1'''
def angry():
    cap = cv2.VideoCapture('/home/gunjan/theara_ws/src/emotion/src/look_right.mp4') 
    while(cap.isOpened()): 
        ret, frame = cap.read() 
        if ret == True:
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(45) == ord('q'): 
                break
        else: 
            break

def cry():
    cap = cv2.VideoCapture('/home/gunjan/theara_ws/src/emotion/src/look_up.mp4') 

    while(cap.isOpened()): 
        ret, frame = cap.read() 
        if ret == True: 
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(38) == ord('q'): 
                break
        else: 
            break

def happy():
    cap = cv2.VideoCapture('/home/gunjan/theara_ws/src/emotion/src/look_left.mp4') 

    while(cap.isOpened()): 
        ret, frame = cap.read() 
        if ret == True: 
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(38) == ord('q'): 
                break
        else: 
            break

def judgy():
    cap = cv2.VideoCapture('/home/gunjan/theara_ws/src/emotion/src/blink.mp4') 

    while(cap.isOpened()): 
        ret, frame = cap.read() 
        if ret == True: 
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(38) == ord('q'): 
                break
        else: 
            break

def blink():
    cap = cv2.VideoCapture('/home/gunjan/theara_ws/src/emotion/src/blink.mp4') 

    while(cap.isOpened()):
        ret, frame = cap.read() 
        if ret == True: 
            print (frame.shape[0],frame.shape[1])
            cv2.imshow('Frame', frame) 
            if cv2.waitKey(38) == ord('q'): 
                break
        else: 
            break

def initial():
    img=cv2.imread('/home/gunjan/theara_ws/src/emotion/src/ini.png')
    #img = cv2.resize(img,(int(854),int(480)))
    cv2.imshow('Frame', img)
    cv2.waitKey(5)

c=[0,0,0,0,0]
total=1
exp='none'
def callback(data):
    global total
    global c
    global exp
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.data)    
    exp=data.data 
    if exp=='blush':
        if c[0]==0:
            blush()
            time.sleep(1)
        else:
            if total%50==0:
                blink()
            else:
                initial()
        c[0]+=1
        c[1:]=[0]*4
    
    elif exp=='angry':
        if c[1]==0:
            angry()
            time.sleep(1)
        else:
            if total%50==0:
                blink()
            else:
                initial()
        c[1]+=1
        c[0],c[2:]=0,[0]*3
    
    elif exp=='cry':
        if c[2]==0:
            cry()
            time.sleep(1)
        else:
            if total%50==0:
                blink()
            else:
                initial()
        c[2]+=1
        c[:2],c[3:]=[0]*2,[0]*2

    elif exp=='judgy':
        if c[3]==0:
            judgy()
            time.sleep(1)
        else:
            if total%50==0:
                blink()
            else:
                initial()
        c[3]+=1
        c[:3],c[4]=[0]*3,0

    elif exp=='happy':
        if c[4]==0:
            happy()
            time.sleep(1)
        else:
            if total%50==0:
                blink()
            else:
                initial()
        c[4]+=1
        c[:4]=[0]*4
    
    elif (total%50)==0:
        blink()

    else:
        initial()

    total+=1
    print(total)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    print ("listen")
    rospy.spin()
    
if __name__ == '__main__':
    listener()
    cap.release() 
    cv2.destroyAllWindows()
