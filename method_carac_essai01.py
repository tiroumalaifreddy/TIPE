# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:05:24 2018
@author: ftiroumala
"""
import numpy as np
import matplotlib.pyplot as plt

cfl=.1
N=1000
c=10
dx=1/N
dt=cfl*dx/c
u_initial=[]
for i in range(N):
    u_initial.append(((np.sin(i/100))/2)+0.5)
print(u_initial)

u_500=[]

t=50

for i in range(N+c*t):
    if i-c*t<0:
        u_500.append(((np.sin(i/100))/2)+0.5)
    if i-c*t==0:
        u_500.append(0.25)
    else:
        u_500.append(u_initial[i-c*t])
print(u_500)

plt.plot(u_initial)
"""plt.plot(u_500)"""
plt.ylim([0,1])
plt.show()