import sys,math,reader

SYMBOLS=' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.\n'

def main():
#	textfile='test.txt'
#	file='cyphertext.txt'
#	mode='decrypt'
	mode,textfile,file=menu()
	if mode == 'encrypt':
		message=reader.readFile(textfile,newline=True)
		cyphertext=encryptAndWriteToFile(file,message)
		print(cyphertext)
	elif mode == 'decrypt':
		plaintext=readFromFileAndDecrypt(file)
		print(plaintext)

def menu():
	try:
		mod=input('to enter encryption mode press "1" and Return\nto enter decryption mode press "2" and Return\n>')
		if mod == '1':
			mod='encrypt'
			txtfile=input('Enter file to read from:')
			_file=input('Enter file to write to:')
			return mod,txtfile,_file
		elif mod == '2':
			mod='decrypt'
			txtfile=None
			_file=input('Enter file to decrypt:')
			return mod,txtfile,_file
	except KeyboardInterrupt:
		pass
	except TypeError:
		pass
	except EOFError:
		pass

def getBlocksFromText(message,size):
	for char in message:
		if char not in SYMBOLS:
			raise TypeError('character %s cannot be encrypted'% char)
	blockInts=[]
	for blockStart in range(0,len(message),size):
		blockInt=0
		for i in range(blockStart,min(blockStart+size,len(message))):
			blockInt+=(SYMBOLS.index(message[i]))*(len(SYMBOLS)**(i % size))
		blockInts.append(blockInt)
	return blockInts

def getTextFromBlocks(blockInts,length,size):
	message=[]
	for blockInt in blockInts:
		blockMessage=[]
		for i in range(size-1,-1,-1):
			if len(message)+i < length:
				charIndex=blockInt // (len(SYMBOLS)**i)
				blockInt=blockInt%(len(SYMBOLS)**i)
				blockMessage.insert(0,SYMBOLS[charIndex])
		message.extend(blockMessage)
	return ''.join(message)

def encryptMessage(message,key,blockSize):
	encryptedBlocks=[]
	n,e=key
	for b in getBlocksFromText(message,blockSize):
		encryptedBlocks.append(pow(b,e,n))
	print(len(encryptedBlocks))
	return encryptedBlocks

def decryptMessage(blocks,length,key,size):
	decryptedBlocks=[]
	n,d=key
	for b in blocks:
		decryptedBlocks.append(pow(b,d,n))
	return getTextFromBlocks(decryptedBlocks,length,size)

def readKeyFile(name):
	with open(name) as f:
		content=f.read()
	keySize,n,E_or_D=content.split(',')
	return int(keySize),int(n),int(E_or_D)

def encryptAndWriteToFile(messageFile,message,blockSize=None):
	size,n,e=readKeyFile('public_Key.txt')
	if blockSize == None:
		blockSize=int(math.log(2**size,len(SYMBOLS)))
#		blockSize=25
	if not int(math.log(2**size,len(SYMBOLS))) >= blockSize:
		raise TypeError
	blocks=encryptMessage(message,(n,e),blockSize)
	for i in range(len(blocks)):
		blocks[i]=str(blocks[i])
	print(blocks)
	content=','.join(blocks)
	with open(messageFile,'w') as f:
		f.write('%s_%s_%s'% (len(message),size,content))
	return content

def readFromFileAndDecrypt(file):
	size,n,d=readKeyFile('private_Key.txt')
	with open(file) as f:
		content=f.read()
	length,blockSize,message=content.split('_')
	length=int(length)
	blockSize=int(blockSize)
#	if not (math.log(2**size,len(SYMBOLS)) >= blockSize):
#			raise TypeError('Block size is to large for the key and symbol set size')
	encryptedBlocks=[]
	for b in message.split(','):
		encryptedBlocks.append(int(b))
	return decryptMessage(encryptedBlocks,length,(n,d),blockSize)

if __name__ == '__main__':
	main()



