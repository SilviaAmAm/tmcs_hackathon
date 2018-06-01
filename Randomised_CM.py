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
    dim_2 = len(cm_array[:, 0])
    new_cm_array = np.zeros(shape=(len(cm_array[:,0]), 49))
    for j in range(dim_2):
        coulomb_square = np.reshape(cm_array[j, :], (7, 7))
        #initialise arrays for later
        norm = np.zeros(shape=7)
        epsilon_array = np.zeros(shape=7)
        norm_plus_e_array = np.zeros(shape=7)
        for i in range(7):
        #calculates norm of each row (i think)
            norm[i] = np.linalg.norm(coulomb_square[i, :])
    #find standard deviation of norm vector (this divides by N but not sure if it should divide by N-1,
    #although that can be changed later
        sigma = np.std(norm)
        for i in range(7):
        #draw a random number from normal distribution
        #centred at zero and standard deviation sigma
            epsilon_array[i] = np.random.normal(0, sigma)
        #add arrays together
            norm_plus_e_array[i] = norm[i] + epsilon_array[i]
    #find permutation that sorts the new array into ascending order
    #not entirely sure how/if this works but this is how I did a similar thing in some earlier code
        p = norm_plus_e_array.argsort()[::1]
    #permute columns using this
        new_cm_array_columns = coulomb_square[p, :]
    #permute rows using this and then return randomised array
        new_coulomb_square = new_cm_array_columns[:, p]
        new_coulomb_line = np.reshape(new_coulomb_square, (49, ))
        new_cm_array[j, :] = new_coulomb_line
    return new_cm_array


if __name__ == "__main__":

    m = np.matrix([[1, 2, 3],[2, 1, 4], [3, 4, 1]])
    print(randomise_cm_array(m))