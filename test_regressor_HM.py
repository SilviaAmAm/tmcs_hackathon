"""
Pipeline for MLP regressor
"""
import numpy as np
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

test_data = np.load('test_100.npz')
descriptor = test_data['arr_0']
energies = test_data['arr_1']


estimator = MLPRegressor(hidden_layer_sizes=(100),solver='lbfgs',max_iter=10000,alpha=0,learning_rate_init=0.0001)

estimator.fit(descriptor, energies)

y_predicted = estimator.predict(descriptor)

plt.scatter(energies,y_predicted)