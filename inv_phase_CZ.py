#inv_phase_CZ.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

#Math
qu = np.array([1, 0])
init = np.kron(qu, qu)
H = np.array([[1, 1], [1, -1] ]) / np.sqrt(2)
I = np.eye(2)
CZ = np.diag([1, 1, 1, -1])
H_full = np.kron(H, I)
H0_full = np.kron(I, H)
final = CZ @ H0_full @ H_full @ init

#qiskit
qc = QuantumCircuit(2)
qc.h(0)
qc.h(1)
qc.cz(0, 1)
state = Statevector.from_instruction(qc)
check = np.allclose(final, state)

#validation
print(final) # answer: [ 0.5  0.5  0.5 -0.5]
print(check) # answer: True