from read_write import *
from histo import histogram
#from matplotlib import pylab
#from pylab import plot,show
#from stat_data import *
from lists import associate
chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet=chars+' '.join(chars).upper().split(' ')+['`','~','!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0','-','_','=','+','[','{',']','}','|',';',':','"','\'',',','<','.','>','/','?',' ']

def frequencies(l):
	ret=[]
	for letter in alphabet:
		ret.append(0)
	for elem in l:
		if elem not in alphabet:
			continue
		else:
			ret[alphabet.index(elem)]+=1
	return ret

f=File('critique_of_pure_reason.txt')

data=' '.join(f.readlines())
#print(data)
#print(associate(alphabet,frequencies(list(data))))
histogram(frequencies(list(data)),alphabet)
#my_set=data_set(data=frequencies(list(data)),data_types=alphabet)
#my_set.graph()
