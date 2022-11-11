from sympy import *
from random import randint
x=Symbol('x')
def exercise():
    f = randint(1,5)*x**2 + randint(0,5)*x + randint(0,10)
    g = randint(1,5)*x**2 + randint(0,5)*x + randint(0,10)
    h=f*g
#    print('('+str(f)+')` = '+str(diff(f).simplify()))
#    print('('+str(g)+')` = '+str(diff(g).simplify()))
    print('('+str(f)+')` * ('+str(g)+')`\n')
    return str(diff(h).simplify())+'\n'

def main():
    a=''
    for i in range(4):
        a+=exercise()
    with open('.answers.py','w') as f:
        f.write(a)

main()
