#!/usr/bin/env python

import serial
import sys
#print (sys.argv)
from time import sleep
#text = input("prompt")
#file = open("testfile.txt","r") 



ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port

#print (ser.readline())
while True:
     file = open("vio.txt","r") 
     print (ser.read())
     sleep(.1)

     print (file.readline())
     #print("You entered:", s)
     var = file.read()
     ser.write(var.encode("utf8"))
     #ser.write((sys.argv).encode())
     #print (file.read())

     #ser.write(str(chr(counter)).encode()) # Convert the decimal number to ASCII then send it to the Arduino
     #ser.write(('\r\n').encode)
     #print (counter,'\r\n') # Read the newest output from the Arduino
     #sleep(2) # Delay for one tenth of a second
     file.close()
     #if counter == 170:
        #counter = 20
