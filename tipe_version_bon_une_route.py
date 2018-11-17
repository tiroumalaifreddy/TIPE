# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:11:57 2018

@author: Freddy
"""

import numpy as np
import matplotlib.pyplot as plt                
def u_suivant(u, c, dx, dt, T):                 #méthode d'euler
    l=[]                                        #liste contenant les densités de toutes les positions à diff. instants
    for i in range(int(T/dt)):                  #on remplit l en partant des conditions initiales
        u[0] = ((np.sin(i/1000+(3/2)*np.pi))/2)+0.5
        du = (u[1:]-u[:-1])/dx
        u[1:] -= c*du*dt
        l.append(u.copy())
    return l


cfl=.1                                          #nombre de courant(évite d'obtenir des résultats aberants)
N=1000                                          #longueur de la route
c=10                                            #vitesse des véhicules (supposée constante)
dx=1/N                                          #pas de position
dt=cfl*dx/c                                     #pas de temps
u_initial=np.zeros(N)                           #conditions initiales

l=u_suivant(u_initial, c, dx, dt, 1)

for i in range(len(l)):                         #on trace la densité en fonction des positions. La boucle permet de tracer à diff. instants
    if i%100==0:
        plt.plot(l[i])
        plt.ylim([0,1])
        plt.show()