# Quantum_mechanics_on_the_curve_field.py
# Implementation the number modeling of evolution the wave package to the 2D-surface to specified curvature with NumPy
# Geometry: sphere (positive curvature)

import numpy as np

# Preparing. Initial
R = 1
h = 1
m = 1
dt = 0.001
phi0 = np.pi
sigma = 0.5

theta = np.linspace(0.01, np.pi - 0.01, num=300)
phi = np.linspace(0.0, 2 * np.pi, endpoint=False)
thp, php = np.meshgrid(theta, phi)
d_theta = theta[1] - theta[0]
d_phi = phi[1] - phi[0]

# Geometry
g_det = R**2  * np.sin(thp)

# Assembly The Laplace–Beltrami operator
theta0 = np.pi / 2
psi = np.exp( - ((thp - theta0)**2 + (php - phi0)**2) / (2 * sigma**2))
grad_theta, grad_phi = np.gradient(psi, d_theta, d_phi)
norm = np.sum(np.abs(psi)**2 * g_det * d_theta * d_phi)
total = psi / np.sqrt(norm)

# func laplace beltrami
def f_laplace_beltrami(total, thp, d_theta, d_phi):
    d_psi_theta = np.gradient(total, axis=1) / d_theta
    in_theta = np.sin(thp) * d_psi_theta
    term1 = (np.gradient(in_theta, axis=0) / d_theta) / np.sin(theta)
    d_psi_phi = (np.gradient(np.gradient(psi, axis=0), axis=1) / (d_phi**2))
    term2 = d_psi_phi / (np.sin(thp)**2)
    
    return (1 / R**2) * (term1 + term2)

H = - (1 / (2 * m)) * f_laplace_beltrami(total, thp, d_theta, d_phi)

psi_new = total - 1j * dt * H

# vis and validation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = R * np.sin(thp) * np.cos(php)
y = R * np.sin(thp) * np.sin(php)
z = R * np.cos(thp)

fcolors = np.abs(psi)**2
fmax, fmin = fcolors.max(), fcolors.min()
fcolors = (fcolors - fmin) / (fmax - fmin)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, facecolors=plt.cm.viridis(fcolors), 
                       antialiased=True, shade=False)

ax.set_title("Ptrob density |ψ|² on the sphere")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_box_aspect([1,1,1]) 

plt.show()

# print
print(np.max(np.abs(psi)**2)) # answer: 0.9998910100595323
print(norm) # answer: 0.7378138002647677
