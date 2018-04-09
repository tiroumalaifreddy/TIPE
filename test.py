# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 16:25:03 2018

@author: ftirouma
"""

import numpy as np
import matplotlib.pyplot as plt
import time
def u_suivant(u, c, dx, dt, nb):
    l=[u]
    t=0
    for i in range(nb):
        if 100 * t - np.floor(100 * t) < 1 / 5:
            u[0] = 1
        else:
            u[1] = 0
        du = (u[1:]-u[:-1])/dx
        u[1:] -= c*du*dt
        t+=dt
        l.append(u.copy())
    return l


u_initial=np.zeros(100)
l=u_suivant(u_initial, 1, 0.1, .01,1000)

for i in range(len(l)):
    if i%10==0:
        plt.plot(l[i])
        plt.show()
