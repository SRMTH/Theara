import datetime

a= input("date: ")
b= input("time: ")
c= input("reminder: ")

stop= False
while stop== False:
    rn= str(datetime.datetime.now())
    if rn>= "{0} {1}:00.000000".format(a,b):
        stop=True
        print (c)
