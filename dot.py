from tkinter import *

def dot_to_dot():
	try:
		global new
		new=True
		tk=Tk()
		canvas=Canvas(tk,width=500,height=500)
		canvas.pack()
		canvas.bind_all('<KeyPress- >',change)
		xold=0
		yold=500
		while True:
			x=int(input('enter x coordinate : '))*10
			y=int(input('enter y coordinate : '))*10
			y=500-y
			if new==False:
				canvas.create_line(xold,yold,x,y)
			new=False
			xold=x
			yold=y
	except KeyboardInterrupt:
		print('done')

def change(event):
	global new
	new=True

if __name__ == '__main__':
	dot_to_dot()
