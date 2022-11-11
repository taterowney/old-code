from tkinter import *
from tk3 import *
import time,random
ctr=0

def screensaver(saver,*args,**kwargs):
	tk,canvas=setup(10000,10000)
	if saver=='text':
		while 1:
			text_saver(args,kwargs)
def text_saver(*args,**kwargs):
	objs.append(canvas.create_text(random.randint(0,10000),random.randint(0,10000),args(random.randint(0,len(args)-1)),fill=kwargs['fill']))
	for o in objs:
		canvas.move(o,0,10)
	tk.after(200,text_saver,args,kwargs)
