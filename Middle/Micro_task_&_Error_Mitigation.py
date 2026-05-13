# Micro_task_&_Error_Mitigation.py

import numpy as np
from qiskit import QuantumCircuit

# Ticket 1. Micro-task: Zero-Noise Extrapolation (ZNE) Linear Fitter
data = [(1.0, 0.45), (3.0, 0.38)]

def f_emitigated(data):
    (l1, e1) = data[0] # 1.0, .45
    (l2, e2) = data[1] # 3.0, .38

    if l1 == l2:
        raise ValueError

    e_mitigate = (e1 * l2 - e2 * l1) / (l2 - l1)

    return e_mitigate

# test
data = [(1.0, 0.45), (3.0, 0.38)]
print(f_emitigated(data)) # answer: 0.48500000000000004

# Ticket 2: Error Mitigation via Probabilistic Error Cancellation (PEC)
p = 0.1

def f_pec(p, o_ideal, o_corr):
   gamma = 1 / (1 - p)
   p_ideal = 1 / gamma
   p_corr = 1 - p_ideal

   O_mitigated = gamma * (o_ideal - p * o_corr)


   return O_mitigated

p_val = 0.1
measured_ideal = 0.4
measured_corr = 0.05

result = f_pec(p_val, measured_ideal, measured_corr)
print(result) # answer: 0.43888888888888894