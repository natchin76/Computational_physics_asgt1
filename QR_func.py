#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:19:28 2020

@author: chintan
"""
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
    eval=np.zeros(len(B))        
    for i in range(len(B)):
        eval[i]=B[i,i]                    
    return(eval,U)