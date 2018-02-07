# -*- coding: utf-8 -*-
import numpy as np

def derivee_de_u_pr_x(u,dx):
    du=(u[1:]-u[:-1])/dx
    return du
    
def u_instant_suivant(du):
    c=1
    u_tsuivant=[]
    for i in range(0,8,1):
        u_tsuivant.append(u[i]-(c*du[i]))        
    return u_tsuivant


