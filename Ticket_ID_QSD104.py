#Ticket_ID_QSD104.py

import numpy as np
import qiskit as qc
from qiskit.circuit.library import RealAmplitudes
from qiskit.quantum_info import Statevector

#Acceptance Criteria
ansatz = RealAmplitudes(1, reps=1)
params = [np.pi/4, np.pi/2]
bound_circuit = ansatz.assign_parameters(params)
state = Statevector.from_instruction(bound_circuit)

psi_id = np.array([1, 0])
psi_res = state.data
inner = np.dot(psi_id.conj(), psi_res)
fidelity = np.abs(inner)**2

if fidelity < .99:
    print("Warning")
else:
    print("Test Passed")