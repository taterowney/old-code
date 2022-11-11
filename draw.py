#!/usr/bin/python3
import tkinter as tk
btn1=False
newline=False

def main():
	root=tk.Tk()
	canvas=tk.Canvas(root,width=2000,height=1000)
	canvas.pack()
#	img=tk.PhotoImage(file='/home/pi/lasers.jpg')
#	canvas.create_image(0,0,anchor=tk.NW,image=img)
	canvas.bind("<Motion>",mousemove)
	canvas.bind("<ButtonPress-1>",mouse1press)
	canvas.bind("<ButtonRelease-1>",mouse1release)
	root.mainloop()

def mouse1press(event):
	global btn1
	btn1=True

def mouse1release(event):
	global btn1,newline
	btn1=False
	newline=True

def mousemove(event):
	if btn1 == True:
		global xorig,yorig,newline
		if newline==False:
			event.widget.create_line(xorig,yorig,event.x,event.y,smooth=tk.TRUE)
		newline=False
	xorig=event.x
	yorig=event.y

if __name__=='__main__':
	main()
