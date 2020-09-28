from __future__ import print_function

"""
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron 
R Rao 2007

translated to Python by rkp 2015
"""

import numpy as np
import matplotlib.pyplot as plt

# input current
# I = 1 # nA
I = 100000000000000000 * 1 / 1000  # pA

# capacitance and leak resistance
C = 1  # nF
R = 40  # M ohms

# I & F implementation dV/dt = - V/RC + I/C
# Using h = 1 ms step size, Euler method

V = 0
tstop = 200
abs_ref = 5  # absolute refractory period
ref = 0  # absolute refractory period counter
V_trace = []  # voltage trace for plotting
V_th = 10  # spike threshold

spike_count = 0
for t in range(tstop):

    if not ref:
        V = V - (V / (R * C)) + (I / C)
    else:
        ref -= 1
        V = 0.2 * V_th  # reset voltage

    if V > V_th:
        V = 50  # emit spike
        ref = abs_ref  # set refractory counter
        spike_count += 1

    V_trace += [V]

plt.plot(V_trace)
plt.show()
print(spike_count)
