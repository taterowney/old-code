import matplotlib.pyplot as plt

def histogram(data,labels,show=True):
	bars=len(data)
	pos=range(1,bars+1)
	plt.barh(pos,data,align='center')
	plt.yticks(pos,labels)
	plt.grid()
	if show==True:
		plt.show()
