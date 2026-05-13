# times_evolution.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

# Implementation of function in Python, that accept to weight of particle and her impulse
# and also step in time and return a circuit the Qiskit,
# than approximate an operator of particles evolution.

# gates
Z = np.array([[1, 0], [0, -1]])
X = np.array([[0, 1], [1, 0]])
m = 2.0 # impulse
p = 0.4 # weight
dt = 0.1

H = p * X + m * Z # Hamiltonian 1D
eigenvalues = np.linalg.eigvalsh(H)

# circuits, func
def f_cirquit(p, m, dt):
    theta_1 = 2 * p * dt # Trotter's formula
    theta_2 = 2 * m * dt # Trotter's formula

    qc = QuantumCircuit(1)
    qc.rx(theta_1, 0) # p \sigma_x
    qc.rz(theta_2, 0) # p \sigma_z

    # observables
    op = SparsePauliOp.from_list([("X", p), ("Z", m)])
    estimator = StatevectorEstimator()
    job = estimator.run([(qc, op)])
    result = job.result()[0]

    qc.measure_all()

    return result.data.evs

# validation
times_e = f_cirquit(p, m, dt)
times_e_2 = f_cirquit(p, m, 0.01)

print(times_e) # answer: 2.00605151166587
print(times_e_2) # answer: 2.000063964845765