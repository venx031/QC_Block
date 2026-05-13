# quantum_event_horizon.py
# Let's imagine that qubit falls in black hole...

import numpy as np

# Initial operator
a = np.array([1, 0])
b = np.array([0, 1])
psi_in = np.kron(a, b)
Z = np.array([[1, 0], [0, -1]])
theta = np.pi / 2

# func of simulate quantum gravity 
def f_simulate_quantum_gravity(theta):
    M = np.array([[np.cos(theta), np.sin(theta)], [- np.sin(theta), np.cos(theta)]])
    I = np.eye(2)
    G = np.kron(M, I)
    result = G @ psi_in
    prob = np.abs(result[3])**2

    return (result, prob)

result, prob = f_simulate_quantum_gravity(theta)
print(result) # answer: [ 0.000000e+00  6.123234e-17  0.000000e+00 -1.000000e+00]
print(prob) # answer: 1.0