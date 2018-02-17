import numpy as np


def u_suivant(u, c, dx, dt):
    for t in range(1000):
        du = (u[1:]-u[:-1])/dx
        du = np.insert(du, 0, 0)
        u[1:] = u-c*du*dt
        if t < 40:
            u[0] = 0
        else:
            u[1] = 1


print(u_suivant(np.zeros(11), 1, 0.1, 1))


