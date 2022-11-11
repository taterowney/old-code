from tkinter import *
from tk3 import *
from math import sin,cos,tan,radians,pi

def get_polar_coords(x,y,theta,hyp):
	opposite=sin(radians(theta))*hyp
	aj=cos(radians(theta))*hyp
#	canvas.create_line(x,y,x+aj,y-opposite)
	return (x+aj), (y+opposite)

if __name__ == '__main__':
	tk,canvas=setup(500,500)
	angle_line(200,200,0,50)
	angle_line(200,200,90,50)
	angle_line(200,200,180,50)
	angle_line(200,200,270,50)
