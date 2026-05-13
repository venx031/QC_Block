#Linear_Algebra_Core.py

import numpy as np

#let initial vector
psi = np.array([1, 0])
H = np.array([[1, 1], [1, -1] ]) / np.sqrt(2)
S = np.array([[1, 0], [0, 1j] ])

#operator
U_total = np.kron(H, S)
psi_initial = np.kron(psi, psi)
psi_final = U_total @ psi_initial

#svd
U, S, Vh = np.linalg.svd(U_total)

print(psi_final) # answer: [0.70710678+0.j 0.        +0.j 0.70710678+0.j 0.        +0.j]
print(Vh) # answer: [[-1.+0.j -0.+0.j -0.+0.j  0.+0.j]
#                   [-0.+0.j -1.+0.j -0.+0.j  0.+0.j]
#                   [-0.+0.j -0.+0.j  0.+0.j -1.+0.j]
#                   [-0.+0.j -0.+0.j -1.+0.j  0.+0.j]]
