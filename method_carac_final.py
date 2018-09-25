# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 11:08:21 2018

@author: ftiroumala
"""

import numpy as np
import matplotlib.pyplot as plt

def methode_caracteristiques(u_initial,t,c):
    u_t=[]
    for i in range(len(u_initial)+c*t):
        if i-c*t<0:
            u_t.append(((np.sin(i/100-(c*t-1)/100))/2)+0.5)
        else:
            u_t.append(u_initial[i-c*t])
    return u_t

cfl=.1
N=1000
c=10
dx=1/N
dt=cfl*dx/c

u_initial=[]
for i in range(N):
    u_initial.append(((np.sin(i/100))/2)+0.5)

plt.plot(u_initial)
plt.plot(methode_caracteristiques(u_initial,1,c))
plt.ylim([0,1])
plt.show()