#Ticket_QDP_2026_04_28.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

# Technical Design
zero = np.array([1, 0])
one = np.array([0, 1])

# kets
v_00 = np.kron(zero, zero)
v_01 = np.kron(zero, one)
v_10 = np.kron(one, zero)
v_11 = np.kron(one, one)

theta = np.pi / 2
e = np.exp(1j * theta)

U_total = (np.outer(v_00, v_00) +
           np.outer(v_01, v_01) +
           np.outer(v_10, v_10) +
           e * np.outer(v_11, v_11))

# validation
print(np.allclose(U_total.conj().T @ U_total, np.eye(4))) # answer: True

# Implementation Ticket
qc = QuantumCircuit(2)
qc.p(theta / 2, 0)
qc.p(theta / 2, 1)
qc.cx(0, 1)
qc.p(-theta / 2, 1)
qc.cx(0, 1)

# validation
op = Operator(qc).data
check_total = np.allclose(U_total, op)
print(check_total) # answer: True