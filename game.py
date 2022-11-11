from tkinter import *
from tk3 import *
import time
import random
import sys

class C:
	pass

def paths(path):
	if path == 1:
		return [0,25,50,75,100,125,150,175,200,200],[250,225,200,175,150,125,100,75,50,50],[0,0,1,0,0,1,0,0,0,1]
	elif path == 2:
		return [500-0,500-25,500-50,500-75,500-100,500-125,500-150,500-175,500-200,500-200],[250,225,200,175,150,125,100,75,50,50],[0,0,1,0,0,1,0,0,0,1]
	elif path==3:
		return [0,25,50,75,100,125,150,175,200,225],[250,250,250,250,250,250,250,250,250,250],[1,0,0,1,0,0,0,1,0,0]
	elif path==4:
		return [500-0,500-25,500-50,500-75,500-100,500-125,500-150,500-175,500-200,500-225],[250,250,250,250,250,250,250,250,250,250],[1,0,0,1,0,0,0,1,0,0]
	elif path==5:
		return [250+0,25+250,50+250,75+250,100+250,125+250,150+250,400,400,400],[275,250,250,250,250,250,225,200,175,125],[0,1,0,1,1,0,0,0,0,0]
	elif path==6:
		return [500-(250+0),500-(25+250),500-(50+250),500-(75+250),500-(100+250),500-(125+250),500-(150+250),100,100,100],[225,250,250,250,250,250,225,200,175,125],[0,1,0,1,1,0,0,0,0,0]
	elif path==7:
		return [200,200,200,200,200,150,125,100,75,75]
	elif path==8:
		return [200,200,200,200,200,200,200,200,175,175],[50,75,100,125,150,175,200,225,250,275],[0,1,0,1,0,0,1,0,1,0]
	elif path==9:
		return [500-200,500-200,500-200,500-200,500-200,500-200,500-200,500-200,500-175,500-175],[50,75,100,125,150,175,200,225,250,275],[0,1,0,1,0,0,1,0,1,0]
	elif path==10:
		return [150,150,150,150,150,150,150,150,150,150],[275,300,325,350,375,400,425,450,475,525],[1,0,1,0,0,0,0,1,0,0]
	elif path==11:
		return [350,350,350,350,350,350,350,350,350,350],[275,300,325,350,375,400,425,450,475,525],[1,0,1,0,0,0,0,1,0,0]
	elif path==12:
		return [375,350,325,350,375,400,425,450,475,500],[150,175,200,225,250,275,300,325,350,375],[0,0,0,1,0,1,0,0,1,0]
	elif path==13:
		return [500-375,500-350,500-325,500-350,500-375,500-400,500-425,500-450,500-475,500-525],[150,175,200,225,250,275,300,325,350,375],[0,0,0,1,0,1,0,0,1,0]
	else :
		return None

def move_player(event):
	if p.dead==False:
		if event.keysym == 'Left':
			if p.pos > 0:
				canvas.move(p.player_ship1,-25,0)
				canvas.move(p.player_ship2,-25,0)
				canvas.move(p.player_ship3,-25,0)
				canvas.move(p.player_ship4,-25,0)
				p.pos-=25
				p.pos_side=list(range(p.pos+5,p.pos+55))
		else:
			if p.pos < 450:
				canvas.move(p.player_ship1,25,0)
				canvas.move(p.player_ship2,25,0)
				canvas.move(p.player_ship3,25,0)
				canvas.move(p.player_ship4,25,0)
				p.pos+=25
				p.pos_side=list(range(p.pos+5,p.pos+55))

def fireshot(event):
	p.xshots.append(p.pos)
	p.yshots.append(500)

def spriteshot(x,y):
	Sprite.s_shots_x.append(x)
	Sprite.s_shots_y.append(y)

class player:
	def __init__(self):
		canvas.bind_all('<KeyPress-Left>',move_player)
		canvas.bind_all('<KeyPress-Right>',move_player)
		canvas.bind_all('<KeyPress-Up>',fireshot)
		self.dead=False
		self.pos=200
		self.lives=1
		global player_ship
#		player_ship=canvas.create_rectangle(5+self.pos,450,55+self.pos,500,outline='blue',fill='blue')
		self.player_ship1=canvas.create_rectangle(5+self.pos,450,5+self.pos+12,500,outline='blue',fill='blue')
		self.player_ship2=canvas.create_rectangle(5+self.pos+36,450,5+self.pos+50,500,outline='blue',fill='blue')
		self.player_ship3=canvas.create_rectangle(5+self.pos,485,5+self.pos+50,500,outline='blue',fill='blue')
		self.player_ship4=canvas.create_rectangle(5+self.pos+18,465,5+self.pos+30,500,outline='blue',fill='blue')
		self.pos_side=list(range(self.pos+5,self.pos+55))

	def drawplayer(self):
		global player_ship,round
		pos=self.pos
		if p.dead==False:
			p.player_ship1=canvas.create_rectangle(5+self.pos,450,5+self.pos+12,500,outline='blue',fill='blue')
			p.player_ship2=canvas.create_rectangle(5+self.pos+36,450,5+self.pos+50,500,outline='blue',fill='blue')
			p.player_ship3=canvas.create_rectangle(5+self.pos,485,5+self.pos+50,500,outline='blue',fill='blue')
			p.player_ship4=canvas.create_rectangle(5+self.pos+18,465,5+self.pos+30,500,outline='blue',fill='blue')
	def draw_explosion(self):
		global player_ship,canvas,round
		player_ship1=None
		player_ship2=None
		player_ship3=None
		player_ship4=None
		canvas.create_rectangle(5+self.pos,450,55+self.pos,500,outline='orange',fill='orange')
		canvas.create_polygon(5+self.pos,450,30+self.pos,450,5+self.pos+12,425,outline='orange',fill='orange')
		canvas.create_polygon(5+self.pos+25,450,25+self.pos+30,450,5+self.pos+25+12,425,outline='orange',fill='orange')
		canvas.create_polygon(5+self.pos,450,5+self.pos,480,5+self.pos-25,465,outline='orange',fill='orange')
		canvas.create_polygon(5+self.pos,450+25,5+self.pos,480+25,5+self.pos-25,465+25,outline='orange',fill='orange')
		canvas.create_polygon(5+self.pos+50,450,5+self.pos+50,480,5+self.pos+25+50,465,outline='orange',fill='orange')
		canvas.create_polygon(5+self.pos+50,450+25,5+self.pos+50,480+25,5+self.pos+25+50,465+25,outline='orange',fill='orange')
		canvas.create_polygon(5+self.pos,450+50,30+self.pos,450+50,5+self.pos+12,425+50,outline='orange',fill='orange')
		canvas.create_polygon(5+self.pos+25,450+50,30+self.pos+25,450+50,5+self.pos+12+25,425+50,outline='orange',fill='orange')

class sprite:
	def __init__(self):
		self.path=None
		self.x_coords=None
		self.y_coords=None
		self.begin_time=None
		self.dead=False
		self.died=False
		self.marker=False
	def draw(self):
		global canvas,round
		if self.path!=None:
			if self.path==0:
#				canvas.create_rectangle(self.x_pos,self.y_pos,self.x_pos+5,self.y_pos+25,outline='red',fill='red')
#				canvas.create_rectangle(self.x_pos+20,self.y_pos,self.x_pos+25,self.y_pos+25,outline='red',fill='red')
#				canvas.create_rectangle(self.x_pos+10,self.y_pos+5,self.x_pos+15,self.y_pos+20,outline='red',fill='red')
#				canvas.create_rectangle(self.x_pos+5,self.y_pos+10,self.x_pos+10,self.y_pos+15,outline='red',fill='red')
#				canvas.create_rectangle(self.x_pos+15,self.y_pos+10,self.x_pos+20,self.y_pos+15,outline='red',fill='red')
#				canvas.create_rectangle(self.x_pos+15,self.y_pos+10,self.x_pos+20,self.y_pos+15,outline='red',fill='red')
				canvas.create_rectangle(self.x_pos,self.y_pos,self.x_pos+5,self.y_pos+25,outline='red',fill='red')
				canvas.create_rectangle(self.x_pos+20,self.y_pos,self.x_pos+25,self.y_pos+25,outline='red',fill='red')
				canvas.create_rectangle(self.x_pos+10,self.y_pos+5,self.x_pos+15,self.y_pos+20,outline='red',fill='red')
				canvas.create_rectangle(self.x_pos+5,self.y_pos+10,self.x_pos+10,self.y_pos+15,outline='red',fill='red')
				canvas.create_rectangle(self.x_pos+15,self.y_pos+10,self.x_pos+20,self.y_pos+15,outline='red',fill='red')
			else:
				inc=(round-self.begin_time)
#				print(inc)
#				print(inc>=len(self.shot_pos)-1)
				if inc > len(self.shot_pos)-1:
					self.path=0
					canvas.create_rectangle(self.x_pos,self.y_pos,self.x_pos+5,self.y_pos+25,outline='red',fill='red')
					canvas.create_rectangle(self.x_pos+20,self.y_pos,self.x_pos+25,self.y_pos+25,outline='red',fill='red')
					canvas.create_rectangle(self.x_pos+10,self.y_pos+5,self.x_pos+15,self.y_pos+20,outline='red',fill='red')
					canvas.create_rectangle(self.x_pos+5,self.y_pos+10,self.x_pos+10,self.y_pos+15,outline='red',fill='red')
					canvas.create_rectangle(self.x_pos+15,self.y_pos+10,self.x_pos+20,self.y_pos+15,outline='red',fill='red')
#					canvas.create_rectangle(self.x_pos,self.y_pos,self.x_pos+5,self.y_pos+25,outline='red',fill='red')
#					canvas.create_rectangle(self.x_pos+20,self.y_pos,self.x_pos+25,self.y_pos+25,outline='red',fill='red')
#					canvas.create_rectangle(self.x_pos+5,self.y_pos+10,self.x_pos+10,self.y_pos+15,outline='red',fill='red')
#					canvas.create_rectangle(self.x_pos+5+10,self.y_pos+10,self.x_pos+10+10,self.y_pos+15,outline='red',fill='red')
#					canvas.create_rectangle(self.x_pos+15,self.y_pos+10,self.x_pos+20,self.y_pos+15,outline='red',fill='red')
				else:
					self.x_pos=self.x_coords[inc]
					self.y_pos=self.y_coords[inc]
					canvas.create_rectangle(self.x_pos,self.y_pos,self.x_pos+5,self.y_pos+25,outline='red',fill='red')
					canvas.create_rectangle(self.x_pos+20,self.y_pos,self.x_pos+25,self.y_pos+25,outline='red',fill='red')
					canvas.create_rectangle(self.x_pos+10,self.y_pos+5,self.x_pos+15,self.y_pos+20,outline='red',fill='red')
					canvas.create_rectangle(self.x_pos+5,self.y_pos+10,self.x_pos+10,self.y_pos+15,outline='red',fill='red')
					canvas.create_rectangle(self.x_pos+15,self.y_pos+10,self.x_pos+20,self.y_pos+15,outline='red',fill='red')
					self.pos_side=list(range(self.x_pos-25,self.x_pos))
					if self.shot_pos[inc] == 1:
						spriteshot(self.x_pos,self.y_pos)
						canvas.create_rectangle(self.x_pos+10,self.y_pos+20,self.x_pos+15,self.y_pos+25,outline='orange',fill='orange')
	def explode(self):
		canvas.create_rectangle(self.x_pos,self.y_pos,self.x_pos+25,self.y_pos+25,fill='orange',outline='orange')
	def enter(self,path):
		global canvas,round
		self.path=path
		self.x_coords,self.y_coords,self.shot_pos=paths(self.path)
		if len(self.x_coords)!=len(self.y_coords):
			raise TypeError
		if len(self.shot_pos)!=len(self.y_coords):
			raise TypeError
		self.begin_time=round
		self.x_pos=self.x_coords[0]
		self.y_pos=self.x_coords[0]
		self.pos_side=list(range(self.x_coords[0]-25,self.x_coords[0]))

def check_collisions():
	global Sprites
	for s in Sprites:
		if s.dead==False:
			for shot in range(len(p.xshots)):
				if p.xshots[shot] in s.pos_side:
					shotrange=list(range(p.yshots[shot],p.yshots[shot]+100))
					if s.y_pos+25 in shotrange or s.y_pos in shotrange:
						s.path=None
						s.dead=True
	for shot in range(len(Sprite.s_shots_x)):
		if Sprite.s_shots_x[shot] in p.pos_side:
			shotrange=list(range(Sprite.s_shots_y[shot],Sprite.s_shots_y[shot]+100))
			if 450 in shotrange or 500 in shotrange:
				p.lives-=1
				if p.lives==0:
#					p.dead=True
					pass

def printshots():
	global canvas,p
	if len(p.xshots) > 0 and len(p.yshots) > 0:
		for i in range(len(p.yshots)):
			if p.yshots[i] > 0:
				p.yshots[i]-=100
				canvas.create_line(p.xshots[i]+30,p.yshots[i]+10,p.xshots[i]+30,p.yshots[i]+20,fill='orange')
	ct=0
	if len(Sprite.s_shots_x) > 0 and len(Sprite.s_shots_y) > 0:
		r=len(Sprite.s_shots_x)
		for i in range(r):
			if len(Sprite.s_shots_x) > 0 and len(Sprite.s_shots_y) > 0:
				j=i-ct
				if Sprite.s_shots_y[j] < 500:
					Sprite.s_shots_y[j]+=100
					canvas.create_line(Sprite.s_shots_x[j]-30,Sprite.s_shots_y[j]-10,Sprite.s_shots_x[j]-30,Sprite.s_shots_y[j]-20,fill='orange')
				else:
					ct+=1
					del Sprite.s_shots_x[j]
					del Sprite.s_shots_y[j]

def update_sprites():
	global round,Sprites
	if round==0:
		if Sprites[0].dead==False:
			Sprites[0].enter(1)
		if Sprites[1].dead==False:
			Sprites[1].enter(2)
	elif round==5:
		if Sprites[2].dead==False:
			Sprites[2].enter(3)
		if Sprites[3].dead==False:
			Sprites[3].enter(4)
	elif round==10:
		if Sprites[2].dead==False:
			Sprites[2].enter(5)
		if Sprites[3].dead==False:
			Sprites[3].enter(6)
		if Sprites[4].dead==False:
			Sprites[4].enter(1)
		if Sprites[5].dead==False:
			Sprites[5].enter(2)
	elif round==15:
		if Sprites[0].dead==False:
			Sprites[0].enter(8)
		if Sprites[1].dead==False:
			Sprites[1].enter(9)
	elif round==20:
		if Sprites[0].dead==False:
			Sprites[0].enter(10)
		if Sprites[1].dead==False:
			Sprites[1].enter(11)
	elif round==25:
		if Sprites[2].dead==False:
			Sprites[2].enter(12)
		if Sprites[3].dead==False:
			Sprites[3].enter(13)
		if Sprites[0].dead==False:
			Sprites[0].enter(1)
		if Sprites[1].dead==False:
			Sprites[1].enter(2)
	for s in Sprites:
		if s.dead==False:
			s.draw()
		else:
			if s.marker==False:
				s.explode()
				s.marker=True

def update_vals():
	global tk,canvas,p,ctr,round,end,Sprites,died,s_count,mark
	round+=1
	val=False
	for s in Sprites:
		if s.marker==False:
			val=True
	if mark==False:
		canvas.delete('all')
		bkrnd()
		canvas.create_text(250,250,text='Game Over',font=('Helvetica',30),fill='blue')
		canvas.create_text(250,300,text='You Win!',font=('Helvetica',30),fill='blue')
		tk.update_idletasks()
		tk.update()
		time.sleep(1)
		tk.destroy()
		s_count=[]
		try:
			sys.exit()
		except SystemExit:
			pass
		return True
	if died==True:
		canvas.delete('all')
		bkrnd()
		canvas.create_text(250,250,text='Game Over',font=('Helvetica',30),fill='red')
		canvas.create_text(250,300,text='You Lose',font=('Helvetica',30),fill='red')
		tk.update_idletasks()
		tk.update()
		time.sleep(1)
		tk.destroy()
		try:
			sys.exit()
		except SystemExit:
			pass
		return True
	if val==False:
		mark=False
	if p.dead==True:
		died=True

def bkrnd():
	global stars_x,stars_y,pts
	canvas.delete('all')
	canvas.create_rectangle(0,0,600,600,outline='black',fill='black')
	i=0
	for j in range(len(stars_x)):
		canvas.create_rectangle(stars_x[i],stars_y[i],stars_x[i]+2,stars_y[i]+2,fill='white')
		i+=1
	canvas.create_text(100,25,text='	GalactaPi		score : '+str(pts),font=('Helvetica',15),fill='blue')
	canvas.create_oval(236,369,246-5,379-5,fill='#ffd800')
	canvas.create_line(232,369,246,374,fill='#ffd800')
	canvas.create_oval(236-150,369+45,246-5-150,379-5+45,fill='#ffd800')
	canvas.create_line(232-150,369+45,246-150,374+45,fill='#ffd800')
	canvas.create_oval(200,150,215,165,fill='blue')

def update():
	global tk,canvas,p,ctr,round,end,Sprites,died,s_count,pts
	for s in Sprites:
		if s.dead==True:
			if s.died==False:
				s.died=True
				pts+=1
	bkrnd()
	p.drawplayer()
	update_sprites()
	check_collisions()
	if p.dead==True:
		p.draw_explosion()
	printshots()
	var=update_vals()
	if var==True:
		return
	if ctr < 100:
		try:
			ctr+=1
			tk.update_idletasks()
			tk.update()
			tk.after(250,update)
			tk.mainloop()
		except KeyboardInterrupt:
			end=True

def begin():
	global tk,canvas,p,ctr,round,Sprites,died,s_count,stars_x,stars_y,end,pts,mark,Sprite
	mark=True
	died=False
	ctr=0
	canvas=setup(w=500,h=500)
	tk=canvas.Tk
	p=player()
	s1=sprite()
	s2=sprite()
	s3=sprite()
	s4=sprite()
	s5=sprite()
	s6=sprite()
	Sprites=[s1,s2,s3,s4,s5,s6]
	pts=0
	s_count=len(Sprites)
	round=0
	tk.title("GalactaPi")
	tk.resizable(0,0)
	tk.wm_attributes("-topmost",1)
	p.xshots=[]
	p.yshots=[]
	Sprite=C()
	Sprite.s_shots_x=[]
	Sprite.s_shots_y=[]
	stars_x=[]
	stars_y=[]
	random.seed(26)
	for s in Sprites:
		s.pos_side=[0,1,2,3,4,5]
	for i in range(30):
		stars_x.append(random.randint(5,495))
		stars_y.append(random.randint(5,495))
	end=False
	canvas.bind_all('<KeyPress-Return>',end_menu)
	menu()
	update()
	end=False
	try:
		while end==False:
			if p.dead==True or s_count==[]:
				return
			if ctr==50:
				ctr=0
				tk.after(250,update)
	except KeyboardInterrupt:
		end=True

def end_menu(event):
	global end
	end=True

def menu():
	global end,tk
	bkrnd()
	canvas.create_text(250,250,text='GalactaPi v1.3',font=('Helvetica',30),fill='blue')
	canvas.create_text(250,300,text='Press Enter To Play',font=('Helvetica',30),fill='blue')
	if end==False:
		tk.update_idletasks()
		tk.update()
		time.sleep(0.25)
		var=menu()
		if var==True:
			return True
	else:
		return True

if __name__ == '__main__':
	global canvas,end
	end=False
	begin()
