#from matplotlib import pyplot as plt
import math

def draw_graph(x,y):
	plt.plot(x,y)
	plt.xlabel('x-coordinate')
	plt.ylabel('y-coordinate')
	plt.title('motion of a projectile')

def frange(start,final,interval):
	nums=[]
	while start < final:
		nums.append(start)
		start+=interval
	return nums

def trajectory(u,theta,mode):
	if u==0 or theta==0:
		raise ValueError('both inputs must be non-zero')
	theta=math.radians(theta)
	g=9.8
	t_flight=2*u*math.sin(theta)/g
	ints=frange(0,t_flight,0.01)
	x=[]
	y=[]
	for t in ints:
		x.append(u*math.cos(theta)*t)
		y.append(u*math.sin(theta)*t-0.5*g*t*t)
	if mode=='plot':
		draw_graph(x,y)
	else:
		return x,y,t_flight

if __name__ == '__main__':
	x1,y1,time1=trajectory(20,40,'dont plot')
	x2,y2,time2=trajectory(20,45,'dont plot')
	x3,y3,time3=trajectory(20,50,'dont plot')
	print('landed '+str(x1[len(x1)-1])+' meters from start')
	print('time in air : '+str(time1)+' seconds')
	print('landed '+str(x2[len(x2)-1])+' meters from start')
	print('time in air : '+str(time2)+' seconds')
	print('landed '+str(x3[len(x3)-1])+' meters from start')
	print('time in air : '+str(time3)+' seconds')
