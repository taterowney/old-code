#! /usr/bin/python2.7
from collections import Counter
from lists import takeout,separate,Lstr

def gcd(a,b):
	while a != 0:
		a,b=b % a,a
	return b

def findModInverse(a,m):
	if gcd(a,m) != 1:
		return None
	u1,u2,u3=1,0,a
	v1,v2,v3=0,1,m
	while v3 != 0:
		q=u3//v3
		v1,v2,v3,u1,u2,u3=(u1 - q * v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
	return u1 % m

def round_to(num,place):
	if str(place).endswith('1')==False and place < 1:
		raise AttributeError('%s not a valid place value'% place)
	if place > 1 and str(place).startswith('1')==False:
		raise AttributeError('%s not a valid place value'% place)
	val=num*(1/place)
	val=round(val)*place
	return val

def tetrate(inI,inII):
	ret=inI
	for i in range(1,inII):
		ret=ret**inI
	return ret

def operation(in1,in2,dim):
	if dim == 4:
		return tetrate(in1,in2)
	elif dim > 4:
		ret=in1
		d=dim-1
		val=in2-1
		for i in range(val):
#			ret=tetrate(ret,in1)
			ret=operation(ret,ret,d)
		return ret
	else:
		raise TypeError

def mean(nums):
	s=sum(nums)
	N=len(nums)
	ret=s/N
	return ret

def median(nums):
	N=len(nums)
	nums.sort()
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

def mode(nums):
	c=Counter(nums)
	freq=c.most_common(5)
	max=freq[0][1]
	modes=[]
	for num in freq:
		if num[1] == max:
			modes.append(num[0])
	return modes

if __name__ == '__main__':
	print(round_to(22345,10))
	print(round_to(23.525267264,0.01))

