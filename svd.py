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
    return(S,U,V**-1)
                
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
print('Using numpy function:\n')
print('S=',np.linalg.svd(Q)[1])
print('U=',np.linalg.svd(Q)[0])
print('V=',np.linalg.svd(Q)[2])
print('Using my function:\n')
print('S=',S)
print('U=',U)
print('V=',V)
print('\nmultiplication of U,S and V*(which matches given matrix Q\n:',U*S*V)
print('\nConclusion: Last 2 columns of U matrix are different for both the methods. This is bcoz\nlast 2 eigenvalues are degenrate and hence any linear combination of last 2 rows is also an eigenvector. Hence last 2 columns of U are not unique. V and S are same for both methods. Also note that 3rd row of V for both methods are negative of each other. Similarly 3rd column of U. Thus the net result will be same.') 


    
#*I learned this technique of permuting columns from Jay Deshmukh    
