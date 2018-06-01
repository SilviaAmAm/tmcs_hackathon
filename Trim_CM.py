"""
This file should contain a function that takes as an input a symmetric matrix and returns the upper triangular part of
it (including the diagonal elements).

The inputs should have the following dimensions:
CM - numpy array of floats of shape (n_samples, n_features)

where: n_samples is the number of data points in the data set and n_atoms is the number of atoms in a molecule and
 n_features in this case is the square of the number of atoms in the molecules (i.e. 49).

The outputs should have the following dimensions:
trimmed_CM - numpy array of floats of shape (n_samples, n_trimmed_features)
n_atoms= sqrt(n_feat)
where: n_trimmed_features is n_atoms*(n_atoms-1))/2 + n_atoms
"""

import math
import numpy as np

def Trim_CM(CM):
    """
    takes as an input a symmetric matrix and returns  a matrix with reduced dimensions that include the upper triangular part of it.
    :param CM: numpy array of floats of shape (n_samples, n_features)
    :return: numpy array of floats of shape (n_samples, n_trimmed_features)
    """

    n_samples, n_features = np.shape(CM)                    #   GET THE N_samples and n_features from the CM matrix
    num_sq = int(math.sqrt(n_features))
    n_trim= int(num_sq*(num_sq-1)/2 + num_sq)               #   Reduced dimensions

    trimmed_CM = np.zeros((n_samples, n_trim))

    for i in range(n_samples):
        working_mat=np.reshape(CM[i],[num_sq,num_sq])       #   Re-shape each row in CM to a square matrix

        data_list = []
        for n in range(num_sq):
            for w in range(n,num_sq):
                data_list.append(working_mat[n,w])          #   Back to row dimensions for the upper-triangle

        trimmed_CM[i, :] = data_list                        #   Trimmed CM composed

    return trimmed_CM

if __name__ == "__main__":                   
    C=np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
    print(C)
    M=Trim_CM(C)

    print(M)
