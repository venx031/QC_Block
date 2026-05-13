#Quantum Dev Practice: Task #1 (Decomposition)

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit, transpile

# Task: Realizing the SWAP gate (changes between two qubits)
# Math Proto. Technical Design
v1 = np.array([1, 0]) # ∣0⟩
v2 = np.array([0, 1]) # ∣1⟩

v_00 = np.kron(v1, v1) # ∣00⟩
v_01 = np.kron(v1, v2) # ∣01⟩
v_10 = np.kron(v2, v1) # ∣10⟩
v_11 = np.kron(v1, v1) # ∣11⟩

P0 = np.outer(v_00, v_00) # ∣00⟩∣00⟩
P1 = np.outer(v_01, v_10) # ∣01⟩∣10⟩
P2 = np.outer(v_10, v_01) # ∣10⟩∣01⟩
P3 = np.outer(v_11, v_11) # ∣11⟩∣11⟩
SWAP = P0 + P1 + P2 + P3

#check
I = np.eye(4)
check = np.allclose(SWAP @ SWAP, I)

# Implementation Ticket. Qiskit
qc = QuantumCircuit(2)
qc.x(0)
qc.cx(0, 1)
qc.cx(1, 0)
qc.cx(0, 1)
state = Statevector.from_instruction(qc)
data = state.data

# QA & Validation
result = SWAP @ v_01
check_state = np.allclose(data, result)

# Metrics
qc_opt = transpile(qc, basis_gates=['sx', 'rz', 'cx'])

#print(SWAP) # answer: [[2 0 0 0]
#                      [0 2 0 0]
#                      [0 0 0 0]
#                      [0 0 0 0]]

print(check) # answer: False
print(check_state) # answer: True
#print(qc_opt.count_ops()) # answer: OrderedDict({'cx': 3, 'sx': 2})

#print(qc_opt) # answer: q_0: ┤ √X ├┤ √X ├──■──┤ X ├──■──
#                            └────┘└────┘┌─┴─┐└─┬─┘┌─┴─┐
#                       q_1: ────────────┤ X ├──■──┤ X ├
#                                        └───┘     └───┘