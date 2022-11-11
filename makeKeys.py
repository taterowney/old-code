import random,primeNum,cryptomath

def generateKey(keySize):
	p=0
	q=0
	print('making primes...')
	while p==q:
		p=primeNum.generateLargePrime(keySize)
		q=primeNum.generateLargePrime(keySize)
	n=p*q
	while True:
		e=random.randrange(2**(keySize-1),2**keySize)
		if cryptomath.gcd(e,(p-1)*(q-1)) == 1:
			break
	d=cryptomath.findModInverse(e,(p-1)*(q-1))
	pubKey=(n,e)
	prvKey=(n,d)
	print('Public Key:',pubKey)
	print('Private Key:',prvKey)
	return pubKey,prvKey

def makeKeyFiles(keysize):
	print('making key files...')
	pub,prv=generateKey(keysize)
	with open('private_Key.txt','w') as f:
		f.write('%s,%s,%s' % (keysize,prv[0],prv[1]))
	with open('public_Key.txt','w') as f:
		f.write('%s,%s,%s' % (keysize,pub[0],pub[1]))
	print('done')

if __name__ == '__main__':
	makeKeyFiles(512)
