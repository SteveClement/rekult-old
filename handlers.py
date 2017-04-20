from __future__ import print_function
import serial, time, time

ser = serial.Serial('/dev/ttyUSB0',115200)

ser.open()

y = 0


while y != 9999:
    x = ser.readline()
    int(x)
    y = 1 + y
    #process = x + 1
    print(x, end='')
ser.close()
