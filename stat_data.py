#! /usr/bin/python3
try:
	import matplotlib.pyplot as plt
except ImportError:
	print('matplotlib for python3.5 not installed. Try "pip3 install matplotlib".')
from collections import Counter
from quicksort import quicksort
from histo import histogram
import random

class data_set:
	def __init__(self,*args,data=None,data_types=None):
		self.data_types=data_types
		if data==None:
			self.data=args
		else:
			self.data=data
		self.datapoints=quicksort(self.data)
		self.frequencies=[]
		cat=None
		for index,d in enumerate(self.datapoints):
			if index==0:
				self.frequencies.append(1)
			elif self.datapoints[index] - self.datapoints[index-1] > 1:
				val=self.datapoints[index] - self.datapoints[index-1] - 1
				for v in range(val+1):
					self.frequencies.append(0)
			elif self.datapoints[index-1]!=self.datapoints[index]:
				self.frequencies.append(1)
			else:
				self.frequencies[len(self.frequencies)-1]+=1
	def __str__(self):
		return str(self.data)
	def __repr__(self):
		return str(self.data)
	def __len__(self):
		return len(self.datapoints)
	def _sort(self):
		self.datapoints=quicksort(self.data)
	def append(self,other):
		if type(other)==type(self):
			self.data=self.data+other.data
		elif type(other)==type(4):
			self.data.append(other)
		else:
			raise TypeError("unsupported operand types for 'append': 'data_set' and %s"% type(other))
		self._sort()
	def __add__(self,other):
		if type(other)==type(self):
			data=[]
			for a,b in zip(self.data,other.data):
				data.append(a+b)
			return data_set(data=data)
		elif type(other)==type(4):
			return data_set(data=self.data+[other])
		else:
			raise TypeError("unsupported operand types for + operator: 'data_set' and %s"% type(other))
	def __sub__(self,other):
		if type(other)==type(self):
			data=[]
			for a,b in zip(self.data,other.data):
				data.append(a-b)
			return data_set(data=data)
		elif type(other)==type(4):
			data=self.data
			var=0
			for d in range(len(data)):
				if data[var]==other:
					del data[var]
				else:
					var+=1
			return data_set(data=data)
		else:
			raise TypeError("unsupported operand types for - operator: 'data_set' and %s"% type(other))
	def __mul__(self,other):
		data=[]
		if type(other)==type(self):
			for a,b in zip(self.data,other.data):
				data.append(a*b)
			return data_set(data=data)
		elif type(other)==type(4):
			datapoints=self.data
			for d in datapoints:
				data.append(d*other)
			return data_set(data=data)
		else:
			raise TypeError("unsupported operand types for * operator: 'data_set' and %s"% type(other))
	def __truediv__(self,other):
		if type(other)==type(4):
			ret=[]
			val=0
			for i in range(0,other-1):
				ret.append([])
				for j in range(round(len(self)/other)):
					ret[i].append(self[val])
					val+=1
				ret[i]=data_set(data=ret[i])
			k=[]
			for i in range(val,len(self)):
				k.append(self[i])
			ret.append(data_set(data=k))
			return ret
		else:
			raise TypeError("unsupported operand types for / operator: 'data_set' and %s"% type(other))
	def __pow__(self,power):
		ret=[]
		for d in self.data:
			ret.append(d**power)
		return data_set(data=ret)
	def sum(self):
		return sum(self.datapoints)
	def __getitem__(self,ind):
		return self.data[ind]
	def __setitem__(self,index,val):
		if type(val)==int or type(val)==float:
			self.data[index]=val
			self._sort()
		else:
			raise TypeError
	def __delitem__(self,index):
		del self.data[index]
		self._sort()
	def __contains__(self,val):
		if val in self.datapoints:
			return True
		return False
	def __eq__(self,other):
		if type(other) == type(self):
			if self.datapoints==other.datapoints:
				return True
		return False
	def __ne__(self,other):
		if self == other:
			return False
		return True
	def __gt__(self,other):
		if type(self)==type(other):
			if len(self) > len(other):
				return True
			return False
		raise TypeError
	def __lt__(self,other):
		if self > other:
			return False
		return True
	def __ge__(self,other):
		if self > other or self == other:
			return True
		return False
	def __le__(self,other):
		if self > other:
			return False
		return True
	def get_percentile(self,val):
#		n=99
#		classes=[]
#		a=(max(self)-min(self))/n
#		for i in range(n):
#			classes.append([i*a,(i+1)*a])
#		if val < min(self):
#			return 1
#		for index,c in enumerate(classes):
#			if c[0] <= val and val < c[1]:
#				return index+1
#		return 99
		val=float(val)
		if val <= min(self):
			return 1
		for i in range(1,100):
			if self.at_percentile(i) >= val and self.at_percentile(i-1) < val:
				return i
		return 99
	def mean(self):
		return sum(self.datapoints)/len(self.datapoints)
	def median(self):
		nums=self.datapoints
		N=len(nums)
		if N % 2 ==0:
			m1=N/2
			m2=(N/2)+1
			m1=int(m1)-1
			m2=int(m2)-1
			med=float(nums[m1]+nums[m2])/2
		else:
			m=(N+1)/2
			m=int(m)-1
			med=nums[m]
		return med
	def quartiles(self):
		Q1=self.at_percentile(25)
		Q3=self.at_percentile(75)
		return Q1,self.median(),Q3
	def mode(self):
		c=Counter(self.datapoints)
		freq=c.most_common()
		max=freq[0][1]
		modes=[]
		for num in freq:
			if num[1] == max:
				modes.append(num[0])
		return modes
	def closest_to(self,var):
		d=self.datapoints
		if var < min(self):
			return min(self),0,min(self),0
		for i in range(len(d)):
			if var==d[i]:
				return d[i],i,d[i],i
			elif i+1 < len(self):
				if var > d[i] and var < d[i+1]:
					return d[i],i,d[i+1],i+1
		return max(self),len(self)-1,max(self),len(self)-1
	def range(self):
		return min(self),max(self),max(self)-min(self)
	def at_percentile(self,p):
		i=((len(self)*p)/100)-0.5
		if float(int(i))==i:
			return self.datapoints[int(i)]
		else:
			k=int(i)
			f=i-int(i)
			return (1-f)*self.datapoints[k] + f*self.datapoints[k+1]
	def varience(self):
		sq_diff=[]
		for p in self.datapoints:
			sq_diff.append((p-self.mean())**2)
		return sum(sq_diff)/len(self.datapoints)
	def standard_deviation(self):
		return self.varience()**0.5
	def graph(self,sh=True):
		if self.data_types==None:
			histogram(self.frequencies,list(range(min(self),max(self)+1)),show=sh)
		else:
			histogram(self.frequencies,self.data_types,show=sh)
	def all_stats(self,show=True):
		print('\n\nTotal Length:\t\t'+str(len(self)))
		min,max,range=self.range()
		print('\nRange:\t\t\t'+str(range))
		print('Minimum:\t\t'+str(min))
		print('Maximum:\t\t'+str(max))
		print('\nMean:\t\t\t'+str(self.mean()))
		Q1,Q2,Q3=self.quartiles()
		print('\nFirst Quartile:\t\t'+str(Q1))
		print('Median:\t\t\t'+str(Q2))
		print('Third Quartile:\t\t'+str(Q3))
		print('\nMode(s):\t\t'+str(self.mode()))
		v=self.varience()
		print('\nVarience:\t\t'+str(v))
		print('Standard Deviation:\t'+str(v**0.5))
		self.graph(sh=show)

def correlation_coefficient(x,y):
	n=len(x)
	if n != len(y):
		raise TypeError('To correlate two sets, they must be of the same length.')
#	if x.sorted==True or y.sorted==True:
#		raise TypeError('Correlation doesn`t work on sorted sets.')
	return ((n*sum(x*y))-(sum(x)*sum(y)))/((((n*sum(x**2))-(sum(x)**2))*((n*sum(y**2))-(sum(y)**2)))**0.5)

def compare_and_correlate(x,y):
	x.all_stats(show=True)
	y.all_stats(show=True)
	print('\n\nPearson Correlation Coeficient:\t'+str(correlation_coefficient(x,y)))
	plt.scatter(x,y,marker='+')
	plt.show()

if __name__ == '__main__':
	set1=data_set(data=[random.randint(0,20) for i in range(50)])
	set2=data_set(data=[random.randint(1,9) for i in range(50)])
	set3=data_set(data=[1,2,3,4,5,6,7,8,9],data_types=['a','b','c','d','e','f','g','h','i'])
#	print(set2.get_percentile(5)==set2.get_percentile(5))
	set3.graph()
