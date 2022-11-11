currentcommand=None
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
otherchars=['comma','period','exclam','space','plus','minus','equal','apostrophe','colon','semicolon','quotedbl','slash','backslash','bar','parenright','parenleft','bracketleft','bracketleft','braceleft','braceright','at','numbersign','dollar','percent','asciicircum','ampersand','asterisk','less','greater','question','asciitilde','grave']
othercharsmap={'comma':',','period':'.','exclam':'!','space':' ','plus':'+','minus':'-','equal':'=','apostrophe':" ",'colon':':','semicolon':';','quotedbl':'"','slash':'/','backslash':'\\','bar':'|','parenright':')','parenleft':'(','bracketleft':'[','bracketright':']','braceleft':'{','braceright':'}','at':'@','numbersign':'#','dollar':'$','percent':'%','asciicircum':'^','ampersand':'&','asterisk':'*','less':'<','greater':'>','question':'?','asciitilde':'~','grave':'`'}
commands=['Shift_L','Shift_R','Control_L','Control_R','Alt_L','Alt_R','Super_L','Super_R','Caps_Lock','Up','Down','Right','Left','Return']
from lists import replace
import time
try:
	from tkinter import *
except ImportError:
	print('cannot import Tkinter file. Try "pip install Tkinter"')
def L_str(l):
	ret=''
	for elem in l:
		ret+=elem
	return ret
def setup(w=500,h=500,pack=True):
	try:
		global tk
		tk=Tk()
		global canvas
		canvas=Canvas(tk,width=w,height=h)
		canvas.pack()
		canvas.width=w
		canvas.height=h
		canvas.Tk=tk
		return canvas
	except TclError:
		print('no display enviorment available.Try "startx"')

def list_out(cvs,str,color):
	y=25
	j=len(str)
	ret=[]
	for i in range(0,j):
		ret.append(cvs.create_text(300,y,text=str[i],font=('Helvetica',14),fill=color))
		y=y+25
	return ret

class menu:
	def __init__(self,title,string,type):
		self.done=0
		self.mode=type
		self.str=string
		self.printval=[title]
		self.printval+=self.str
		self.length=len(self.str)-1
		self.yI=25+17
		self.yII=25+33
		self.selbar=canvas.create_rectangle(500,self.yI,0,self.yII,fill="blue",outline="blue")
		self.lines=list_out(self.printval)
		self.ctr=0
		self.t()

	def t(self):
		canvas.bind_all('<KeyPress-Up>',self.sel)
		canvas.bind_all('<KeyPress-Down>',self.sel)
		canvas.bind_all('<KeyPress-Return>',self.sel)
		while 1:
			if self.done != 0:
				return
			else:
				tk.update()
				tk.mainloop()
				time.sleep(0.2)

	def sel(self,event):
		global ctr
		global length
		global str
		global mode
		global done
		global rval
		if self.done==0:
			if self.ctr != 0:
				if event.keysym =='Up':
					self.ctr=self.ctr-1
					canvas.move(self.selbar,0,-25)
			if self.ctr != self.length:
				if event.keysym =='Down':
					canvas.move(self.selbar,0,25)
					self.ctr=self.ctr+1
			if event.keysym == 'Return':
				self.rval=self.str[self.ctr]
				print("%s  selected" % self.rval)
				canvas.delete(self.selbar)
				for i in self.lines:
					canvas.delete(i)
				self.done=1

class table:
	def __init__(self,x,y,c,size=[500,500]):
		self.canvas=c
		self.x=round(size[0]/x)
		self.y=round(size[1]/y)
		self.objs=[]
		self.buffer=[]
		for i in range(y):
			self.buffer.append([])
			for j in range(x):
				self.buffer[i].append('')
		self.writing=[]
		for i in range(y):
			self.writing.append([])
			for j in range(x):
				self.writing[i].append(None)
		for i in range(0,size[0],round(size[0]/x)):
			self.objs.append(canvas.create_line(i,0,i,size[0]))
		for i in range(0,size[1],round(size[1]/y)):
			self.objs.append(canvas.create_line(0,i,size[1],i))
		canvas.bind_all('<KeyPress-BackSpace>',self._delete)
		canvas.bind('<ButtonRelease-1>',self._assign)
		bindletters(self._write)
	def _assign(self,event):
		self.x_val=event.x // self.x
		self.y_val=event.y // self.y
	def _write(self,event):
		self.buffer[self.y_val][self.x_val]+=event
		if self.writing[self.y_val][self.x_val]!=None:
			canvas.delete(self.writing[self.y_val][self.x_val])
		val=self.canvas.create_text(self.x_val*self.x+(0.5*self.x),self.y_val*self.y+(0.5*self.y),text=self.buffer[self.y_val][self.x_val],font=('Helvetica',10))
		self.writing[self.y_val][self.x_val]=val
		self.objs.append(val)
	def _delete(self,event):
		if self.buffer[self.y_val][self.x_val]!='':
			l=list(self.buffer[self.y_val][self.x_val])
			del l[len(l)-1]
			self.buffer[self.y_val][self.x_val] = L_str(l)
			self._write('')
	def destroy(self):
		for o in self.objs:
			self.canvas.delete(o)

class new_tab:
	def create_new_tab(self,w=100,h=100):
		self=Canvas(tk,width=w,height=h)

def bindletters(f):
	global func
	func=f
#	canvas.bind_all('<KeyPress- >',write)
	for letter in alphabet:
		txt='<KeyPress-'+letter+'>'
		canvas.bind_all(txt,_write)
	for letter in otherchars:
		txt='<KeyPress-'+letter+'>'
		canvas.bind_all(txt,_write)
	for cmd in commands:
		txt='<KeyPress-'+cmd+'>'
		canvas.bind_all(txt,_cmd)
	tk.update()
#	tk.mainloop()

def _write(event):
	global func
	if event.keysym in alphabet:
		tk.after(0,func,event.keysym)
	elif event.keysym in otherchars:
		tk.after(0,func,othercharsmap[event.keysym])

def _cmd(event):
	global currentcommand
	currentcommand=event.keysym

class get_input:
	def __init__(self,x,y,func,size=[500,20]):
		self.bar=canvas.create_rectangle(x,y,x+size[0],y+size[1],outline='blue')
		self.x=x
		self.y=y
		self.size=size
		self.text_size=self.size[1]-5
		self.letters=[]
		self.cursor_pos=x+5
		self.message=[]
		self.func=func
		canvas.bind_all('<KeyPress-BackSpace>',self._delete)
		bindletters(self._print)
		canvas.bind_all('<KeyPress-Return>',self._submit)
	def _print(self,event):
		self.letters.append(canvas.create_text(self.cursor_pos,self.y+(0.5*self.size[1]),text=event,font=('Helvetica',self.text_size)))
		self.message.append(event)
		self.cursor_pos+=self.text_size
#		print(event)
	def _submit(self,event):
		self.input=L_str(self.message)
#		print(self.input)
		tk.after(0,self.func,self.input,doofus=None)
		self.destroy()
	def _delete(self,event):
		if len(self.letters) > 0:
			canvas.delete(self.letters[len(self.letters)-1])
			self.cursor_pos-=self.text_size
			del self.letters[len(self.letters)-1]
			del self.message[len(self.message)-1]
	def destroy(self):
		for l in self.letters:
			canvas.delete(l)
		canvas.delete(self.bar)

def my_func(event):
	print(event)

if __name__=="__main__":
	tk,canvas=setup(500,500)
	i=get_input(0,250,my_func)
