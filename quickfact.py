from num_archive import get_primes

primes=get_primes()

def factor(val):
	ret=[]
	if len(list(str(val))) > 21:
		raise ValueError('cannot factor numbers this big')
	for p in primes:
		if val/p == val//p:
			if p != val:
				f1=val/p
				f2=p
				if f1 in primes:
					ret.append(int(f1))
					ret.append(f2)
				else:
					var=factor(f1)
					for i in range(len(var)):
						ret.append(int(var[i]))
					ret.append(f2)
				break
	if ret==[]:
		ret.append(val)
		if len(ret) == 1:
			ret.append(1)
	ret.sort()
	return ret

if __name__ == '__main__':
	print(factor(1507))
