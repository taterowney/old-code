pin=13
gUpTime=0L
gDownTime=0L

def cbfRise(a,b,tick):
	global gUpTime
	gUpTime=tick
	print('cbfI activated')
#        print(a,b,tick)

def cbfFall(c,d,tick):
	global gDownTime
	gDownTime=tick
	print('cbfII activated')
#	print(c,d,tick)

try:
	import time
	import pigpio

	pi = pigpio.pi()

	g=pi.callback(pin,pigpio.RISING_EDGE,cbfRise)
	h=pi.callback(pin,pigpio.FALLING_EDGE,cbfFall)

	while True:
		time.sleep(1.0)
		total=gDownTime-gUpTime
		print(total,gDownTime,gUpTime)
except KeyboardInterrupt:
	print(' : program ended')

