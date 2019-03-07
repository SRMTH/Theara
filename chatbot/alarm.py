import datetime 
import re
from mpd import MPDClient

client= MPDClient()
client.timeout=60
client.idletimeout=None
client.connect("localhost", 8800)

a= input("time= ")
x= re.findall("[0-5][0-9]", a)
c= int(x[1])
b= x[0]
d= str(c+1)
c= str(c)
stop= False
while stop== False:
    rn= str(datetime.datetime.now().time())
    if rn >= "{0}:{1}:00.000000".format(b,c) and rn<= "{0}:{1}:00.000000".format(b, d):
        stop=True
        client.play(12)


