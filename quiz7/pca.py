import pickle
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

with open('c10p1.pickle', 'rb') as f:
    data = pickle.load(f)
    # initial data
    # plt.scatter(data['c10p1'][:, 0], data['c10p1'][:, 1])
    # plt.show()

    # shifted data
    plt.figure()
    col1 = np.array(data['c10p1'][:, 0] - sum(data['c10p1'][:, 0]) / 100)
    # col1+= np.ones(100) # checking what happens to w if we shift data from zero
    col2 = np.array(data['c10p1'][:, 1] - sum(data['c10p1'][:, 1]) / 100)
    shifted_data = np.concatenate((col1[:, np.newaxis], col2[:, np.newaxis]), axis=1)
    plt.scatter(shifted_data[:, 0], shifted_data[:, 1])

    # finding principal eigenvector
    cov_matrix = shifted_data.transpose().dot(shifted_data) / 100
    eigvals, eigvecs = la.eig(cov_matrix)
    print eigvals
    print eigvecs

    eta = 1
    alpha = 1
    dt = 0.01

    n_steps = 100000
    w = np.array([random.random() for i in range(2)])

    for i in range(n_steps):
        u = shifted_data[i % 100]
        v = u.dot(w)
        # Oja's rule
        # w = w + dt * eta * (v * u - alpha * (v * v) * w)
        w = w + dt * eta * (v * u)  # Hebb rule
    print w
    plt.plot(w[0], w[1], 'r*')
    plt.show()
