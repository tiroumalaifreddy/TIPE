
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:04:27 2018
@author: ftirouma
"""

import numpy as np
import matplotlib.pyplot as plt
def u_suivant(u, c, dx, dt, T):
    l=[]
    t=0
    for i in range(int(T/dt)):
        u[0] = ((np.sin(i/1000+np.pi))/2)+0.5
        du = (u[1:]-u[:-1])/dx
        u[1:] -= c*du*dt
        t+=dt
        l.append(u.copy())
    return l


cfl=.1
N=1000
c=10
dx=1/N
dt=cfl*dx/c
u_initial=np.zeros(N)
for i in range(N):
    u_initial[i]=(((np.sin(i/100))/2)+0.5)

l=u_suivant(u_initial, c, dx, dt,1)

for i in range(len(l)):
    if i%100==0:
        plt.plot(l[i])
        plt.ylim([0,1])
        plt.show()