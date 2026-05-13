# TICKET_QDEV_2048_Deutsch_Algorythm.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from qiskit.quantum_info import Statevector

# Initial State
x = np.array(([1, 0]) + np.array([0, 1])) / np.sqrt(2) # plus
y = np.array(([1, 0]) - np.array([0, 1])) / np.sqrt(2) # minus
psi_in = np.kron(y, x)

# kets
v0 = np.array([1, 0])
v1 = np.array([0, 1])

# function
def f_deutsch(x):
   return x

# matrix
list_vect = [v0, v1]
U00 = np.kron(v0, v0)
U01 = np.kron(v1, v0)
U10 = np.kron(v0, v1)
U11 = np.kron(v1, v1)

U_f1 = np.outer(np.kron(list_vect[0 ^ f_deutsch(0)], v0), U00)
U_f2 = np.outer(np.kron(list_vect[1 ^ f_deutsch(0)], v0), U01)
U_f3 = np.outer(np.kron(list_vect[0 ^ f_deutsch(1)], v1), U10)
U_f4 = np.outer(np.kron(list_vect[1 ^ f_deutsch(1)], v1), U11)

U_full = U_f1 + U_f2 + U_f3 + U_f4

check = np.allclose(U_full, psi_in)

# circuit
qc = QuantumCircuit(2)
qc.x(1)
qc.h(0)
qc.h(1)
qc.cx(0, 1)
qc.h(0)

state = Statevector.from_instruction(qc)

H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
OpH0 = np.kron(np.eye(2), H)
res = U_full @ psi_in
op_final = OpH0 @ res
check = np.allclose(op_final, state)

# validation
print(check) # answer: True