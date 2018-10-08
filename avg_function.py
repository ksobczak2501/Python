# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:33:44 2018

@author: Karolcia
"""
def avg(x):
    a=0
    for i in x:
        a=a+i
        b=a/len(x)
    return(b)

print(avg([2,2,2,2,2]))
print(avg([4,6,55,18,17,12]))
print(avg([86,89,24,45,62,17,61,63,30,13]))