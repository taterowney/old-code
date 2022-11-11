#!/usr/bin/python3
import time

def _rand_int():
	t1=time.time()
	low=input('enter lower bound:')
	up=input('enter upper bound:')
	dif=up-low
	t2=time.time()
	T=(t2-t1)*1000
	T=int(round(T % dif))
	T=T+low
	return T

def __rand_int(low,high):
	t1=time.time()
	dif=high-low
	input('press enter to continue:')
	t2=time.time()
	T=(t2-t1)*1000
	T=int(round(T % dif))
	T=T+low
	return T

def rand_int(low,high):
	diff=high-low
	return round((time.time()-int(time.time()))*100000) % diff + low

if __name__ =='__main__':
	print(rand_int(55,1023))
