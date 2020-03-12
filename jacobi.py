#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:57:39 2020
Prob3: Jacobi method
@author: chintan
"""
import numpy as np

def jacobi(A,b,xt):
    x=np.zeros(len(b))
    m=0
    while max(abs(x-xt))>.01:
        m+=1
        y=np.zeros(len(b))
        for i in range(len(b)):
            y[i]=x[i]
        for j in range(len(b)):
            s=0
            for k in range(len(b)):
                if j!=k:
                    s+=A[j,k]*y[k]
                x[j]=(b[j]-s)/A[j,j]  
    return(x,m)        


A=np.array([[.2,.1,1,1,0],[.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b=np.array([1,2,3,4,5])
xt=np.array([7.859713071,.422926408,-.073592239,-.540643016,.010626163])        
print('solution:',jacobi(A,b,xt)[0])
print('No of iterations:',jacobi(A,b,xt)[1])
