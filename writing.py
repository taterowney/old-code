from tk3 import *

def move(event):
	global pos
	if event.keysym=='Right':
		canvas.move(line,1,0)
		pos+=1
	elif event.keysym=='Left':
		canvas.move(line,-1,0)
		pos-=1

def end(event):
	global pos,val1,val2
	if val1==None:
		val1=pos
	else:
		val2=pos
		print(abs(val2-val1)/len(message))

tk,canvas=setup(300,300)
message='hhhhh'
canvas.create_text(150,150,text=message,font=('Helvecica',10))
line=canvas.create_line(150,0,150,300)
val1=None
val2=None
pos=150
canvas.bind_all('<KeyPress-Right>',move)
canvas.bind_all('<KeyPress-Left>',move)
canvas.bind_all('<KeyPress-Return>',end)


