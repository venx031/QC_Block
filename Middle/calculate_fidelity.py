# calculate_fidelity.py

import numpy as np

# linal
psi = np.array([1, 0])
phi = np.array([0, 1])

fidelity = np.abs(np.vdot(psi, phi))**2

print(fidelity) # answer: 0

# Qiskit & optimisation
psi_p = (np.array([1, 0, 0, 0]) + np.array([0, 0, 0, 1])) / np.sqrt(2)
theta = np.pi
Ry = np.array([
    [np.cos(theta / 2), -np.sin(theta / 2)],
    [np.sin(theta / 2), np.cos(theta / 2)]
    ])

theta1 = np.pi / 2
theta2 = 0
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
Ry1 = np.array([
    [np.cos(theta1 / 2), -np.sin(theta1 / 2)],
    [np.sin(theta1 / 2), np.cos(theta1 / 2)]
    ])
Ry2 = np.array([
    [np.cos(theta2 / 2), -np.sin(theta2 / 2)],
    [np.sin(theta2 / 2), np.cos(theta2 / 2)]
    ])

op = np.kron(Ry1, Ry2)
state = op @ np.array([1, 0, 0, 0])
psi_f = CNOT @ state
check = np.allclose(psi_f, psi_p)

print(check) # answer: True