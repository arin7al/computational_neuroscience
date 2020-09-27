import pickle
import numpy as np

with open('pop_coding_2.7.pickle', 'rb') as f:
    data = pickle.load(f)
    r_max1 = max(data['r1'])
    mean1 = sum(data['r1'])/len(data['r1'])
    r_max2 = max(data['r2'])
    mean2 = sum(data['r2'])/len(data['r2'])
    r_max3 = max(data['r3'])
    mean3 = sum(data['r3'])/len(data['r3'])
    r_max4 = max(data['r4'])
    mean4 = sum(data['r4'])/len(data['r4'])
    population_vector = (mean1/r_max1)*data['c1'] + (mean2/r_max2)*data['c2']
    print population_vector
    print np.angle(population_vector[0] + population_vector[1]*1j, deg=True)
