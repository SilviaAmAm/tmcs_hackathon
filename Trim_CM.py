"""
This file should contain a function that takes as an input a symmetric matrix and returns the upper triangular part of
it (including the diagonal elements).

The inputs should have the following dimensions:
CM - numpy array of floats of shape (n_samples, n_features)

where: n_samples is the number of data points in the data set and n_atoms is the number of atoms in a molecule and
 n_features in this case is the square of the number of atoms in the molecules (i.e. 49).

The outputs should have the following dimensions:
trimmed_CM - numpy array of floats of shape (n_samples, n_trimmed_features)

where: n_trimmed_features is n_features*(n_features-1)/2
"""