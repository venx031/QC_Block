# Ticket_QDP_2026_01.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

# Implementation a custom unitary operator and decomposition
# Technical Design
H = np.array([[1, 1], [1, -1] ]) / np.sqrt(2)
X = np.array([[0, 1], [1, 0] ])
U_total = np.kron(H, X)

I = np.eye(4)
U_dag = U_total.conj().T
check = np.allclose(U_dag @ U_total, I)

# Implementation
a = np.array([1, 0]) # ∣0⟩
b = np.array([0, 1]) # ∣1⟩

a00 = np.kron(a, a)
a01 = np.kron(a, b)
a10 = np.kron(b, a)
a11 = np.kron(a, a)

P1 = np.outer(a00, a00)
P2 = np.outer(a01, a10)
P3 = np.outer(a10, a01)
P4 = np.outer(a11, a11)
SWAP = P1 + P2 + P3 + P4

I = np.eye(4)
check_swap = np.allclose(SWAP @ SWAP, I)

# Decomposition
qc = QuantumCircuit(2)
qc.x(0)
qc.h(1)

# QA & Validation
op = Operator(qc).data
check_uni = np.allclose(U_total, op)

print(check) # answer: True
print(check_uni) # answer: True