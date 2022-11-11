import math

def A(val):
    total=0
    for v in val:
        total+=v
    return total/len(val)

def G(val):
    total=1
    for v in val:
        total*=v
    return total**(1/len(val))

def factor(val):
    ret = [val]
    for i in range(1, math.ceil(val/2)+1):
        if val/i == val//i:
            ret.append(i)
    return ret
