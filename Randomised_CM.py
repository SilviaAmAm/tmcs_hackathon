"""
This file should contain a function that takes as an input the plain coulomb matrix and calculates the randomised
version of it.

The inputs should have the following dimensions:
CM - numpy array of floats of shape (n_samples, n_features)

where: n_samples is the number of data points in the data set and n_atoms is the number of atoms in a molecule and
 n_features in this case is the square of the number of atoms in the molecules (i.e. 49).

The output should have the following dimensions:
random_CM - numpy array of floats of shape (n_samples, n_features)
"""