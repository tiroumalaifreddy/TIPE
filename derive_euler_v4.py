
import numpy as np

def couleur_feu(k,dt):
    if  k*dt <3 :
        x=0 #feu rouge
    else:
        x=1 #feu vert   
    return x 


def derivee_de_u_pr_x(u, dx, k, dt):
    du = (u[1:]-u[:-1])/dx
    du=np.insert(du, 0, (u[0]-couleur_feu(k,dt))/dx)    
    return du



def u_instant_suivant(c, u, dx, k, dt):
    du = derivee_de_u_pr_x(u, dx, k, dt)
    u_t_suivant = u-c*(du)*dt
    return u_t_suivant


print(u_instant_suivant(1, np.arange(0, 1, 0.1), 2, 0, 1))
