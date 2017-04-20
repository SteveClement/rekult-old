import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

s = 'a'
ser.open()
ser.write(s)
x = ser.readline()
print x
ser.close
