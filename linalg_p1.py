#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:19:26 2020

@author: chintan

Prob1:Solution of system of 3 linear equations using linalg.solve
"""
import numpy as np
A=[[1,.67,.33],[.45,1,.55],[.67,.33,1]]
A=np.matrix(A)
B=np.array([2,2,2])
x=np.linalg.solve(A,B)
print(x)