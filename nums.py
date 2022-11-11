#!/usr/bin/python3
import math
def num_archive():
	file=open("num_archive.py",'w')
	file.write('def get_primes:\n')
	file.write('        primes={2:0,3:0')
	for i in range(5,100002):
		prime=1
		for j in range(2,int(math.ceil(i**0.5)+1)):
			if i/j == int(i/j):
				prime=0
		if prime == 1:
			file.write(','+str(i)+':0')
	file.write('}\n')
	file.write('        return primes')
	file.close()

if __name__ == '__main__':
	num_archive()

