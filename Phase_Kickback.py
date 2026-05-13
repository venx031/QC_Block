#Phase_Kickback.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

#Math
qu_0 = np.array([1, 0])
qu_1 = np.array([0, 1])
qu = np.kron(qu_0, qu_1)
H = np.array([[1, 1], [1, -1] ]) / np.sqrt(2)
I = np.eye(2)
H_full = np.kron(H, I)
CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])
V_final = CNOT @ H_full @ qu

#qiskit
qc = QuantumCircuit(2)
qc.x(0)
qc.h(1)
qc.cx(1, 0)
state = Statevector.from_instruction(qc)
check = np.allclose(V_final, state)

#validation
print(V_final) # answer: [0.         1.41421356 0.70710678 0.70710678]
print(check) # answer: True