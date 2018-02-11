import numpy as np


def derivee_de_u_pr_x(u, dx):
    du = (u[1:]-u[:-1])/dx
    return du


def u_instant_suivant(c, u, dx, dt):
    du = derivee_de_u_pr_x(u, dx)
    du = np.insert(du, 0, 0)
    u_t_suivant = u-c*(du)*dt
    return u_t_suivant


print(u_instant_suivant(2, np.arange(1, 11, 1), 0.1, 1))
