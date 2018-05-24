# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:27:40 2018

@author: ftirouma
"""

import numpy as np

import matplotlib.pyplot as plt


def u_suivant(u, c, dx, dt, nb):
    l=[u]
    for t in range(nb):
        du = (u[1:]-u[:-1])/dx
        u[1:] -= c*du*dt
        if t > 500:
            u[0] = 0
        else:
            u[1] = 1
        l.append(u.copy())
    return l


u_initial=np.zeros(100)

l=u_suivant(u_initial, 1, 0.1, .01,1000)


for i in range(len(l)):
    if i%100==0:
        plt.plot(l[i])


plt.show()