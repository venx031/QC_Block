# Implement_Grover’s_Search.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from qiskit.quantum_info import Statevector

# Implement Grover’s Search for 3-bit Unstructured Database
# Initial State
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
v = np.array([1, 0])
v0 = np.kron(v, v)
vt1 = np.kron(v0, v)
H3 = np.kron(H, np.kron(H, H))
psi0 = H3 @ vt1

# Oracle Operator
I = np.eye(8)
w = np.zeros(8)
w[5] = 1
U = I - 2 * np.outer(w, w)
Us = 2 * np.outer(psi0, psi0) - I

# Diffusion Operator
qc = QuantumCircuit(3)
qc.h(0)
qc.x(1)
qc.cz(0, 1)
qc.x(1)
qc.h(0)

# Optimal Iterations
psi = psi0.copy()
for _ in range(2):
    psi = Us @ (U @ psi)

prob = np.abs(psi)**2

# validation
print(prob) # answer: [0.0078125 0.0078125 0.0078125 0.0078125 0.0078125 0.9453125 0.0078125
#                      0.0078125]