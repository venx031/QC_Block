#checking_up_mixed_state_throu_Pauli_decompress.py

import numpy as np

#entrance matrix
I = np.eye(2)
sz = np.array([[1, 0], [0, -1]])
P = 0.5 * I + 0.3 * sz

r_tr = np.trace(P @ sz)

purity = np.trace(P @ P)
check = np.isclose(purity, 1.0)

print(purity) # answer: 0.6800000000000002
print(r_tr) # answer; 0.6000000000000001
print(check) # answer: False