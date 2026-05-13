# Quantum_Error_Correction.py

import numpy as np

# Holographic screen simulator
# Preparing
X = np.array([[0, 1], [1, 0]])
a = np.array([1, 0])
I = np.eye(2)
aa = np.kron(a, a)
a3 = np.kron(aa, a)
XX = np.kron(X, X)
XXI = np.kron(XX, I)
XXIa = XXI @ a3

print(XXIa) # answer: [0. 0. 0. 0. 0. 0. 1. 0.]

# superposition
H = a3 + XXIa / np.sqrt(2)
print(H)# answer:  [1.         0.         0.         0.         0.         0.
#                   0.70710678 0.        ]

# GHZ state
XXX = np.kron(XX, X)
flip = XXX @ a3
norm = (a3 + flip) / np.sqrt(2)

print(norm) # answer: [0.70710678 0.         0.         0.         0.         0.
#                      0.         0.70710678]

# mistake matrix
E = np.kron(X, I)
EX = np.kron(E, I)

print(EX) # answer: [[0. 0. 0. 0. 1. 0. 0. 0.]
#                    [0. 0. 0. 0. 0. 1. 0. 0.]
#                    [0. 0. 0. 0. 0. 0. 1. 0.]
#                    [0. 0. 0. 0. 0. 0. 0. 1.]
#                    [1. 0. 0. 0. 0. 0. 0. 0.]
#                    [0. 1. 0. 0. 0. 0. 0. 0.]
#                    [0. 0. 1. 0. 0. 0. 0. 0.]
#                    [0. 0. 0. 1. 0. 0. 0. 0.]]

# func QEC
def f_qec(fixed_vector):
    indices = np.where(np.abs(fixed_vector) > 0.1)[0]

    if np.array_equal(np.sort(indices), [0, 7]):
        print("All good!")
        return fixed_vector
    elif np.array_equal(np.sort(indices), [3, 4]):
        print("Correct")
        fixed = EX @ fixed_vector
        return fixed
    else:
        print("Noname Error!")
        return fixed_vector

err_vec = EX @ norm
call_f = f_qec(err_vec)
print(call_f) # amswer: Correct
#                       [0.70710678 0.         0.         0.         0.         0.
#                        0.         0.70710678]