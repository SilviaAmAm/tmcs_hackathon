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

import numpy as np

def randomise_cm_array(cm_array):
    #find out how many rows there are in the coulomb matrix
    dim = len(cm_array[:, 0])
    #initialise arrays for later
    norm = np.zeros(shape=dim)
    epsilon_array = np.zeros(shape=dim)
    norm_plus_e_array = np.zeros(shape=dim)
    for i in range(dim):
        #calculates norm of each row (i think)
        norm[i] = np.linalg.norm(cm_array[i, :])
    #find standard deviation of norm vector (this divides by N but not sure if it should divide by N-1,
    #although that can be changed later
    sigma = np.std(norm)
    for i in range(dim):
        #draw a random number from normal distribution
        #centred at zero and standard deviation sigma
        epsilon_array[i] = np.random.normal(0, sigma)
        #add arrays together
        norm_plus_e_array[i] = norm[i] + epsilon_array[i]
    #find permutation that sorts the new array into ascending order
    #not entirely sure how/if this works but this is how I did a similar thing in some earlier code
    p = norm_plus_e_array.argsort()[::1]
    #permute columns using this
    new_cm_array_columns = cm_array[p, :]
    #permute rows using this and then return randomised array
    new_cm_array = new_cm_array_columns[:, p]
    return new_cm_array

if __name__ == "__main__":

    m = np.matrix([[1, 2, 3],[2, 1, 4], [3, 4, 1]])
    print(randomise_cm_array(m))