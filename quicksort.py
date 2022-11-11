import random
def QS(elems):
	if len(elems)==1 or len(elems)==0:
		return elems,[]
	pivot=elems[int(len(elems)/2)]
	new_1=[]
	new_2=[]
	for e in range(len(elems)):
		if elems[e] > pivot:
			new_2.append(elems[e])
		elif elems[e] < pivot:
			new_1.append(elems[e])
		else:
			if len(new_1)==0:
				new_1.append(elems[e])
			else:
				if len(new_2)>0:
					l=[elems[e]]
					new_2=l+new_2
				else:
					new_2.append(elems[e])
	return new_1,new_2

def is_sorted(elems):
	if len(elems)==0:
		return False
	val=elems[0]
	for i in elems:
		if val <= i:
			val=i
		else:
			return False
	return True

def quicksort(elems):
	ret=[]
	e1,e2=QS(elems)
#	print(e1,e2)
	if e1==[]:
		return e2
	if e2==[]:
		return e1
	if is_sorted(e1)==True:
		for e in e1:
			ret.append(e)
	else:
#		print('for e1')
		e1_2=quicksort(e1)
		for e in e1_2:
			ret.append(e)
	if is_sorted(e2)==True:
		for e in e2:
			ret.append(e)
	else:
#		print('for e2')
		e2_2=quicksort(e2)
		for e in e2_2:
			ret.append(e)
	return ret

if __name__ == '__main__':
	l=[]
	random.seed(45)
	for i in range(100):
		l.append(random.randint(0,25))
	print(quicksort(l))

