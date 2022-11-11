import sys
try:
        import matplotlib.pyplot as plot
except ImportError:
        print("matplotlib for python 3.5 has not been installed. Try 'sudo pip3 install matplotlib'")

class Plotter:
        def plot(self,*args):
                plt.xlabel('X axis')
                plt.ylabel('Y axis')
                self.points=[]
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
        def __getitem__(self,index):
                return self.coords[index]
        def __len__(self):
                return len(self.coords)
        def __str__(self):
                return 'vector '+str(self.coords)+' in dimention '+self.dim
        def __repr__(self):
                return 'vector '+str(self.coords)+' in dimention '+self.dim
        def __add__(self,other):
              if type(other)==type(self):
                   if other.type==self.type:
                         if self.dim==other.dim:
                                        ret=[]
                                        for i in range(len(self)):
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
                elif type(other) == type(Matrix([[1,2],[3,4]])):
                        if other.type=='matrix':
                                return other*self
                elif type(self)==type(other):
                        return mul_obj(self,other)
                elif type(other)==type(mul_obj(Vector([1,1,1]),Vector([1,1,1]))):
                        return other*self
                raise TypeError('In vector multiplication, a vector must be multiplied by another vector, a scaler (int or float), or a matrix, not %s'% str(type(other)))
        def __div__(self,other):
                if type(other)==int:
                        ret=[]
                        for c in self.coords:
                                ret.append(c/other)
                        return Vector(ret)
                raise TypeError()
        def __abs__(self):
                sum=0
                for c in self.coords:
                        sum+=c**2
                return sum**0.5

class mul_obj:
	def __init__(self,v1,v2):
		self.components=[v1,v2]
		if type(v1)==type(self) and type(v2)==type(Vector([1,1])):
			val=list(v1)+[v2.coords]
			self.cross_product=self.x_prod(*val)
			self.components=val
		elif type(v1)== type(self) and type(v2)== type(self):
			val=[*list(v1),*list(v2)]
			self.cross_product=self.x_prod(*val)
			self.components=val
		else:
			v1=v1.coords
			v2=v2.coords
			self.components=[v1,v2]
			self.cross_product=self.x_prod(v1,v2)
			self.dot_product=self.dot_prod(v1,v2)
			self.outer_product=self.O_prod(v1,v2)
	def __list__(self):
		return self.components
	def __getitem__(self,index):
		return self.components[index]
	def __mul__(self,other):
		if type(other) == type(Vector([1,1])) or type(other) == type(self):
			return mul_obj(self,other)
		else:
			raise TypeError
	def x_prod(self,*args):
		val=len(args[0])
		for a in args:
			if len(a) != val:
				return None
#				raise TypeError('For a cross product, all vectors must be of the same dimention')
		if val != len(args)+1:
			return None
		vectors=getBasisVectors(len(args)+1)
		ret=[[]*1 for k in range(len(args)+1)]
		for i in range(len(ret)):
			ret[0].append(vectors[i])
		for row in range(1,len(ret)):
			for elem in range(len(args[0])):
				ret[row].append(args[row-1][elem])
		return det(Matrix(ret))
	def dot_prod(self,v1,v2):
		if len(v1) != len(v2):
			return None
		sum=0
		for u,v in zip(v1,v2):
			sum+=u*v
		return sum
	def O_prod(self,v1,v2):
		ret=[[]*1 for i in range(len(v1))]
		for i in range(len(v1)):
			for j in range(len(v2)):
				ret[i].append(v1[i]*v2[j])
		return Matrix(ret)

class Matrix:
        def __init__(self,ref=0,affine=None):
                self.type='matrix'
                if ref == 0:
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
                                        self.matrix[i].append(ref[i][j])
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
        def _show(self):
                for i in range(0,self.height):
                    print(self.matrix[i])
        def show(self):
                height=self.height
                max_lens=[1 for i in range(height)]
                width=0
                affine_width=0
                for w in self.rows:
                        if len(str(w)) > width+1:
                                width=len(str(w))-1
                        for index,val in enumerate(w):
                                if len(str(val)) > max_lens[index]:
                                        max_lens[index]=len(str(val))
                sum=0
                for val in range(len(max_lens)):
                        newsum=max_lens[val]
                        max_lens[val]+=sum
                        sum+=newsum
                sum=0
                for val in range(len(max_lens)):
                        max_lens[val]+=sum
                        sum+=2
                print(max_lens)
                for a in list(self.affine):
#                        affine_width=len(str(a))
                        if len(str(a)) > affine_width+1:
                                affine_width=len(str(a))
                if not self.affine_val:
                        affine_width=0
                grid=[[[' ']*1 for j in range(width+7+affine_width)]*1 for i in range(height)]
                for h in range(height):
#                       for index,val in enumerate(max_lens):
#                               grid[h][val]=str(self.matrix[h][index])
                        num=0
                        for index,char in enumerate(list(str(self.matrix[h]))):
                                if (len(char)-1+index)==max_lens[num]:
                                        print(index)
                                        num+=1
                        grid[h][0]='['
                        grid[h][width]=']'
                        if affine_width > 0:
                                grid[h][width+4]='['
                                grid[h][width+5+affine_width]=']'
#                                for char,space in zip(list(self.affine[h]),range(width+5,len(list(self.affine[h]))*3,3)):
#                                        grid[h][space]=str(char)
#                        for char,space in zip(self.matrix[h],range(1,len(my_str(self.matrix[h]))*3,3)):
#                                grid[h][space]=str(char)
                self.conc(grid)
        def conc(self,l):
                for sub in l:
                        val=''
                        for piece in sub:
                                val+=piece[0]
                        print(val)
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
                if type(other) == type(Matrix([[1,1],[1,1]])):
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
                elif type(other) == type(Matrix([[1,1],[1,1]])):
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
#                print(str(self.width)+' by '+str(self.height))
                return len(self.matrix) * len(self.matrix[0])
        def __list__(self):
                return self.coords
def det(m):
        return getMatrixDeternminant(list(m))

class ids:
	def __getitem__(self,index):
		return Matrix(GBV(index))

IDENTITIES=ids()

def GBV(dim):
	ret=[]
	for i in range(dim):
		ret.append([0]*dim)
		ret[i][i]=1
	return ret

def getBasisVectors(dim):
	ret=[]
	for v in GBV(dim):
		ret.append(Vector(v))
	return ret

def transposeMatrix(m):
        return map(list,zip(*m))

def getMatrixMinor(m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
        #base case for 2x2 matrix
        if len(m) == 2:
                return m[0][0]*m[1][1]-m[0][1]*m[1][0]
        determinant = 0
        vec_det=Vector([0]*len(m))
        val=1
        for c in range(len(m)):
                if type(m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))*((-1)**c))==int:
                        val=0
                        determinant += m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))*((-1)**c)
                else:
                        vec_det += m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))*((-1)**c)

        if val==0:
                return determinant
        else:
                return vec_det

def getMatrixInverse(m):
        if len(m) != len(m[0]):
                return None
        determinant = getMatrixDeternminant(m)
        #special case for 2x2 matrix:
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
                if mode==1 :
                        ret=Matrix(rval)
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
        _m3=Matrix(ret)
        return _m3

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

def my_str(l):
        ret=''
        for elem in l:
                ret+=str(elem)
        return l

if __name__ == '__main__':
#        m=Matrix([[Vector([1,0,0]),Vector([0,1,0]),Vector([0,0,1])],[3,4,5],[1,2,3]])
        m=Matrix([[0,1,2],[13,4,5],[1,2,3]],[3,8,9])
#        print(getBasisVectors(4))
#        M=mul_obj(Vector([1,2,3,4]),Vector([6,5,5,6]))*Vector([-7,-8,-9,-10])
#        print(M.cross_product)
#        M=mul_obj(Vector([1,2,3,4,5]),Vector([3,4,5,6,7]))*mul_obj(Vector([1,2,3,4,5]),Vector([3,4,5,6,7]))
#        print(M.cross_product)
#        print((Vector([1,5,7])*Vector([6,3,4])).cross_product)
#        print((Vector([1,5,7])*Vector([6,3,4])).dot_product)
#        print((Vector([1,2,3,4])*Vector([6,5,5,6])*Vector([-7,-8,-9,-10])).cross_product)
        m.show()
