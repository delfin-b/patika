# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:18:14 2023

@author: delfi
"""

def flatten(M):
    arr=[]
    for i in M:
        if type(i) is list:
            for j in i:
                arr.append(j)
        else:
            arr.append(i)
    return arr
  
  
A=[[1,2,3],[5,6],[2,9]]
print (flatten(A))

a= [[1, 2], [3, 4], [5, 6, 7]]

def reverse(arr):
    M=[]
    for i in arr:
        if type(i) is list:
            M.append(i[::-1])
        else:
            M.append(arr[::-1])
    return M[::-1]

print (reverse(a))