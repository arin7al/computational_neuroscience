import numpy as np
import scipy.linalg as la

Q = np.array([
    [0.15, 0.1],
    [0.1, 0.12]
])
eigvals, eigvecs = la.eig(Q)

print eigvals
print eigvecs