import numpy as np
import scipy.linalg as la

u = np.array([[0.6], [0.5], [0.6], [0.2], [0.1]])
W = np.array([[0.6, 0.1, 0.1, 0.1, 0.1],
              [0.1, 0.6, 0.1, 0.1, 0.1],
              [0.1, 0.1, 0.6, 0.1, 0.1],
              [0.1, 0.1, 0.1, 0.6, 0.1],
              [0.1, 0.1, 0.1, 0.1, 0.6],
              ])
h = W.dot(u)
M = np.array([[-0.125, 0.0, 0.125, 0.125, 0.0],
              [0.0, -0.125, 0.0, 0.125, 0.125],
              [0.125, 0.0, -0.125, 0.0, 0.125],
              [0.125, 0.125, 0.0, -0.125, 0.0],
              [0.0, 0.125, 0.125, 0.0, -0.125]])
eigvals, eigvecs = la.eig(M)
print eigvals
eigvecs = eigvecs.T
print eigvecs
v_steady_state = 0
for i in range(0, 5):
    vector_i = eigvecs[i]/np.sqrt(sum(eigvecs[i]*eigvecs[i]))
    const = (vector_i.dot(h)) / (1 - eigvals[i])
    v_steady_state += const * vector_i

print v_steady_state