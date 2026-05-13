# VQE_Light.py

import numpy as np

# Hamiltonian
Z = np.array([[1, 0], [0, -1]])
H = np.kron(Z, Z)

# qubits
psi = np.array([1, 0])
psi_total = np.kron(psi, psi)
x = np.pi

def f_theta(x):
    Ry = np.array([
    [np.cos(x / 2), -np.sin(x / 2)],
    [np.sin(x / 2), np.cos(x / 2)]
    ])

    Ryy = np.kron(Ry, Ry)
    pt = Ryy @ psi_total

    return pt.conj().T @ H @ pt

print(f_theta(x)) # answer: 1.0