import serial
import time

TURNING=0
VELOCITY=1
current=TURNING
min=940
max=1780

ser=serial.Serial("/dev/ttyACM0",9600)
#change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

while True:
	read_ser=list(str(ser.readline()))
	del read_ser[:2]
	del read_ser[len(read_ser)-5:]
	printval=''
	for val in read_ser:
		printval+=val
	if printval!='':
		if int(printval)>min and int(printval)<max:
			print(str(current)+': '+printval)
	if current==TURNING:
		current=VELOCITY
	else:
		current=TURNING
