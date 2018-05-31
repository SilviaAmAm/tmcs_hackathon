"""
This file should contain a function that takes as an input the xyz coordinates and the nuclear charges of molecules
and returns the plain Coulomb matrix for all the molecules.

The inputs should have these dimensions:
xyz - numpy array of floats of shape (n_samples, n_atoms, 3)
Zs - numpy array of floats of shape (n_atoms,)

where: n_samples is the number of data points in the data set and n_atoms is the number of atoms in a molecule.

The outpus should have the following dimensions:
CM - numpy array of floats of shape (n_samples, n_features)

where: n_features in this case is the square of the number of atoms in the molecules (i.e. 49)

The reason why the output should have this shape is explained below. Each molecule will have a corresponding Coulomb matrix. The Coulomb matrices are square, symmetric matrices. So, you will have n_samples Coulomb matrices. The neural networks take vectors as inputs, not matrices. So the Coulomb matrices need to be flattened to vectors to be suitable.
"""
