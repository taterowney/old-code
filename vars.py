from read_write import *

def uppercase(l):
	ret=[]
	for elem in l:
		ret.append(elem.upper())
	return ret

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet=letters+uppercase(letters)

def record(file,**kwargs):
	f=File(file+'.py')
	for k in kwargs:
		f.write('global '+k)
		f.write(k+' = '+form(kwargs[k]))

def form(val):
	st=False
	for char in alphabet:
		if char in str(val):
			st=True
	if st:
		return '\"'+str(val)+'\"'
	else:
		return str(val)

#def execute(f):
#	f=File(file)
#	exec('from '+str(f)+' import *')
#	print(f.readlines())
#	for l in f.readlines():
#		if l != '':
#			exec('print(l)')
#			exec(l)
#			exec("global bar")
#			exec("bar=1")

if __name__ == '__main__':
#	l=[form(1),form('hello')]
	record('stuff',bar=1,foo='blah')
	from stuff import *
