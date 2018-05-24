# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:31:49 2018

@author: ftirouma
"""

import numpy as np
import matplotlib.pyplot as plt
def u_suivant(u, c, dx, dt, nb):
    l=[]
    t=0
    for i in range(nb):
        du = (np.roll(u,-1)-u)/dx
        u -= c*du*dt
        t+=dt
        l.append(u.copy())
    return l

li=[]
x=np.linspace(0,1,100)
u_initial=np.sin(np.pi*x)**2
c=.1
l=u_suivant(u_initial.copy(), c, 0.1, .01,1000)
for i in range(len(l)):
    if i%10==0:
        plt.plot(l[i])
        plt.plot(np.sin(np.pi*(x-c*i/1000))**2)
        plt.show()
