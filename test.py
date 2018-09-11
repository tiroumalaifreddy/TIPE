# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:05:24 2018

@author: ftiroumala
"""
import numpy as np
import matplotlib.pyplot as plt

cfl=.1
N=1000
c=100
dx=1/N
dt=cfl*dx/c
u_initial=[]
for i in range(N):
    u_initial.append(abs(np.cos(i)))
print(u_initial)

u_500=[]
for i in range(2*N):
    if i-c*500<0:
        u_500.append(0)
    else:
        u_500.append(u_initial[i-c*500])
        
plt.plot(u_500)
plt.ylim([0,1])
plt.show()
    