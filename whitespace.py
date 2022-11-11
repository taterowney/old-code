import sys
from read_write import *
#f=File(sys.argv[1])
with open(sys.argv[1],'r') as f:
	text=list(f.readlines())
def write(text,line,char):
    with open(sys.argv[1],'r') as _f:
        old=_f.readlines()
    with open(sys.argv[1],'w') as _f:
        cont=list(old[line])
        cont.insert(char,text)
        old[line]=''.join(cont)
#        print(old[line])
        _f.write(''.join(old))
def delete(line,char):
    with open(sys.argv[1],'r') as _f:
        old=_f.readlines()
    with open(sys.argv[1],'w') as _f:
        cont=list(old[line])
        del cont[char]
        old[line]=''.join(cont)
#        print(old[line])
        _f.write(''.join(old))
def check_for_commas():
	for line,content in zip(range(len(text)),text):
		char=0
		index=0
#		print(list(content))
		for letter in list(content):
			if 0 < index:
#				print('triggered')
				if list(content)[index-1]==',' and list(content)[index]!=' ':
					write(' ',line,char)
					char+=1
			char+=1
			index+=1
def replace_tabs():
	for line,content in zip(range(len(text)),text):
		char=0
		for letter in list(content):
			if letter=='\t':
				delete(line,char)
				write('    ',line,char)
			char+=1
#		print(list(content))
replace_tabs()
