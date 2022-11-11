from read_write import *
import sys

f=File(sys.argv[1])
text=f.read()

f2=File(sys.argv[2])
f2.insert=False
f2.delete('all')
f2.write('<!DOCTYPE: html>\n<html>\n<head>\n')
f2.write('<title>'+str(input('enter document title: '))+'</title>\n</head>\n')
f2.write('<body>\n<pre>'+text+'</pre>\n</body>\n</html>')
