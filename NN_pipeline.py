"""
This file should contain a data science pipeline that takes some data in (the Coulomb matrix) and fits an estimator to
the data. The estimator is scored and then used to make predictions on a test set which was not used for training.
"""
import numpy as np
import Extract_data
from Eigenspectrum import  diagonalise
from Randomised_CM import randomise_cm_array
from SD_plain_coulomb_matrix import plain_cm
from Trim_CM import Trim_CM


#   Extract data from file
xyz_files= "vr_ccsd/*.xyz"
CH4_CN="vr_ccsd/properties.txt"
configs,energies_data,Z_array = Extract_data.extract_and_format_data(xyz_files,CH4_CN)        # Configs, xyz data, Z_array, atomic numbers,

#   The plain CM matrix
CM=plain_cm(configs,Z_array)

#   Use Eigenspectrum, Sorted_CM, Randomised_CM to make the variations of the Coulomb matrices
CM_Eigenvalues = diagonalise(CM)
#   CM_sorted=
Random_CM = randomise_cm_array(CM)

## Use Trim_CM to reduce the number of features of the CM

reduced_CM=Trim_CM(CM)
reduced_randomCM=Trim_CM(Random_CM)
#reduced_shortedCM=Trim_CM(Sorted_CM)

## Split the data into a train and test set


## Create an object MLPRegressor


## Fit the regressor


## Score the regressor


## Make predictions for the test set