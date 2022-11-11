from tk3 import *
tk,canvas=setup(1000,500)
round=0
from terrain import *

class avatar:
	def __init__(self,pos_x,pos_y):
		canvas.bind_all('<KeyPress-Up>',self.move)
		canvas.bind_all('<KeyPress-Down>',self.move)
		canvas.bind_all('<KeyPress-Left>',self.move)
		canvas.bind_all('<KeyPress-Right>',self.move)
		canvas.bind_all('<KeyPress-Return>',self.fire)
		self.x=pos_x
		self.y=pos_y
		self.speed=10
		self.update_pos()
		self.draw()
	def fire(self,event):
		global shots
		shots.append(Shot(self.x-10,self.y+10,[-20,-20]))
	def move(self,event):
		if event.keysym=='Up':
			for w in self.widgets:
				canvas.move(w,0,-self.speed)
				self.y-=self.speed
		if event.keysym=='Down':
			for w in self.widgets:
				canvas.move(w,0,self.speed)
				self.y+=self.speed
		if event.keysym=='Left':
			for w in self.widgets:
				canvas.move(w,-self.speed,0)
				self.x-=self.speed
		if event.keysym=='Right':
			for w in self.widgets:
				canvas.move(w,self.speed,0)
				self.x+=self.speed
		self.update_pos()
	def draw(self):
		self.widgets=[canvas.create_rectangle(self.x,self.y,self.x+10,self.y+10,outline='black',fill='black'),
canvas.create_polygon(self.x,self.y,self.x,self.y+10,self.x-20,self.y+7,outline='black',fill='black'),
canvas.create_polygon(self.x+10,self.y+10,self.x+10,self.y,self.x+15,self.y-5,outline='black',fill='black'),
canvas.create_line(self.x-10,self.y+4,self.x-6,self.y+4,fill='white'),
canvas.create_line(self.x+12,self.y+4,self.x+15,self.y+4,fill='orange'),
canvas.create_line(self.x+11,self.y+6,self.x+15,self.y+6,fill='orange'),
canvas.create_line(self.x+11,self.y+5,self.x+15,self.y+5,fill='orange'),
canvas.create_line(self.x-2,self.y+5,self.x+7,self.y+5,fill='white')]
		self.update_pos()
	def update_pos(self):
		self.x_side=list(range(self.x-20,self.x+15))
		self.y_side=list(range(self.y-5,self.y+10))

class Sprite:
	def __init__(self,type,move,pattern,location,ground=False):
		self.type=type
		self.move=move
		self.pattern=pattern
		self.x=location[0]
		self.y=location[1]-3
		self.ground=ground
		self.draw()
	def draw(self):
		global t,shots
		if self.type=='fuel':
			self.widgets=[canvas.create_rectangle(self.x,self.y,self.x+15,self.y-10,outline='#0b3b49',fill='#0b3b49'),canvas.create_oval(self.x+5,self.y,self.x-5,self.y-10,outline='#0b3b49',fill='#0b3b49'),canvas.create_oval(self.x+5+15,self.y,self.x-5+15,self.y-10,outline='#0b3b49',fill='#0b3b49'),canvas.create_text(self.x+7,self.y-5,text='fuel',font=('Courier',7),fill='white'),canvas.create_line(self.x,self.y,self.x,self.y+3,fill='black'),canvas.create_line(self.x+15,self.y,self.x+15,self.y+3,fill='black')]
		elif self.type=='artillary':
			self.widgets=[
canvas.create_line(self.x,self.y,self.x+15,self.y-15,fill='black'),
canvas.create_line(self.x,self.y-1,self.x+15,self.y-16,fill='black'),
canvas.create_rectangle(self.x+10,self.y,self.x+8,self.y-15,outline='#1c7304',fill='#1c7304')]
			self.shot=[30,30]
			self.shot_bonus=[15,-15]
		if not self.ground:
			move=self.move[round % len(self.move)]
		else:
			move=[]
			move.append(self.move[round % len(self.move)][0])
			move.append(-(t[self.x+self.move[round % len(self.move)][0]]-t[self.x]))
		for w in self.widgets:
			canvas.move(w,move[0],move[1])
		self.x+=move[0]
		self.y+=move[1]
		if self.pattern[round % len(self.pattern)]==1:
			sh=Shot(self.x+self.shot_bonus[0],self.y+self.shot_bonus[1],self.shot)
			shots.append(sh)

class Shot:
	def __init__(self,x,y,coords,type='bullet'):
		self.x=x
		self.y=y
		self.destroyed=False
		self.x_inc=coords[0]
		self.y_inc=coords[1]
		self.type=type
		self.draw()
	def draw(self):
		global t
		if self.destroyed==False:
			self.widgets=[canvas.create_line(self.x,self.y,self.x+self.x_inc//3,self.y-self.y_inc//3,fill='orange'),canvas.create_line(self.x,self.y-1,self.x+self.x_inc//3,self.y-self.y_inc//3-1,fill='orange')]
			xr=list(range(self.x,self.x+self.x_inc))
			yr=list(range(self.y,self.y-self.y_inc))
			self.x+=self.x_inc
			self.y-=self.y_inc
			for x,y in zip(xr,yr):
				if y >= 500-t[x]:
					self.destroy()
	def destroy(self):
		for w in self.widgets:
			canvas.delete(w)
		self.widgets=[canvas.create_oval(self.x-20,self.y-20,self.x,self.y,outline='orange',fill='orange')]
		self.destroyed=True

if __name__ == '__main__':
	global t,shots
	shots=[]
	t=create_backround(canvas)
	bkrnd(canvas,t)
#	s=shot(500,100,[20,-20])
#	s=Sprite('artillary',[[0,0]],[1,0,1],[500,500-t[500]],ground=True)
	a=avatar(100,100)
	for i in range(10):
		for j in range(50):
			tk.update()
			time.sleep(0.01)
		round+=1
		canvas.delete('all')
		bkrnd(canvas,t)
		a.draw()
		for shot in shots:
			shot.draw()
#	canvas.delete('all')
#	bkrnd(canvas,t)
#	s.destroy()
