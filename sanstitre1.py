# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:06:55 2018

@author: ftirouma
"""

import numpy as np
import matplotlib.pyplot as plt
def u_suivant(u, c, dx, dt, nb):
    l=[u]
    t=0
    for i in range(nb):
        u[0]=1
        du = (u[1:]-u[:-1])/dx
        u[1:] -= c*du*dt
        t+=dt
        l.append(u.copy())
    return l


u_initial=np.arange(11)
l=u_suivant(u_initial, 1, 0.1, .01,1000)

for i in range(len(l)):
    if i%10==0:
        plt.plot(l[i])
        plt.show()