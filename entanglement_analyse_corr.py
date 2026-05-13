#entanglement_analyse_corr.py

import numpy as np

#tensor dot
psi_a = np.array([0, 1])
psi_b = np.array([0, 1])
psi_ab = np.kron(psi_a, psi_b)

#tensor matrix
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
I = np.eye(2)
U_total = np.kron(H, I)
psi_final = U_total @ psi_ab

#prob and amp
P_prob = np.abs(psi_final)**2

print(P_prob) # answer: [0.  0.5 0.  0.5]