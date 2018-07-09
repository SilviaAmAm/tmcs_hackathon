"""
This file should contain a function that takes as an input a symmetric matrix and returns the upper triangular part of
it (including the diagonal elements) as a vector.

The inputs should have the following dimensions:
CM - numpy array of floats of shape (n_samples, n_atoms, n_atoms)

where: n_samples is the number of data points in the data set and n_atoms is the number of atoms in a molecule.

The outputs should have the following dimensions:
trimmed_CM - numpy array of floats of shape (n_samples, n_trimmed_features)

where: n_trimmed_features is n_atoms*(n_atoms+1)/2
"""
