# Custom_Entangler_State_Preparation.py

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

# Technical Design (Math Proto)
zero = np.array([1, 0])
one = np.array([0, 1])

# kets
v_00 = np.kron(zero, zero)
v_01 = np.kron(zero, one)
v_10 = np.kron(one, zero)
v_11 = np.kron(one, one)

# assembly
thetha = np.pi / 4
c = np.cos(thetha)
s = -1j * np.sin(thetha)

U_total = (np.outer(v_00, v_00) +
           c * np.outer(v_01, v_01) +
           s * np.outer(v_01, v_10) + 
           s * np.outer(v_10, v_01) + 
           c * np.outer(v_10, v_10) +
           np.outer(v_11, v_11))


#check
check_unitarity = np.allclose(U_total @ U_total.conj().T, np.eye(4))

# Implementation Ticket (Qiskit)
# Challenge Modifier: Decomposition
qc = QuantumCircuit(2)
#qc.h(0)
#qc.h(1)
#qc.cx(1, 0)
#qc.rx(2 * thetha, 0)
#qc.cx(1, 0)
#qc.h(0)
#qc.h(1)

qc.rxx(thetha, 0, 1)
qc.ryy(thetha, 0, 1)

op = Operator(qc).data
check_uni = np.allclose(U_total, op)

#print(check_unitarity) # answer: True
print(check_uni) # answer: True
#print(qc.depth()) # answer: 3
print("U_total[0,0]:", U_total[0,0])
print("op[0,0]:", op[0,0])