#Share_Phase_Effect.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

#Block Math
qu = np.array([1, 0])
initial = np.kron(qu, qu)
H = np.array([[1, 1], [1, -1] ]) / np.sqrt(2)
I = np.eye(2)
HI = np.kron(I, H)
CNOT = np.array([
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
])
Z = np.array([[1, 0], [0, -1] ])

tensor = np.kron(Z, I)
state_1 = HI @ initial
state_2 = CNOT @ state_1
final = tensor @ state_2

print(final) # answer: [ 0.70710678  0.          0.         -0.70710678]

#Block Qiskit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.z(1)
state = Statevector.from_instruction(qc)

check = np.allclose(final, state)

print(check) # answer: True