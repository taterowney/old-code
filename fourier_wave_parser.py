#fourier transform filter

import math
from numpy import arange

def find_peaks(val, g):
    ret = []
    average = find_midline(val)
    gain = abs(find_average_peak_height(val)-average)*g
    for i in range(1, len(val)-1):
        point = val[i]
        if (point>=val[i+1] and point>=val[i-1]):
            if abs(point-average) >= gain:
                ret.append((i, point))
    return ret

def find_midline(val):
    total = 0
    for v in val:
        total += v
    return total/len(val)

def find_average_peak_height(val):
    ret = 0
    average = find_midline(val)
#    average = 0
    total=0
    for i in range(1, len(val)-1):
        point = val[i]
#        if (point<=val[i+1] and point<=val[i-1]) or (point>=val[i+1] and point>=val[i-1]):
        if (point>=val[i+1] and point>=val[i-1]):
            ret += point
            total+=1
    try:
        return ret/total
    except ZeroDivisionError:
        return None

def get_discrete_values(func, lower, upper, interval):
    ret = []
    for i in list(arange(lower, upper, interval)):
        ret.append(func(i))
    return ret

