import numpy as np
import math
import scipy as sp



#calculate each component of matrix
def plain_cm(xyz, z_s):
        n_samples = xyz.shape[0]
        n_atoms = xyz.shape[1]
        n_features = n_atoms * n_atoms
        coulomb_matrix = np.zeros((n_atoms, n_atoms))
        plain_matrix = np.zeros((n_samples, n_features))
        # loop over all geometries
        for p in range(0, n_samples):
            for i in range(0, n_atoms):
                for j in range(i+1, n_atoms):
                    dist = np.linalg.norm(xyz[p][i] - xyz[p][j])
                    coulomb_matrix[i][j] = (z_s[i] * z_s[j]) / dist
            for k in range(0, n_atoms):
                coulomb_matrix[k][k] = 0.5 * (z_s[k] ** 2.4)
            #print(coulomb_matrix)

            row_of_data = coulomb_matrix.tolist()
            #print(row_of_data)
            linear_data = []
            for sublist in row_of_data:
                for elem in sublist:
                    linear_data.append(elem)
            #print(linear_data)
            linear_array = np.array(linear_data)
            #print(linear_array)
            
            plain_matrix[p] = linear_array
            
            """
            if (p == 0):
                plain_matrix = linear_array
            else:
                np.concatenate((plain_matrix, linear_array), axis = 0)
            """
            #print(plain_matrix)

        return plain_matrix

if __name__ == "__main__":
    # xyz = np.arange(21).reshape(2,7,3)
    test_xyz = np.ones((2, 7, 3))
    z_s = [6, 6, 1, 1, 1, 1, 7]
    #n_samples = 2
    #n_features = 49
    n_atoms = 7
    # print(xyz)

    plain_cm(test_xyz, z_s)
