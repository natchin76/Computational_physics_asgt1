#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:14:16 2020
Relaxation method
@author: chintan
"""
import numpy as np				 

def relaxation(A,b,xt):
    x0=np.zeros(len(b))
    X=[x0]
    k=0
    w=1.25
    while max(abs(X[k]-xt))>.01:
        k+=1
        x=np.zeros(len(b))
        for i in range(len(b)):
            x[i]=X[k-1][i]
        for j in range(5):
            s=0
            for l in range(5):
                if j!=l:
                    s+=A[j][l]*x[l]
                x[j]=w*(b[j]-s)/A[j][j]+(1-w)*X[k-1][j]
        X.append(x)
        if k>100:
            print('did not converge')
            break  
    return(x,k)
    
A = [[.2,.1,1,1,0],[.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]]
b = [1,2,3,4,5]
xt=np.array([7.859713071,.422926408,-.073592239,-.540643016,.010626163])
print('solution:',relaxation(A,b,xt)[0])    
print('no of iterations:',relaxation(A,b,xt)[1])

