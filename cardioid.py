from polar_coords import *
from tkinter import *
from math import cos
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()

a=150
oldx=100+2*a
oldy=250
for theta in range(1,361):
	x,y=get_polar_coords(100,250,theta=theta,hyp=a*(cos(radians(theta))+1))
	canvas.create_line(oldx,oldy,x,y)
	oldx=x
	oldy=y
