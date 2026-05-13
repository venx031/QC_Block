#Bell_state.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

#math_block
v = np.array([1, 0])
v_initial = np.kron(v, v)
H = np.array([[1, 1], [1, -1] ]) / np.sqrt(2)
I = np.eye(2)
HI = np.kron(I, H)
CNOT = np.array([
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
])

HIv = HI @ v_initial
final = CNOT @ HIv

#qc_block
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
state = Statevector.from_instruction(qc)

#summary
print(HI) # answer: [ 0.          0.          0.70710678  0.         -0.         -0.
#                    -0.70710678 -0.        ]
#                   [ 0.          0.          0.          0.70710678 -0.         -0.
#                    -0.         -0.70710678]]

print(np.allclose(final, state)) # answer: True