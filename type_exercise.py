from lists import separate
from random import randint,seed
import random
import time
from rand import rand_int
import sys
seed(rand_int(0,100))

def sents(rand):
	things=[' the Raspberry Pi',' a Five Crown game',' a Rubick`s cube']
	pronouns=[' you',' him',' her',' them',' me',' all of them']
	sent2=[' lost the game',' knows'+pronouns[random.randint(0,len(pronouns)-1)],' owns'+things[random.randint(0,len(things)-1)],' used'+things[random.randint(0,len(things)-1)]]
	sent2_2=[' lost the game',' know'+pronouns[random.randint(0,len(pronouns)-1)],' own'+things[random.randint(0,len(things)-1)],' used'+things[random.randint(0,len(things)-1)]]
	sents=['I'+sent2_2[random.randint(0,len(sent2_2)-1)],'You'+sent2_2[random.randint(0,len(sent2_2)-1)],'She'+sent2[random.randint(0,len(sent2)-1)],'He'+sent2[random.randint(0,len(sent2)-1)],'They'+sent2_2[random.randint(0,len(sent2_2)-1)],'They all'+sent2_2[random.randint(0,len(sent2_2)-1)]]
	return sents[randint(0,len(sents)-1)]+'.'

def ask(rand):
	try:
		global words,mistakes
		sent=sents(rand)
		print(sent)
		words+=len(separate(sent,' '))
		inp = input('>> ')
		if inp==sent:
			return True
		else:
			print('try again')
			mistakes+=1
			return False
	except KeyboardInterrupt:
		sys.exit()

t1=time.time()
words=0
mistakes=0

l=int(input('enter length of exercise : '))
for i in range(l):
	end=False
	rand=randint(0,5)
	val=round((time.time()-t1)*1000+randint(0,25))
	while end==False:
		seed(val)
		end=ask(rand)

t2=time.time()
mins=(t2-t1)/60
wpm=round(words/mins)
print('words per minute : ~ '+str(wpm))
print('mistakes : '+str(mistakes))
