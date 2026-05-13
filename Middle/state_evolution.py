# state_evolution.py

import numpy as np
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit.quantum_info import Statevector

H = np.array([[1, 0], [0, 1]])
t = np.pi / 4
I = np.eye(2)
sigma = np.array([[0, 1], [1, 0] ])
U = (np.cos(t) * I) - 1j * (np.sin(t) * sigma)
psi = np.array([1, 0])
sigma_x = sigma @ psi
f_state = U @ psi

print(f_state) # answer: [0.70710678+0.j         0.        -0.70710678j]

# Parametric scheme
theta = np.pi
pr = Parameter('theta')
qc = QuantumCircuit(2)

qc.ry(pr, 0)
qc.cx(0, 1)

b_qc = qc.assign_parameters({pr: theta})
state = Statevector.from_instruction(b_qc)
psi_f = np.cos(theta / 2) * np.array([1, 0, 0, 0]) + np.sin(theta / 2) * np.array([0, 0, 0, 1])

print(psi_f) # answer: [6.123234e-17 0.000000e+00 0.000000e+00 1.000000e+00]