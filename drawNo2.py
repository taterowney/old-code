#!/usr/bin/python3
from lists import Lstr
import tkinter as tk
from tkinter import colorchooser
btn1=False
newline=True
check=False
mode='line'
txtcheck=False
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
strings=[]
count=0
map=[]

def main():
	global canvas,outline,fill
	outline='#000000'
	fill='#ffffff'
	root=tk.Tk()
	cir_btn=tk.Button(root,text="circle",command=crc)
	cir_btn.pack()
	ln_btn=tk.Button(root,text="line",command=ln)
	ln_btn.pack()
	rec_btn=tk.Button(root,text="rectangle",command=rec)
	rec_btn.pack()
	txt_btn=tk.Button(root,text="text",command=text)
	txt_btn.pack()
	outline_btn=tk.Button(root,text='change outline color',command=out_color)
	outline_btn.pack()
	fill_btn=tk.Button(root,text='change fill color',command=fill_color)
	fill_btn.pack()
	canvas=tk.Canvas(root,width=500,height=500)
	canvas.pack()
	canvas.bind("<Motion>",mousemove)
	canvas.bind("<ButtonPress-1>",mouse1press)
	canvas.bind("<ButtonRelease-1>",mouse1release)
	canvas.bind_all('<KeyPress- >',write)
	for letter in alphabet:
		txt='<KeyPress-'+letter+'>'
		canvas.bind_all(txt,write)
	root.mainloop()

def write(event):
	global mode,canvas,txt,txtcheck,xorig,yorig,strings,count,new,fill,map
	if event.keysym=='Return' or event.keysym=='Down':
		txtcheck=False
	if txtcheck==True:
		canvas.delete(txt)
	if mode=='text':
		if event.keysym=='Return' or event.keysym=='Down':
			count+=1
			strings.append('')
			xorig=-50
			yorig=-50
			new=True
			map.append('canvas.create_text(xval+'+str(xorig)+',yval+'+str(yorig)+',font=("Helvetica",13),text="'+str(strings[count])+'\",fill=\"'+str(fill)+'\")')
		if new==False:
			if event.keysym=='space':
				strings[count]+=' '
			elif event.keysym.startswith('Shift'):
				pass
			elif event.keysym=='BackSpace':
				lst=list(strings[count])
				st=[]
				for i in range(len(lst)-1):
					st.append(lst[i])
				strings[count]=Lstr(st)
			else:
				strings[count]+=event.keysym
			txt=canvas.create_text(xorig,yorig,font=('Helvetica',13),text=strings[count],fill=fill)
			txtcheck=True

def text():
	global mode,strings,count
	mode='text'
	strings.append('')

def crc():
	global mode
	mode='circle'

def ln():
	global mode
	mode='line'

def rec():
	global mode
	mode='rectangle'

def mouse1press(event):
	global btn1,newline,new
	btn1=True
	newline=False
	global xorig,yorig
	xorig=event.x
	yorig=event.y
	new=False

def mouse1release(event):
	global btn1,newline,check
	btn1=False
	newline=True
	check=False

def mousemove(event):
	global xorig,yorig,canvas,check,line,mode,outline,fill
	if check==True:
		canvas.delete(line)
	if newline==False:
		if mode=='rectangle':
			line=canvas.create_rectangle(xorig,yorig,event.x,event.y,outline=outline,fill=fill)
			check=True
		elif mode=='line':
			line=canvas.create_line(xorig,yorig,event.x,event.y,fill=fill)
			check=True
		elif mode=='circle':
			line=canvas.create_oval(xorig,yorig,event.x,event.y,outline=outline,fill=fill)
			check=True

def out_color():
	global outline
	val=colorchooser.askcolor()[1]
	if val != None:
		outline=val

def fill_color():
	global fill
	val=colorchooser.askcolor()[1]
	if val != None:
		fill=val

if __name__=='__main__':
	main()
