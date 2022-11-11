from sympy import Symbol,factor,expand,sympify,solve,pprint
from sympy.core.sympify import SympifyError
x=Symbol('x')
import random,rand
random.seed(rand.rand_int(0,100))

def question(coef=1):
	expr=(x-random.randint(-8,8))*(x-random.randint(-8,8))*coef
#	modes=['What are the roots of ','Factor ']
	modes=['Factor ']
	random.shuffle(modes)
#	print(modes)
	if modes[0]=='Factor ':
		if get_ans(expr,modes[0])==expr:
			pprint('Correct!')
		else:
			pprint('Incorrect. :(')
	else:
#		print(sort(solve(expr)))
		if sort(get_ans(expr,modes[0]))==sort(solve(expr)):
			pprint('Correct!')
		else:
			pprint('Incorrect. :(')
def get_ans(expr,mode):
	try:
		if mode=='Factor ':
			pprint(mode+'%s'% expand(expr))
			ans=factor(expand(sympify(input('> '))))
			print(ans)
		else:
			ans=list_int(input(mode+'%s: '% str(expand(expr))).split(','))
#			print(ans)
	except SympifyError:
		print('Invalid input. Try again.')
		ans=get_ans(expr,mode)
		return ans
	except KeyboardInterrupt:
		pass
	return ans

def list_int(l):
	ret=[]
	for elem in l:
		ret.append(int(elem))
	return ret

def sort(l):
	l.sort()
	return l

if __name__ == '__main__':
	for i in range(4):
		question(coef=random.randint(1,4))
