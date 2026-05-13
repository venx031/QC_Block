#Ticket_QSD_305.py
#Validation of Noise-Induced State Purity

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

#circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.s(1)
state = Statevector.from_instruction(qc)

#math_analysis
psi = np.array([1, 0])
psi_res = state.data
P = np.outer(psi, psi_res.conj())
P_tr = np.trace(P)

#svd
U, S, Vh = np.linalg.svd(P)

#summary
print(S[0]) # answer: 1.0
print(np.allclose(sum(S), 1.0)) # answer: True