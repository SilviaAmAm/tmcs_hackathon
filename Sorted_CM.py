"""
This file should contain a function that takes as an input the plain coulomb matrix and calculates the sorted version of
it.

The inputs should have the following dimensions:
CM - numpy array of floats of shape (n_samples, n_features)

where: n_samples is the number of data points in the data set and n_atoms is the number of atoms in a molecule and
 n_features in this case is the square of the number of atoms in the molecules (i.e. 49).

The output should have the following dimensions:
sorted_CM - numpy array of floats of shape (n_samples, n_features)
"""

import numpy as np
from math import sqrt
from numpy import linalg as LA

#
# def generate_sorted_cm(coul_mat):

    # n_samples, n_features = coul_mat.shape
    # n_atoms = int(np.sqrt(n_features))
    #
    # SortedCoulombMatrix = np.empty([n_atoms, n_atoms])

    # natoms2 = n_atoms ** 2
    #
    # for i in range(natoms2):
    #     for j in range(n_atoms):
    #         if coul_mat[0][i] > n_atoms or coul_mat[0][i] <= n_atoms * j:
    #             SortedCoulombMatrix[i,j] = coul_mat[0][i]
    # return SortedCoulombMatrix


# if __name__ == "__main__":
#
#     ar = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
#
#     generate_sorted_cm(ar)

# ar[::-1].sort()
# print(ar)
#
# ar2 = np.reshape(ar, (3,3))
# print(ar2)
#
# norm1=LA.norm(ar2, axis=1)
# norm = np.sort(norm1)[::-1]
# print(norm)
def SortCM(plain):
    n_sample = plain.shape[0]
    n_atoms = int(np.sqrt(plain.shape[1]))
    n_features = plain.shape[1]

    sorted_cm = np.zeros((n_sample, n_features))

    for j in range(n_sample):
        square_plain = np.reshape(plain[j], (n_atoms, n_atoms))
        norm = np.zeros(shape=len(square_plain[:,0]))
        for i in range(len(square_plain[:, 0])):
            norm[i] = np.linalg.norm(square_plain[i, :])
        p = norm.argsort()[::-1]
        new_array = square_plain[p,:]
        sorted = new_array[:,p]

        reshape_sorted = np.reshape(sorted, (n_features,))                   # reshape it from 7x7 to 49
        sorted_cm[j] = reshape_sorted

    return sorted_cm


if __name__ == "__main__":
    array = np.matrix([[1, 2, 3, 0],[2, 5, 4, 0],[3, 4, 9, 0]])
    print(array)

    print(SortCM(array))