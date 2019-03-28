import datetime 
import re
from mpd import MPDClient
import time

client= MPDClient()
client.timeout=60
client.idletimeout=None
client.connect("localhost", 8800)

a= argv[0]
x= re.findall("[0-2][0-9]:[0-5][0-9]", a)

c= int(x[0][3])
b= x[0][0]
f= x[0][1]
e= x[0][4]
d= str(c+1)
c= str(c)

stop= False

while stop== False:
    rn= str(datetime.datetime.now().time())
    if rn >= "{0}{1}:{2}{3}:00.000000".format(b,f,c,e) and rn<= "{0}{1}:{2}{3}:05.000000".format(b,f,d,e):
        stop=True
        client.play(12)
        time.sleep(5)
        client.stop()

