import serial
import datetime
import time
import sys
import os


name = input("What is your first name? ")
print("Nice to meet you " + name + "!")

age = input("What is your age? ")
enterval = input("Wear hear rate monitor, GSR monitor and hit enter....")

filenamegsr = name+str(age)+str(datetime.datetime.now())+".gsr"
filenamehr = name+str(age)+str(datetime.datetime.now())+".hr"
filenamexyz = name+str(age)+str(datetime.datetime.now())+".xyz"

filegsr = "gsr.txt"
filehr = "hr.txt"
filexyz = "xyz.txt"

print(filenamegsr)
print(filenamehr)
print(filenamexyz)

ser = serial.Serial('/dev/cu.usbmodem14321',9600)
f1 = open(filenamegsr,'a')
f2 = open(filenamehr,'a')
f3 = open(filenamexyz,'a')

'''f1a = open(filegsr, 'w')
f2a = open(filehr, 'w')
f3a = open(filexyz, 'w')
'''
mycount = 0
less10loop = 0

f1.write("name" + "," + "age" + "," + "timestamp" + "," + "GSR")
f2.write("name" + "," + "age" + "," + "timestamp" + "," + "HRate")
f3.write("name" + "," + "age" + "," + "timestamp" + "," + "X" + "," + "Y" + "," + "Z")

while True:
    try:
        if (less10loop == 0):
            f1a = open(filegsr, 'w')
            f2a = open(filehr, 'w')
            f3a = open(filexyz, 'w')
        
        text = ser.readline().decode()
        print (text)
        f1.write(str(mycount) + "," + name + "," + datetime.datetime.now().strftime("%b.%d.%Y.%H:%M:%S") + "," + text)
        f2.write(str(mycount) + "," + name + "," + datetime.datetime.now().strftime("%b.%d.%Y.%H:%M:%S") + "," + text)
        f3.write(str(mycount) + "," + name + "," + datetime.datetime.now().strftime("%b.%d.%Y.%H:%M:%S") + "," + text)
            
        if (mycount < 10):
            f1a.write(str(mycount) + "," + name + "," + datetime.datetime.now().strftime("%b.%d.%Y.%H:%M:%S") + "," + text)
            f2a.write(str(mycount) + "," + name + "," + datetime.datetime.now().strftime("%b.%d.%Y.%H:%M:%S") + "," + text)
            f3a.write(str(mycount) + "," + name + "," + datetime.datetime.now().strftime("%b.%d.%Y.%H:%M:%S") + "," + text)
            f1a.flush()
            f2a.flush()
            f3a.flush()
            less10loop = 1
        else:
            mycount = 0
            less10loop = 0
            f1a.close()
            f2a.close()
            f3a.close()
        
        print ("sensor data logged..... hit control+c to end data collection ..... ", str(mycount), ".....", str(datetime.datetime.now()))
        mycount = mycount+1
        #os.system('tail -10 $filenamegsr > gsr.txt')
        
    except serial.SerialTimeoutException:
        print('Data could not be read')

ser.close()
