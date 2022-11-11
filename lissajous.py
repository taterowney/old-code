#! /usr/bin/python3
from tkinter import *
from tk3 import *
from math import sin,pi

# |                                                                         |
# v  change these parameters to create different versions of the lissajous  v
A=1
B=1
a=4
b=3
delta=pi/2
# ^  change these parameters to create different versions of the lissajous  ^
# |                                                                         |

tk,canvas=setup(500,500)

prev_x=A*sin(delta)*100+200
prev_y=B*sin(0)*100+200

for t in range(0,180):
	x=A*sin(a*t+delta)*100+200
	y=B*sin(b*t)*100+200
	canvas.create_line(prev_x,prev_y,x,y,fill='red')
	prev_x=x
	prev_y=y
