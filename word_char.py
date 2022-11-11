import sys
with open(sys.argv[1],'r') as f:
	val=f.read().split(' ')
print(val,len(val))
