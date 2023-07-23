# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 02:36:07 2023

@author: delfi
"""

def wrapper(f):
    def fun(l):
        # complete the function
        annen=[]
        for x in l:
            if len(x)==10:
                annen.append("+91 " + x[:5] + " " + x[5:])
            elif x.startswith("+91"):
                annen.append("+91 " + x[3:8] + " " + x[8:])
            elif x.startswith("0"):
                annen.append("+91 " + x[1:6] + " " + x[6:])
            elif x.startswith("91"):
                annen.append("+91 " + x[2:7] + " " + x[7:])
        return f(annen)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 