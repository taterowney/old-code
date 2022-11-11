import sys
try:
	import matplotlib.pyplot as plt
except ImportError:
	print("matplotlib for python3 not installed.")

class Plotter:
	def plot(self,*args):
		self.points=[]
		plt.xlabel('X axis')
		plt.ylabel('Y axis')
		for i in args:
			if i != None:
				if type(i) == list or type(i) == tuple:
				        self.points.append(list(i))
				elif type(i) == type(Vector([0,0])):
					self.points.append(i.coords)
				else:
					raise TypeError
		for p in range(len(self.points)):
        		plt.plot([0,self.points[p][0]],[0,self.points[p][1]],marker='o')
		plt.show()

plotter=Plotter()

class Vector:
	def __init__(self,pts):
		self.coords=pts
		self.dim='R'+str(len(pts))
		self.type='vector'
	def __len__(self):
		return len(self.coords)
	def __str__(self):
		return 'vector '+str(self.coords)+' in dimention '+self.dim
	def __repr__(self):
                return 'vector '+str(self.coords)+' in dimention '+self.dim
	def __getitem__(self,index):
		return '['+str(self.coords[index])+']'
	def __add__(self,other):
		if type(other)==type(self):
			if other.type==self.type:
				if self.dim==other.dim:
					ret=[]
					for i in range(len(self.coords)):
						ret.append(self.coords[i]+other.coords[i])
					return Vector(ret)
		raise TypeError('in vector addition , both elements must be vectors of the same dimention')
	def __sub__(self,other):
		if type(other)==type(self):
			if other.type==self.type:
				if self.dim==other.dim:
					ret=[]
					for i in range(len(self)):
						ret.append(self.coords[i]-other.coords[i])
					return Vector(ret)
		raise TypeError('in vector subtraction , both elements must be vectors of the same dimention')
	def __mul__(self,other):
		if type(other)==int:
			ret=[]
			for c in self.coords:
				ret.append(c*other)
			return Vector(ret)
		elif type(other) == type(IDENTITY):
			if other.type=='matrix':
				return other*self
		raise TypeError()
	def __div__(self,other):
		if type(other)==int:
			ret=[]
			for c in self.coords:
				ret.append(c/other)
			return Vector(ret)
		raise TypeError()

class Matrix:
	def __init__(self,ref=0,affine=None):
		self.type='matrix'
		if ref==0:
			h=input('enter height of matrix :')
			self.matrix=[]
			for i in range(0,h):
				vals=[]
				vals=input("line %s of matrix :" %eval("i+1"))
				if i==0:
					w=len(vals)
				self.matrix.append([])
				if len(vals)!=w:
					raise NameError('matrices must have equal length in all rows')
				for j in range(0,w):
					self.matrix[i].append(float(vals[j]))
		else:
			self.matrix=[]
			for i in range(len(ref)):
				self.matrix.append([])
				for j in range(len(ref[i])):
					self.matrix[i].append(float(ref[i][j]))
		self.width=len(self.matrix[0])
		self.height=len(self.matrix)
		self.rows=self.matrix
		self.cols=[]
		for i in range(self.width):
			self.cols.append([])
			for j in range(self.height):
				self.cols[i].append(self.matrix[j][i])
		if affine != None:
			self.affine_val=True
			if type(affine)==list:
				if len(affine)!=self.height:
					raise TypeError('affine vector must be the same height as matrix')
				self.affine=Vector(affine)
			else:
				try:
					if affine.type=='vector':
						self.affine=affine
				finally:
					raise TypeError('affine component of a matrix must be a list or Vector object')
		else:
			self.affine=Vector([0]*self.height)
			self.affine_val=False
	def show(self):
		ind=0
		for c in self.rows:
			if len(str(c)) > ind:
				ind=len(str(c))+3
		for i in range(0,self.height):
			val=' '*(ind-len(str(self.matrix[i]))+1)
			if self.affine_val==False:
				print(self.matrix[i])
			else:
				if i==round((self.width)/2):
					val=' '*(ind-len(str(self.matrix[i]))-1)+'+'
				print(str(self.matrix[i])+val+str(self.affine[i]))
	def apply(self,vector,mod=0):
		vector=vector.coords
		if len(vector)!=self.height:
			raise TypeError('vector of length %s is not compatable with a matrix of height %s'% (str(len(vector)),str(self.height)))
		rval=[]
		for i in range(0,self.width):
			x=0
			for j in range(0,self.height):
				y=self.matrix[j][i]
				x=x+(y*vector[j])
			rval.append(x)
		if self.affine_val==False:
			return Vector(rval)
		else:
			return Vector(rval)+self.affine
	def __str__(self):
		self.show()
		return ''
	def __repr__(self):
                self.show()
                return ''
	def __getitem__(self,index1):
		if type(index1)==tuple:
			return self.matrix[index1[0]][index1[1]]
		else:
			return self.matrix[index1]
	def __eq__(self,other):
		if type(other) == type(IDENTITY):
			if self.type==other.type:
				if self.matrix == other.matrix:
					return True
		return False
	def __ne__(self,other):
		if self==other:
			return False
		else:
			return True
	def __invert__(self):
		inv=getMatrixInverse(self.matrix)
		if inv==None:
			return None
		return Matrix(inv)
	def __add__(self,other):
		ret=_add(self,other,1)
		return ret
	def __sub__(self,other):
		return _sub(self,other)
	def __mul__(self,other):
		if type(other) == int or type(other) == float:
			return self._mul_const(float(other))
		elif type(self) == int or type(self) == float:
			other._mul_const(float(self))
		elif type(other) == type(IDENTITY):
			if other.type == 'matrix':
				return _mul(self,other)
		elif type(other) == type(Vector([0,0])):
			if other.type == 'vector':
				return self.apply(other)
	def __truediv__(self,other):
		ret=~other
		if ret==None:
			return None
		else:
			ret=self*ret
			return ret
	def _mul_const(self,fl):
		ret=[]
		for line in range(len(self.matrix)):
			ret.append([])
			for elem in self.matrix[line]:
				ret[line].append(float(elem)*fl)
		ret=Matrix(ret)
		return ret
	def __pow__(self,other):
		ret=self
		for i in range(other-1):
			ret*=ret
		return ret
	def __len__(self):
		print(str(self.width)+' by '+str(self.height))
		return len(self.matrix) * len(self.matrix[0])

IDENTITY=Matrix([[1,0],[0,1]])

def transposeMatrix(m):
	return map(list,zip(*m))

def getMatrixMinor(m,i,j):
	return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
	#base case for 2x2 matrix
	if len(m) == 2:
		return m[0][0]*m[1][1]-m[0][1]*m[1][0]
	determinant = 0
	for c in range(len(m)):
		determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
	return determinant

def getMatrixInverse(m):
	if len(m) != len(m[0]):
		return None
	determinant = getMatrixDeternminant(m)
	if determinant == 0:
		return None
	if len(m) == 2:
		return [[m[1][1]/determinant, -1*m[0][1]/determinant], [-1*m[1][0]/determinant, m[0][0]/determinant]]
	#find matrix of cofactors
	cofactors = []
	for r in range(len(m)):
		cofactorRow = []
		for c in range(len(m)):
			minor = getMatrixMinor(m,r,c)
			cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
		cofactors.append(cofactorRow)
	cofactors = transposeMatrix(cofactors)
	for r in range(len(cofactors)):
		for c in range(len(cofactors)):
			cofactors[r][c] = cofactors[r][c]/determinant
	return cofactors

def _add(MI,MII,mode=0):
	if(MI.height==MII.height and MI.width==MII.width):
		rval=[[0]*MI.width for p in range(MI.height)]
		ls=[]
		for i in range(0,MI.height):
			for j in range(0,MI.width):
				x=MI.matrix[i][j]
				y=MII.matrix[i][j]
				z=x+y
				if(mode==0):
					ls.append(z)
				else:
					rval[i][j]=z
			if mode==0:
				print(ls)
				ls=[]
		if mode==1:
			ret=Matrix(rval,(MI.affine+MII.affine).coords)
			return ret
	else:
		raise TypeError("you cannot add matricies of different sizes!")

def _sub(_m1,_m2):
	ret=[]
	if _m1.height!=_m2.height or _m1.width!=_m2.width:
		raise TypeError("you cannot subtract matricies of different sizes!")
	for i in range(_m1.height):
		ret.append([])
		for j in range(_m1.width):
			ret[i].append(_m1.matrix[i][j] - _m2.matrix[i][j])
	return Matrix(ret,(_m1.affine-_m2.affine).coords)

def _mul(_m1,_m2):
	ret=[]
	if _m1.height!=_m2.width or _m1.width!=_m2.height:
		raise TypeError("you cannot multiply matricies of incompatible sizes!")
	n=_m1.width
	for i in range(_m1.height):
		ret.append([])
		for j in range(n):
			val=0
			for k in range(n):
				val+=(_m1[i][k])*(_m2[k][j])
			ret[i].append(float(val))
	ret=Matrix(ret)
	return ret

identities=[None,None,Matrix([[1,0],[0,1]]),Matrix([[1,0,0],[0,1,0],[0,0,1]]),Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]),Matrix([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]),Matrix([[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]])]

if __name__ == '__main__':
#	plotter.plot(Vector([1,2]),Vector([3,4]),Vector([5,6]))
#	print(Matrix([[1,2],[3,4],[5,6]],[5,6,7])-Matrix([[1,2],[3,4],[5,6]],[5,6,7]))
	m=Matrix([[1,2],[3,4000]],[5,6])
	print(m)
