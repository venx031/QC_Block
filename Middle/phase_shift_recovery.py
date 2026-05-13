# phase_shift_recovery.py

import numpy as np
import cirq

# initial state
state_0 = np.array([1, 0]) # state basis
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2) # Hadamar
X = np.array([[0, 1], [1, 0]]) # Pauli X
Z = np.array([[1, 0], [0, -1]]) # Pauli Z
theta = np.pi / 3
st_H = H @ state_0

# cirq
qubit = cirq.LineQubit(0)
circuit = cirq.Circuit(
    cirq.H(qubit),
    cirq.rz(theta)(qubit)
    )

simulator = cirq.Simulator()
result = simulator.simulate(circuit)
f_state = result.final_state_vector

check = np.conj(f_state).T @ X @ f_state

print(check) # answer: (0.5000000420713633+0j)