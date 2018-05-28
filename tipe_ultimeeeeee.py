# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:04:27 2018

@author: ftirouma
"""

import numpy as np
import matplotlib.pyplot as plt
def u_suivant(u, c, dx, dt, nb):
    l=[]
    t=0
    for i in range(nb):
        if 200 * t - np.floor(200 * t) < 1 / 4:
            u[0] = 1
        else:
            u[0]=0
        du = (u[1:]-u[:-1])/dx
        u[1:] -= c*du*dt
        t+=dt
        l.append(u.copy())
    return l


cfl=.1
N=1000
c=100
dx=1/N
dt=cfl*dx/c
u_initial=np.zeros(N)
l=u_suivant(u_initial, c, dx, dt,50000)

for i in range(len(l)):
    if i%100==0:
        plt.plot(l[i])
        plt.ylim([0,1])
        plt.show()
