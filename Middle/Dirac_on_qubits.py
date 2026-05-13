# Dirac_on_qubits.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

p = 1.0 # impulse
m = 0.5 # weight

# Pauli matrix
Z = np.array([[1, 0], [0, -1]])
X = np.array([[0, 1], [1, 0]])

# Ham_Dirac
Hd = p * X + m * Z
eigenvalues = np.linalg.eigvalsh(Hd)

# circuit
theta = np.pi

qc = QuantumCircuit(1)
qc.ry(theta, 0)

op = SparsePauliOp.from_list([("X", p), ("Z", m)])
estimator = StatevectorEstimator()
job = estimator.run([(qc, op)])
result = job.result()

# validation
print(eigenvalues) # answer: [-1.11803399  1.11803399]
print(result[0].data.evs) # answer: -0.4999999999999999