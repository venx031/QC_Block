# Implement_Entangled_CZ_Decomposition.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit, transpile

# Technical Design (Math Proto)
z = np.array([1, 0])
o = np.array([0, 1])

# kets
v_00 = np.kron(z, z)
v_01 = np.kron(z, o)
v_10 = np.kron(o, z)
v_11 = np.kron(o, o)

# proj matrix
U1 = np.outer(v_00, v_00)
U2 = np.outer(v_01, v_01)
U3 = np.outer(v_10, v_10)
U4 = np.outer(v_11, v_11)
U_cz = U1 + U2 + U3 - U4

# validation
I = np.eye(4)
I2 = np.eye(2)
U_dag = U_cz.conj().T
check = np.allclose(U_cz @ U_dag, I)

# Implementation Ticket (Qiskit)
qc = QuantumCircuit(2)
qc.x(0)
qc.x(1)
qc.h(1)
qc.cx(0, 1)
qc.h(1)
state = Statevector.from_instruction(qc)
data = state.data

H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
CX = np.array([
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
])

initial = (np.kron(I2, H) @ CX) @ np.kron(I2, H)

# QA & Validation
res = U_cz @ v_11
check_res = np.allclose(data, res)
qc_opt = transpile(qc, basis_gates=['sx', 'rz', 'cx'])

# Metrics
print(check) # answer: True
print(check_res) # answer: True
print(qc_opt.count_ops()) # answer: OrderedDict({'rz': 4, 'sx': 2, 'cx': 1})