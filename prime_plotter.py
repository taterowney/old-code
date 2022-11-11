from num_archive import get_primes

max=1000

P=[]
dict_P=get_primes()
for val in dict_P:
	P.append(val)

import matplotlib.pyplot as plt

print('calculating...')

x=list(range(0,max))
y1=[]
y2=[]

for n in range(0,max):
	y1.append((2*P[n]))
	y2.append(P[n+1])

print('done')

plt.plot(x,y1,x,y2)
plt.title('Prime Comparison up to %sth Prime'% str(max))
plt.legend(['2 x P[n]','P[n+1]'])
plt.show()
