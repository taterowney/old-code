import rand
import random
random.seed(rand.rand_int(0,100))

print('strategy I : always choose previous guess')
wins=0
losses=0
for i in range(0,500):
	prize=random.randint(0,2)
	guess=random.randint(0,2)
	doors=[False,False,False]
	doors[prize]=True
	if doors[guess]==True:
		wins+=1
	else:
		losses+=1
print('		wins : %s'% str(wins))
print('		losses : %s' % str(losses))
print('		probability of winning with this strategy : %s' % str(wins/(losses+wins)))

random.seed(rand.rand_int(0,100))
print('strategy II : always choose opposite of previous guess')
wins=0
losses=0
for i in range(0,500):
	prize=random.randint(0,2)
	guess=random.randint(0,2)
	doors=[False,False,False]
	doors[prize]=True
	if doors[guess]==True:
		losses+=1
	else:
		wins+=1
print('		wins : %s'% str(wins))
print('		losses : %s' % str(losses))
print('		probabiltiy of winning with this strategy : %s' % str(wins/(losses+wins)))

