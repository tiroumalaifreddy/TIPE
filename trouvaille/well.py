from __future__ import division

import numpy as np

import matplotlib . pyplot as plt

# Righthand side of differential equation
def f (x):
    return -x + 1
# Define initial condition
x0 = 0
# Time step
dt = 0.01
# Solve the differential equation from time 0 to time T
T = 5
# Define discretized time ; assumes dt divides nicely into T
t = np. linspace (0 , T, int(T/dt )+1)
# An array to store the solution
x = np. zeros (len(t))
# Integrate the differential equation using Euler ’s method
x[0] = x0

for i in range (1 , len(t)):
    x[i] = x[i -1] + f(x[i -1])* dt

print(x)
