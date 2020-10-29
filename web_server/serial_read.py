import serial, time, datetime, sys
import sqlite3
import os.path
#from xbee import XBee, ZigBee

SERIALPORT = '/dev/ttyUSB0'    # the com/serial port the XBee is connected to, the pi GPIO should always be ttyAMA0
BAUDRATE = 9600      # the baud rate we talk to the xbee
#TIMEOUT=1

ser = serial.Serial(SERIALPORT, BAUDRATE)
#conn=sqlite3.connect('sensordata.db')
#c=conn.cursor()
airq = 0
macnum = 0
#xbee = ZigBee(ser)

#print ('Receiving xbee data')
# Continuously read and print packets
#print('New value is {0:0.2f}'.format(ser.readline().strip()))

while True:
#    try:
        
        incoming = ''
        #ser.write('hello user \r\n')
        #response = ser.readline().strip() #wait_read_frame()
        incoming = ser.readline()
        air_quality = [0,0] # have to decode incoming because a lot of garbage characters come through
        if incoming[0] > 47 and incoming[0] < 58 and incoming[1] > 47 and incoming[1] < 58:
            air_quality[0] = incoming[0]-48
            air_quality[1] = incoming[1]-48
            aq = air_quality[0] * 10 + air_quality[1] # CONVERSION ASCII -> number -> total Air quality
            print(aq)
        #cursor.execute("INSERT INTO mac(currenttime, mac) values(time('now'),(?))", incoming)
        #c.execute("INSERT INTO airqua(currenttime, airq) values(time('now'),(?))", incoming)
        #print(incoming) #(response)
    #except KeyboardInterrupt:
     #   break

#ser.close()