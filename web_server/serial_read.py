import serial
import time
import sys
import sqlite3
import os.path
import re

ser = serial.Serial('/dev/ttyUSB0', 9600) # set up for serial read
time.sleep(2)

counter = 0
while 1: # repeatedly parse for incoming data
    connection = sqlite3.connect('xbee.db') # connect to local db
    db = connection.cursor()
    data = ''
    curr_e = time.localtime()
    curr_t = int(time.strftime("%H%M%S", curr_e)) #timestamp
    data = ser.readline() # reading data from router
    data = data.decode().strip('\r\n')
    if data.find('PPM') >= 0: # airquality data
        aq = int(data[0]) * 10 + int(data[1])
    else: # mac address data
        dev = int(data[0]) * 10 + int(data[1])
    if counter % 2 == 0 and counter != 0:
        print(curr_e)
        db.execute("INSERT INTO sensordata(devices, airquality, time) VALUES({},{},{})".format(dev,aq,curr_t)) # write to DB

    connection.commit()
    connection.close()
    counter += 1
