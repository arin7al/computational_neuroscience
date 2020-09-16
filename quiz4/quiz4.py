import pickle
import matplotlib.pyplot as plt
import numpy as np

with open('tuning_2.7.pickle', 'rb') as f:
    data = pickle.load(f)
    # plotting the tuning curve
    plt.plot(data['stim'], np.sum(data['neuron1'], axis=0))
    plt.show()

