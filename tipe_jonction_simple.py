# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:11:57 2018

@author: Freddy
"""
import copy
import numpy as np
import matplotlib.pyplot as plt                
def u_suivant(u, c, dx, dt, T):                 #méthode d'euler
    l=[]                                        #liste contenant les densités de toutes les positions à diff. instants
    for i in range(int(T/dt)):                  #on remplit l en partant des conditions initiales
        u[0] = ((np.sin(i/1000+np.pi))/2)+0.5
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


u_initialbis=copy.deepcopy(u_initial)
l=u_suivant(u_initial, c, dx, dt, 0.01)
m=u_suivant(u_initialbis, 100, dx, cfl*dx/100, 0.01)
n=l+m
for i in range(len(n)):
    if i%100==0:
        plt.plot(n[i])
        plt.ylim([0,1])
        plt.show()


