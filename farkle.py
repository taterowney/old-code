from tk3 import *
tk,canvas=setup(500,500)
newtk,newcanvas=setup(600,600)
import random,time,rand
random.seed(rand.rand_int(0,100))

class game:
	def __init__(self):
		self.occupied=[0,0,0,0,0,0]
		self.top_occupied=[0,0,0,0,0,0]
		self.last_farkle=False
		canvas.bind('<ButtonRelease-1>',self.scan)
		canvas.bind_all('<KeyPress- >',self.reroll)
		canvas.bind_all('<KeyPress-Return>',self.redo)
		canvas.bind_all('<KeyPress-Shift_R>',self.pattern)
		canvas.create_rectangle(0,0,500,500,fill='#734603')
		tk.title('Solitare Farkle')
		tk.resizable(0,0)
		newtk.title('Solitare Farkle Instructions')
		newtk.resizable(0,0)
		newcanvas.create_rectangle(0,0,600,600,fill='#734603')
#		newcanvas.create_rectangle(0,0,
		list_out(newcanvas,['SOLITARE  FARKLE',' ','Press Enter to roll, and Space to continue rolling.','Select a die by clicking on it, and ','Right Shift to count the selected die for points',' ','single 1: 100 points','single 5: 50 points','three 1s: 300 points','three 2s: 200 points','three 3s: 300 points','three 4s: 400 points','three 5s: 500 points','three 6s; 600 points','four of a kind: 1000 points','five of a kind: 2000 points','six of a kind: 3000 points','one of every number 1 - 6: 1500 points','three pairs: 1500 points','four of a kind, plus a pair: 1500 points','two groups of three: 2500 points'],'white')
		d1=die(self)
		d2=die(self)
		d3=die(self)
		d4=die(self)
		d5=die(self)
		d6=die(self)
		self.scorer=scorer(self)
		self.farkle=None
		self.sprites=[d1,d2,d3,d4,d5,d6]
		self.last=True
		self.roll()
	def redo(self,event):
		self.scorer.update()
		if self.last_farkle==False:
			self.scorer.remove_farkles()
		else:
			self.last_farkle=False
		self.reset(event)
	def pattern(self,event):
#		print(self.top_occupied)
		if self.check_pattern(self.top_occupied):
			for s in self.sprites:
				if s.selected==True:
					self.last=True
					if s.old==False:
						self.top_occupied[int(s.num)-1]-=1
					s.old=True
					s.delete()
		if self.scorer.score >= 10000:
			canvas.create_text(250,250,font=('Helvetica',20),text='Congratulations! You won in %s rounds.'% str(self.scorer.round+1),fill='white')
			tk.update()
			time.sleep(4)
			tk.destroy()
	def reset(self,event):
#		print('triggered')
		if self.farkle!=None:
			canvas.delete(self.farkle)
			self.farkle=None
		for s in self.sprites:
			s.old=False
			s.selected=False
		self.top_occupied=[0,0,0,0,0,0]
		self.last=True
		self.roll()
	def reroll(self,event):
		for s in self.sprites:
			if s.selected==False:
				self.roll()
				return
		self.reset(None)
	def check_pattern(self,l):
		if l==[1,0,0,0,0,0]:
			self.scorer.add_score(100)
			return True
		elif l==[0,0,0,0,1,0]:
			self.scorer.add_score(50)
			return True
		elif l==[2,0,0,0,0,0]:
			self.scorer.add_score(200)
			return True
		elif l==[0,0,0,0,2,0]:
			self.scorer.add_score(100)
			return True
#		val = _pattern(l,1,3):
		elif l==[3,0,0,0,0,0]:
			self.scorer.add_score(300)
			return True
		elif l==[0,3,0,0,0,0]:
			self.scorer.add_score(200)
			return True
		elif l==[0,0,3,0,0,0]:
			self.scorer.add_score(300)
			return True
		elif l==[0,0,0,3,0,0]:
			self.scorer.add_score(400)
			return True
		elif l==[0,0,0,0,3,0]:
			self.scorer.add_score(500)
			return True
		elif l==[0,0,0,0,0,3]:
			self.scorer.add_score(600)
			return True
		elif _pattern(l,1,4):
			self.scorer.add_score(1000)
			return True
		elif _pattern(l,1,5):
			self.scorer.add_score(2000)
			return True
		elif _pattern(l,1,6):
			self.scorer.add_score(3000)
			return True
		elif l==[1,1,1,1,1,1]:
			self.scorer.add_score(1500)
			return True
		elif _pattern(l,2,3):
			self.scorer.add_score(2500)
			return True
		elif _pattern(l,3,2):
			self.scorer.add_score(1500)
			return True
		elif _pattern(l,1,4) and _pattern(l,1,2):
			self.scorer.add_score(1500)
			return True
		else:
			return False
	def scan(self,event):
		for s in self.sprites:
			if event.x in s.x_range and event.y in s.y_range and s.old==False:
				s.select()
				break
	def roll(g):
#		g.scorer.update()
		if not g.last:
			g.farkle=canvas.create_text(250,250,font=('Helvetica',20),text='FARKLE!',fill='white')
			g.scorer.add_farkle()
			g.last_farkle=True
			return
		g.last=False
		g.top_occupied=[0,0,0,0,0,0]
		for i in range(1,11):
			tk.update()
			time.sleep(0.1)
			for s in g.sprites:
				if s.selected==False:
					s.num=str(1+(i % 6))
					canvas.delete(s.widgets[1])
					canvas.delete(s.widgets[0])
					s.draw()
				else:
					s.old=True
		for s in g.sprites:
			if s.selected==False:
				s.num=str(random.randint(1,6))
				s.delete()
				s.sort()
				s.draw()
		g.occupied=[0,0,0,0,0,0]
		for s in g.sprites:
			if s.selected==False:
				s.delete()
				s.sort()
				s.draw()

class scorer:
	def __init__(self,game):
		self.g=game
		self.score=0
		self.round=0
		self.farkles=0
		self.temp_score=0
		self.score_widget=canvas.create_text(125,12,font=('Helvetica',12),text='score : '+str(self.score),fill='white')
		self.round_widget=canvas.create_text(250,12,font=('Helvetica',12),text='rounds : '+str(self.round),fill='white')
		self.farkle_widget=canvas.create_text(375,12,font=('Helvetica',12),text='farkles : '+str(self.farkles),fill='white')
	def update(self):
		self.temp_score=0
		self.round+=1
		canvas.delete(self.round_widget)
		self.round_widget=canvas.create_text(250,12,font=('Helvetica',12),text='rounds : '+str(self.round),fill='white')
	def add_farkle(self):
		self.farkles+=1
		self.add_score(-self.temp_score)
		if self.farkles >= 3:
			self.farkles=0
			self.add_score(-1000)
		canvas.delete(self.farkle_widget)
		self.farkle_widget=canvas.create_text(375,12,font=('Helvetica',12),text='farkles : '+str(self.farkles),fill='white')
	def remove_farkles(self):
		self.farkles=0
		canvas.delete(self.farkle_widget)
		self.farkle_widget=canvas.create_text(375,12,font=('Helvetica',12),text='farkles : '+str(self.farkles),fill='white')
	def add_score(self,score):
		self.temp_score+=score
		self.score+=score
		canvas.delete(self.score_widget)
		self.score_widget=canvas.create_text(125,12,font=('Helvetica',12),text='score : '+str(self.score),fill='white')

class die:
	def __init__(self,game):
		self.g=game
		self.num=str(6)
		self.sort()
		self.draw()
		self.selected=False
		self.old=False
	def draw(self):
		self.widgets=[
canvas.create_rectangle(self.x,self.y,self.x+25,self.y+25,outline='white'),
canvas.create_text(self.x+12,self.y+12,font=('Helvetica',8),text=self.num,fill='white')]
	def delete(self):
		for w in self.widgets:
			canvas.delete(w)
	def sort(self):
		self.x=int(self.num)*70-35
		self.y=450-(50*self.g.occupied[int(self.num)-1])
		self.g.occupied[int(self.num)-1]+=1
		self.x_range=list(range(self.x,self.x+25))
		self.y_range=list(range(self.y,self.y+25))
	def select(self):
		if self.selected==False:
			self.delete()
			self.y=25+50*self.g.top_occupied[int(self.num)-1]
			self.y_range=list(range(self.y,self.y+25))
			self.g.top_occupied[int(self.num)-1]+=1
			self.g.occupied[int(self.num)-1]-=1
			self.draw()
			self.selected=True
		else:
			self.delete()
			self.y=450-(50*self.g.occupied[int(self.num)-1])
			self.y_range=list(range(self.y,self.y+25))
			self.g.top_occupied[int(self.num)-1]-=1
			self.g.occupied[int(self.num)-1]+=1
			self.draw()
			self.selected=False


def _pattern(l,qty,value):
	var=0
	for index,elem in enumerate(l):
		if elem==value:
			var+=1
	if var==qty:
		return True
	return False

if __name__ == '__main__':
	new_game=game()
