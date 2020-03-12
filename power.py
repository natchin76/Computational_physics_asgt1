#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:11:16 2020
Power method
@author: chintan
"""
import numpy as np
#Real dominant eigenvalue
A=np.matrix([[2,-1,0],[-1,2,-1],[0,-1,2]])
eigs=np.linalg.eigvals(A)
deig=max(abs(eigs))

#using power method
x0=np.matrix([[1],[0],[0]])
def power(A,x0,deig):
    k=0
    ld=0
    while abs(ld-deig)/abs(deig)>.001:
        y=A**k*x0
        ld=(np.transpose((A*y))*y)/(np.transpose(y)*y)
        k+=1
    return(ld,y)        

print('actual dominant eigval:',deig)
print('dominant eigval using power method:',power(A,x0,deig)[0][0,0])
print('dominant eigvector:',power(A,x0,deig)[1])
x=power(A,x0,deig)[1]/1000   #converting vector elements to order 1
ld=power(A,x0,deig)[0][0,0]
e=A*x-ld*x
print('A*x-lambda*x=',e)