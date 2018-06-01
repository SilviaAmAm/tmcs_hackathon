"""
This file should contain a data science pipeline that takes some data in (the Coulomb matrix) and fits an estimator to
the data. The estimator is scored and then used to make predictions on a test set which was not used for training.
"""

## Use Extract_data to obtain the data from the data set


## Use Plain_CM to make the plain Coulomb matrix


## Use Eigenspectrum, Sorted_CM, Randomised_CM to make the variations of the Coulomb matrices


## Use Trim_CM to reduce the number of features of the CM


## Split the data into a train and test set


## Create an object MLPRegressor


## Fit the regressor


## Score the regressor


## Make predictions for the test set