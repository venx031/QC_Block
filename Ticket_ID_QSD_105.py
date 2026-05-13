#Ticket_ID_QSD_105.py

import numpy as np
import qiskit as qc
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

#create circuit
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
state = Statevector.from_instruction(circuit)

#create Bell vector
psi_id = np.array([1, 0, 0, 1]) / np.sqrt(2)
psi_res = state.data
fidelity = np.abs(np.vdot(psi_id, psi_res))**2

if fidelity > .99:
    print("Bell state verified")
else:
    print("Entanglement error") # answer: "Bell state verified"