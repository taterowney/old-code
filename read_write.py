#read_write.py

import os

class File:
	def __init__(self,filename):
		self.name=filename
		self.extension=self._get_ext()
		self.insert=True
#		self.cursor_pos=0
		if not os.path.exists(self.name):
			os.system('touch %s'% self.name)
			self.cursor_pos=0
		else:
			self.set_cursor('last')
	def set_cursor(self,pos):
		if type(pos)==str:
			if pos.lower()=='last':
				self.cursor_pos=len(self)-1
			elif pos.lower()=='first':
				self.cursor_pos=0
		else:
			self.cursor_pos=pos
		if self.cursor_pos >= len(self):
			raise IndexError('file %s is only %s long'% self.name,len(self)-1)
	def write(self,text):
		old=self.readlines()
		if self.insert==False:
			self.set_cursor('last')
		with open(self.name,'w') as _f:
			old.insert(self.cursor_pos,text)
#			print(old)
			_f.write('\n'.join(old))
			self.cursor_pos+=1
	def delete(self,*args):
		if args == ():
			self._del(self.cursor_pos)
			return
		for a in args:
			if type(a) == str:
				if a=='first':
					self._del(0)
				elif a=='last':
					self._del(len(self)-1)
				elif a=='all':
					with open(self.name,'w') as _f:
						_f.write('')
			elif type(a)==int:
				self._del(a)
			else:
				raise TypeError('invalid arguement for delete: %s'% a)
	def _del(self,val):
		text=self.readlines(newline=True)
		del text[val]
		with open(self.name,'w') as _f:
			_f.write(''.join(text))
	def remove(self,yes=False):
		if yes==False:
			ans=input('are you sure you want to remove file %s? (y/n) '% self.name).lower().startswith('y')
			if not ans:
				return
		os.system('rm %s'% self.name)
	def lines(self):
		with open(self.name,'r') as _f:
			return _f.readlines()
	def readlines(self,newline=False):
		if self.extension != '.csv':
			with open(self.name,'r') as _f:
				if newline==True:
					return _f.readlines()
				else:
					return _f.read().split('\n')
		else:
			return self.read_csv()
	def read(self):
		if self.extension != '.csv':
			with open(self.name,'r') as _f:
				return _f.read()
		else:
			return self.read_csv()
	def read_csv(self):
		title=True
		captions=[]
		ret={}
		with open(self.name,'r') as _f:
			lines=_f.read().split('\n')
			for l in lines:
				if l.startswith('#') or l=='':
					continue
				vals=l.strip().split(',')
				if title==True:
					for v in vals:
						ret[v]=[]
						captions.append(v)
					title=False
				else:
					for v,index in zip(vals,captions):
						ret[index].append(float(v))
		return ret
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name
	def __len__(self):
		return len(self.lines())
	def __getitem__(self,iind):
		return self.readlines()[ind]
	def __contains__(self,val):
		return val in self.readlines()
	def __delitem__(self,ind):
		self._del(ind)
	def type(self):
		return '"%s" file'% self.extension
	def _get_ext(self):
		l=list(self.name)
		for i in range(len(l)-1,-1,-1):
			if l[i]=='.':
				return ''.join(l[i:])
		return 'unmarked'

if __name__ == '__main__':
	f=File('new.csv')
#	print(f.read_csv())
	print(f.readlines())
