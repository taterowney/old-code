def find(listI,element):
	try:
		for i in range(0,len(listI)):
			if listI[i] is element:
				return i
		raise NameError
	except TypeError:
		print('input 1 must be a list')

def associate(LI,LII):
	try:
		if len(LI) is not len(LII):
			raise TypeError
		dictI={}
		for i in range(0,len(LI)):
			dictI[LI[i]]=LII[i]
		return dictI
	except TypeError:
		print('both inputs must be lists or touples')

def is_in(string,element):
	L=list(string)
	for i in range(0,len(L)):
		if element is L[i]:
			return 1
	return 0

def replace(e1,e2,string):
	string=list(string)
	for i in range(len(string)):
		if e1 is string[i]:
			string[i]=e2
	ret=''
	for i in range(len(string)):
		ret=ret+string[i]
	return ret

def takeout(element,string):
	L=list(string)
	var=0
	for i in range(0,len(L)):
		if L[var] is element:
			del L[var]
			var=var-1
		var=var+1
	ret=''
	for i in range(0,len(L)):
		ret=ret+L[i]
	return ret

def separate(string,separator):
	L=list(string)
	rets=[]
	var=0
	ctr=0
	for i in range(len(L)):
		if L[var] is separator:
			ret=[]
			val=var+1
			for j in range(val):
				ret.append(L[0])
				del(L[0])
			ret=Lstr(ret)
			rets.append(ret)
			var=0
			ctr=ctr+1
		else:
			var=var+1
	rets.append(Lstr(L))
	return rets

def Lstr(lst):
	ret=''
	for i in range(len(lst)):
		ret=ret+str(lst[i])
	return ret

def contains(chars,str):
	str=list(str)
	chars=list(chars)
	if len(chars)==0:
		if len(str)==0:
			return True
		else:
			return False
	if len(str)==0:
		return True
	for c in range(len(chars)):
			yes=0
			if chars[c]==str[0]:
				yes=1
				for C in range(len(str)):
					if len(chars) <= c+C:
						yes=0
					else:
						if not chars[c+C]==str[C]:
							yes=0
			if yes==1:
				return True
	return False

def split(list,thepivot,pivot=True):
	for index,val in enumerate(list):
		if val == thepivot:
			if pivot == False:
				ret1=list[:index]
				ret2=list[index+1:]
			else:
				ret1=list[:index+1]
				ret2=list[index+1:]
			break
	return ret1,ret2

if __name__ == '__main__':
	print(split([1,2,3,4,5,6],3,pivot=False))
