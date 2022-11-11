import math,random,num_archive

global primes
primes=num_archive.get_primes()

def rabinMiller(num):
	if num % 2 == 0 or num < 2:
		return False
	if num == 3:
		return True
	s=num-1
	t=0
	while s % 2 == 0:
		s=s//2
		t+=1
	for tries in range(50):
		a=random.randrange(2,num-1)
		v=pow(a,s,num)
		if v != 1:
			i=0
			while v != (num-1):
				if i == (t-1):
					return False
				else:
					i+=1
					v=(v ** 2) % num
	return True

def isPrime(num):
	if num < 2:
		return False
	for p in primes:
		if (num % p) == 0:
			return False
	return rabinMiller(num)

def generateLargePrime(keysize=1024):
	while True:
		num = random.randrange(2**(keysize-1),2**(keysize))
		if isPrime(num):
			return num
