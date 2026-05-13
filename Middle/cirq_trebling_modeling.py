# cirq_trebling_modeling.py

import numpy as np

# content parts
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])
m = 0.3
c = 1.0
h = 1.0
p = 1.0
dt = 0.1

# hamiltonian
H = p * X + m * Z
E = np.sqrt(p**2 + m**2)
theta = E * dt
U = np.eye(2) * np.cos(theta) - 1j * (H / E) * np.sin(theta)

print(U) # answer: [[0.99156189-0.02991557j 0.        -0.09971857j]
#                   [0.        -0.09971857j 0.99156189+0.02991557j]]

# treblling
import cirq
from cirq import NamedQubit, Circuit, MatrixGate, Simulator

q = NamedQubit("q0")
sim  = Simulator()

# loop
results = []
steps = 100
for i in range(steps):
    t = i * dt
    theta = E * t
    U = np.eye(2) * np.cos(theta) - 1j * (H / E) * np.sin(theta)

    circuit = cirq.Circuit()
    circuit.append(cirq.H(q))
    circuit.append(cirq.MatrixGate(U).on(q))
    
    result = sim.simulate(circuit)
    prob = np.abs(result.state_vector()[1])**2
    results.append(prob)

# plot
import matplotlib.pyplot as plt
plt.plot(results)
plt.show()