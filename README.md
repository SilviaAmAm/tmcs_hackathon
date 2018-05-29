# Fitting potential energy surfaces with neural networks

In this exercise, you will use a neural network to fit a potential energy surface for a chemical reaction. The reaction under study is:

CH_4 + CN -> CH_3 + HCN

The idea of fitting potential energy surfaces is used to speed up ab-initio molecular dynamics.

## General information about this project

### The data set

In this repository there is a file called ch4cn.tar.gz which contains the data set. You will need to extract the files with the following command:

```
tar -xf ch4cn.tar.gz
``` 

Then, you will have a new directory called vr_ccsd that contains many xyz files and a properties.txt file. The xyz files contain many different configurations of the CH<sub>4</sub> + CN system, while the properties file contains the energies of all the configurations.

### The descriptor

In order to use the data to train a neural network, the xyz coordinates cannot be used directly, they have to be turned in a suitable form. The descriptor that we will use is called the Coulomb matrix. You can find more information about the Coulomb matrix in [this](https://pubs.acs.org/doi/abs/10.1021/ct400195d) paper.

### The division of tasks

This is a suggestion of how you could split the tasks: 

1. Write the scripts to extract the data from the xyz files and the properties.txt file.
2. Write the script that generates the "plain" Coulomb matrix.
3. Write the script that generates the eigenspectrum of the Coulomb matrix.
4. Write the script that generates the sorted Coulomb matrix.
5. Write the script that generates the randomised Coulomb matrix.
6. Write the script that reduces the dimensions of the Coulomb matrices.
7. Write the machine learning pipeline using sci-kit learn.

For each of these tasks, you will find a file in this directory that tells you what shape the input and the output of the function that you need to write. Tasks2 and 3 are for beginner level; task 1, 4, 5 are lower intermediate level and task 7 is more advanced.

For task 7, a mini pre-made data set with 100 data points is provided to test if the science pipeline works. This can be found in the file test_100.npz. To load the data from this file, use:

```
import numpy as np

npzfile = np.load("test_100.npz")
descriptor = npzfile['arr_0']
energies = npzfile['arr_1']
```

### When everything works

Once the descriptors and the pipeline are all ready you should try to make plotsof how the predictions of the neural network compare to the original data. You can do this by plotting the predictions on the x axis and the true values on the y axis. In an ideal world, you should obtain y = x lines. You can then compare the performance of the different descriptor.

If you have time left, you can also write a function that calculates different properties of the molecule (like C-C distances, C-H distances...) and then plot the predictions and the true values as a function of these properties. This can give you an insight on which structures the neural network struggles to predict.
