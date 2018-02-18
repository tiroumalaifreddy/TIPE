import numpy as np


def u_suivant(u, c, dx, dt):

    def f(u):
        return 1-u

    u[0] = 0

    for i in range(1, len(u)):
        u[i] = u[i-1] - c*f(u[i-1])*dt
       

print(u_suivant(np.zeros(11), 1, 0.1, 0.1))
