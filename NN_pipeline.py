"""
This file should contain a data science pipeline that takes some data in (the Coulomb matrix) and fits an estimator to
the data. The estimator is scored and then used to make predictions on a test set which was not used for training.
"""
import numpy as np
from Eigenspectrum import  diagonalise
from Randomised_CM import randomise_cm_array
from SD_plain_coulomb_matrix import plain_cm
from Trim_CM import Trim_CM
import sklearn.model_selection as modsel
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

import Extract_data

#   Extract data from file
xyz_files= "vr_ccsd/*.xyz"
CH4_CN="vr_ccsd/properties.txt"
configs,energies_data,Z_array = Extract_data.extract_and_format_data(xyz_files,CH4_CN)        # Configs, xyz data, Z_array, atomic numbers,

#   The plain CM matrix

CM=plain_cm(configs,Z_array)

#   Use Eigenspectrum, Sorted_CM, Randomised_CM to make the variations of the Coulomb matrices
#CM_Eigenvalues = diagonalise(CM)
#   CM_sorted=
Random_CM = randomise_cm_array(CM)

## Use Trim_CM to reduce the number of features of the CM

#reduced_CM=Trim_CM(CM)
reduced_randomCM=Trim_CM(Random_CM)

#reduced_shortedCM=Trim_CM(Sorted_CM)

## Split the data into a train and test set
x_train, x_test, y_train, y_test = modsel.train_test_split(reduced_randomCM, energies_data, test_size=0.2, random_state=0)
print(x_train.shape)
print(y_train.shape)

## Create an object MLPRegressor

estimator = MLPRegressor(hidden_layer_sizes=(30,30,30),solver='adam',max_iter=5000,alpha=0,learning_rate_init=0.0001)


## Fit the regressor
estimator.fit(x_train, y_train)

## Score the regressor
score = estimator.score(x_train, y_train)
print(score)

y_predicted = estimator.predict(x_train)

plt.scatter(y_train,y_predicted)
## Make predictions for the test set