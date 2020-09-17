import pickle
import matplotlib.pyplot as plt
import numpy as np


def mean_spike_and_variance_count(neuron_name, data):
    num_of_spikes = data[neuron_name] * 10
    num_of_experiments = len(num_of_spikes)
    mean = np.sum(num_of_spikes, axis=0) / num_of_experiments
    variance = np.sum((num_of_spikes - np.array([mean, ] * num_of_experiments)) ** 2, axis=0) / (num_of_experiments - 1)
    return mean, variance


with open('tuning_2.7.pickle', 'rb') as f:
    data = pickle.load(f)
    # plotting the tuning curve
    plot1 = plt.figure(1)
    plt.plot(data['stim'], np.sum(data['neuron1'], axis=0) / len(data['neuron1']))
    plt.xlabel('stimulus')
    plt.ylabel('mean firing rate of neuron')

    plot2 = plt.figure(2)
    (mean, variance) = mean_spike_and_variance_count('neuron1', data)
    plt.plot(mean, variance, 'bo', label='Neuron1')
    (mean, variance) = mean_spike_and_variance_count('neuron2', data)
    plt.plot(mean, variance, 'ro', label='Neuron2')
    (mean, variance) = mean_spike_and_variance_count('neuron3', data)
    plt.plot(mean, variance, 'go', label='Neuron3')
    (mean, variance) = mean_spike_and_variance_count('neuron4', data)
    plt.plot(mean, variance, 'yo', label='Neuron4')
    plt.plot(np.linspace(0, 350), np.linspace(0, 350), label='Fano factor of poisson process')
    plt.xlabel('mean number of spikes')
    plt.ylabel('variance in number of spikes')
    plt.legend()
    plt.show()
