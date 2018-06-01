"""
This file should contain a function that takes as an input the plain coulomb matrix and calculates its eigenspectrum.

The inputs should have the following dimensions:
CM - numpy array of floats of shape (n_samples, n_features)

where: n_samples is the number of data points in the data set and n_atoms is the number of atoms in a molecule and
 n_features in this case is the square of the number of atoms in the molecules (i.e. 49).

The output should have the following dimensions:
es - numpy array of floats of shape (n_samples, n_eigenvalues)

where: n_eigenvalues is the number of eigenvalues of the Coulomb matrix (i.e. - 7)
"""

import numpy as np

def diagonalise(cm_array):
    eigenspectrum_mat = np.zeros(shape=(len(cm_array[:,0]), 7))
    for i in range(len(cm_array[:, 0])):
        to_diag = np.reshape(cm_array[i, :], (7, 7))
        energy = np.linalg.eigvals(to_diag)
        energy = np.sort(energy)[::-1]
        eigenspectrum_mat[i, :] = energy
    return eigenspectrum_mat
