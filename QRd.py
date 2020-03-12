#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:52:41 2020
QR decomposition and eigenvalues
@author: chintan
"""
#1) Using QR decomposition
import numpy as np
def QR(A):
    QR=np.linalg.qr(A)
    Q1=np.matrix(QR[0])
    R=np.matrix(QR[1])
    B=R*Q1
    U=Q1
    for i in range(50):
        QR=np.linalg.qr(B)
        Q=np.matrix(QR[0])
        R=np.matrix(QR[1])
        U=U*Q
        B=R*Q
        QR=np.linalg.qr(B)                
    return(B,U**-1)
A=np.matrix([[5,-2],[-2,8]])    
print('Eigenvalues from QR:',QR(A)[0][1,1],QR(A)[0][0,0])

#2) Using numpy function
eigs=np.linalg.eigh(A)
print('Eigenvalues from linalg:',eigs[0][0],eigs[0][1])
print('eigenvectors:\n',QR(A)[1][:,0],QR(A)[1][:,1])
print('(U*)*A*U=',QR(A)[1]**-1*A*QR(A)[1])