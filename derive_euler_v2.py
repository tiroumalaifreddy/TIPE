import numpy as np

def derivee_de_u_pr_x(u,dx):
    du=(u[1:]-u[:-1])/dx
    return du
    
def u_instant_suivant(c,u,dx,dt):
    u_t_suivant=u-(c*derivee_de_u_pr_x(u,dx)*dt)
    return u_t_suivant

print(u_instant_suivant(5,np.arange(1,9,1),0.1))
