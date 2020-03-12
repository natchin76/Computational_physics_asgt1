#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:17:47 2020
Conjugate gradient method
@author: chintan
"""
import numpy as np


def CG(A,b,xt):
    x=np.zeros(5)
    x=np.transpose(np.matrix(x))
    r=b-A*x
    p=r[:]
    k=0
    while max(abs(x-xt))>.01:
        a=(np.transpose(r)*r)[0,0]/(np.transpose(p)*A*p)[0,0]
        x=x[:]+(p*a)[:]
        r=r-A*p*a
        bt=(np.transpose(r)*r)[0,0]/(np.transpose(r+A*p*a)*(r+A*p*a))[0,0]
        p=r+p*bt
        k+=1
    return(x,k)
    
A=np.matrix([[.2,.1,1,1,0],[.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b=np.transpose(np.matrix([1,2,3,4,5]))
xt=np.transpose((np.matrix([7.859713071,.422926408,-.073592239,-.540643016,.010626163])))
print('soln:',CG(A,b,xt)[0])
print('no of iterations:',CG(A,b,xt)[1])   
   
