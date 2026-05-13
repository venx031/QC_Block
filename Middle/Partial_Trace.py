# Partial_Trace.py

import numpy as np
from qiskit.quantum_info import DensityMatrix

a = np.array([1, 0])
b = np.array([0, 1])

v_00 = np.kron(a, a)
v_01 = np.kron(a, b)
v_10 = np.kron(b, a)
v_11 = np.kron(b, b)

P1 = np.outer(v_00, v_00)
P2 = np.outer(v_01, v_01)
P3 = np.outer(v_10, v_10)
P4 = np.outer(v_11, v_11)
P_ab = P1 + P2 + P3 + P4
rho_total = P_ab / np.trace(P_ab)

rho = rho_total.reshape(2, 2, 2, 2)
Pr_trace = np.trace(rho, axis1=1, axis2=3)

print(Pr_trace) # answer: [[0.5 0. ]
#                          [0.  0.5]]

# density matrix
dm = DensityMatrix(Pr_trace)

print(dm) # answer: DensityMatrix([[0.5+0.j, 0. +0.j],
#                                  [0. +0.j, 0.5+0.j]],
#                                  dims=(2,))