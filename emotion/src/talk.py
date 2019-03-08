#!/usr/bin/env python
import rospy
import cv2
from pynput.keyboard import Key, Listener
from std_msgs.msg import String
import sys, select, termios, tty,random

'''def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key'''

'''key='none'
def on_press(key1):
    global key
    try:
        key=key1.char
    except AttributeError:
        pass
def on_release(key1):    
    if key1 == keyboard.Key.esc:
        # Stop listener
        return False'''
exp="none"
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    global exp
    total=0
    e=['b','a','c','j','h']
    while not rospy.is_shutdown():
        #cv2.waitKey(200)
        #key = getKey()
        #print ("rewind")
        #key=raw_input()
        #with Listener(on_press=key) as listener:listener.join()
        if total%41==0:
            i=random.randint(0,4)
        key=e[i]
        print(key)
        if key=='b': 
            exp='blush'
            #c[1:]=[0]*4
        elif key=='a': 
            exp='angry'
            #c[0],c[2:]=0,[0]*3
        elif key=='c': 
            exp='cry'
            #c[:2],c[3:]=[0]*2,[0]*2
        elif key=='j': 
            exp='judgy'
            #c[:3],c[4]=[0]*3,0
        elif key=='h': 
            exp='happy'
            #c[:4]=[0]*4
        elif key=='q':  
            exp='q'
        rospy.loginfo(exp)
        pub.publish(exp)
        rate.sleep()
        total+=1
        print (total)
        if key== 'q': 
            break
        #hello_str = "hello world %s" % rospy.get_time()
        
   
if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)