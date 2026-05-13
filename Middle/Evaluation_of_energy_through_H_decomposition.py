# Evaluation_of_energy_through_H_decomposition.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import SparsePauliOp, Statevector

# Hamil
Z = np.array([[1, 0], [0, -1]])
I = np.eye(2)
X = np.array([[0, 1], [1, 0]])
H = 0.5 * np.kron(Z, I) + 0.8 * np.kron(X, X)
theta = np.pi

# func
def f_counts(counts):
    total_shots = sum(counts.values())
    exp = 0

    for outcome, count in counts.items():
        count_ones = outcome.count('1')
        sign = 1 if count_ones % 2 == 0 else -1
        exp += sign * (count / total_shots)

    return exp

# circuit 1
step_prep = QuantumCircuit(2)
step_prep.h(0)
step_prep.ry(theta, 1)
step_prep.cx(0, 1)

# measure zi
qc_zi = step_prep.copy()
qc_zi.measure_all()

# measure xx
qc_xx = step_prep.copy()
qc_xx.h([0, 1])
qc_xx.measure_all()

# final
sampler = StatevectorSampler()
job = sampler.run([qc_zi, qc_xx])
result = job.result()
counts_zi = result[0].data.meas.get_counts()
counts_xx = result[1].data.meas.get_counts()

energy = 0.5 * f_counts(counts_zi) + 0.8 * f_counts(counts_xx)

print(energy) # answer: 0.30000000000000004