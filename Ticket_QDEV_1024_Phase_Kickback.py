# Ticket_QDEV_1024_Phase_Kickback.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from qiskit.quantum_info import Statevector

# Initial State
a = np.array(([1, 0]) + np.array([0, 1])) / np.sqrt(2) # plus
b = np.array(([1, 0]) - np.array([0, 1])) / np.sqrt(2) # minus
psi_in = np.kron(b, a)

v0 = np.array([1, 0])
v1 = np.array([0, 1])

# Operator
theta = np.pi / 2
e = np.exp(1j * theta)

v_00 = np.kron(v0, v0)
v_01 = np.kron(v1, v0)
v_10 = np.kron(v0, v1)
v_11 = np.kron(v1, v1)

U_total = (np.outer(v_00, v_00) +
           np.outer(v_01, v_01) +
           np.outer(v_10, v_10) +
           e * np.outer(v_11, v_11))

# Expected State
psi_out = U_total @ psi_in

# circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.x(1)
qc.h(1)
qc.cp(theta, 0, 1)

state = Statevector.from_instruction(qc)

# check
check = np.allclose(psi_out, state)

print(check) # answer: True