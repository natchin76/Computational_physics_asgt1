#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 00:25:21 2020
singular value decomposition
@author: chintan
"""
from QR_func import QR
import numpy as np
import time
def svd(A):
    m=len(A)
    n=len(A[0])
    B=np.matrix(A[:])
    X=np.transpose(B)*B
    Y=B*np.transpose(B)
    e_val=QR(X)[0]
    V=QR(X)[1]
    pt=e_val.argsort()[::-1]                                         #sorting eigenvalues of X in descending order
    e_val=e_val[pt]                                                
    V=V[:,pt]                                                  #permuting columns of U same as permutation of eigenvalues*
    e_val2=QR(Y)[0]
    U=QR(Y)[1]
    pt=e_val2.argsort()[::-1]                                         #sorting eigenvalues of Y in descending order
    e_val2=e_val2[pt]
    U=U[:,pt]
    S=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if i==j:
                S[i,j]=np.sqrt(e_val[i])
    return(S,U,V)
                
Q=[[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]]
st=time.time()
svd(Q)
ed=time.time()
print('time taken using my function:',ed-st)
st=time.time()
np.linalg.svd(Q)
ed=time.time()
print('time taken using np.linalg.svd:',ed-st)
S=svd(Q)[0]
U=svd(Q)[1]
V=svd(Q)[2]
print('multiplication of U,S and V*\n:',U*S*V**-1)


    
#*I learned this technique of permuting columns from Jay Deshmukh    