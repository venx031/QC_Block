#check_the_unitary_and_decompression_of_mixed_state.py

import numpy as np

#gates
a = np.array([[1, 0]])
b = np.array([[1, 0]])
ab = np.kron(a, b)

I = np.eye(4)
U_mx = np.kron(ab, I)
U_total = U_mx @ U_mx.conj().T

print(U_total) # answer: [[1. 0. 0. 0.]
#                        [0. 1. 0. 0.]
#                        [0. 0. 1. 0.]
#                        [0. 0. 0. 1.]]

#tensor dot
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])
XZ = np.kron(X, Z)
check = XZ @ XZ.conj().T

print(check) # answer: [[1 0 0 0]
#                       [0 1 0 0]
#                       [0 0 1 0]
#                       [0 0 0 1]]

#outer dot
P = np.outer(ab, ab.conj())

print(P) # answer: [[1 0 0 0]
#                   [0 0 0 0]
#                   [0 0 0 0]
#                   [0 0 0 0]]