#Ticket_ID_QSD_201.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

#TASK_1
#Pauli gates
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])
U = np.kron(X, Z)
check = U @ U.conj().T

print(check) # answer: [[1 0 0 0]
#                       [0 1 0 0]
#                       [0 0 1 0]
#                       [0 0 0 1]]


#TASK_2
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
state = Statevector.from_instruction(circuit)

#TASK_3
psi_res = state.data
P = np.outer(state, psi_res.conj())
P_tr = np.trace(P)

print(P) # answer: [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
#                  [0. +0.j 0. +0.j 0. +0.j 0. +0.j]
#                  [0.5+0.j 0. +0.j 0. +0.j 0.5+0.j]]

print(P_tr) # answer: (0.9999999999999998+0j)