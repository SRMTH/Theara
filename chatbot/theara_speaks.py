import spacy
import re
import os
import random
import time 
from mpd import MPDClient
from PyDictionary import PyDictionary

print("THEARA: Hello!")

client= MPDClient()
client.timeout=10
client.idletimeout= None
client.connect("localhost", 8800)

def startm():
    a= random.randint(1,12)
    print("THEARA: Sure, here you go! :)")
    client.play(a)

def stopm():
    print("THEARA: Stopping the music") 
    client.stop() 

def pausem():
    print("THEARA: Pausing the music")
    client.pause()
    b= input("YOU:")
    b= b.lower()
    c= re.search(".*play.*", b)
    if c:
        client.play()
        print("THEARA: Continuing to play the music")
    else:
       reply(b) 

def dictionary():
    a= input("THEARA: What is the word you want the meaning for?\nYOU:")
    dictionary= PyDictionary()
    mean= dictionary.meaning("{}".format(a))
    print("THEARA:\n\n")
    for i,j in mean.items():
        print( i,":\n")
        print(*j, sep="\n")
        print("\n")

def reply(a):
        nlp= spacy.load('en_core_web_sm')
        w= re.search(".*mean.*",a)
        x= re.search(".*play.*",a)
        y= re.search(".*stop.*",a)
        z= re.search(".*pause.*",a)
        if a != "bye":
            if(x):
                startm()
            elif(y):
                stopm()
            elif(z):
                pausem()
            elif(w):
                dictionary()
        else: 
            return exit 

while True:
    a= input("YOU:")
    a=a.lower()
    x= reply(a)
    if x== exit:
        break

print("THEARA: Bye!")

