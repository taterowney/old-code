#!/usr/bin/python3

from reader import *
import sys

name=sys.argv[1]

text=readFile(name,list=True)

with open(sys.argv[2],'w') as f:
	f.write('<!DOCTYPE html>\n<html>\n   <head>\n      <title>'+name+'</title>\n   </head>\n   <body>\n')
	for i in text:
		if len(i) > 20:
			
			f.write('      <h3>'+i+'</h3>\n')
	f.write('   </body>\n</html>')

