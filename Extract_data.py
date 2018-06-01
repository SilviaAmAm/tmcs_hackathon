"""
This file should contain a function that takes as an input the data set folder and returns a numpy array containing the
xyz coordinates of all the molecules, a numpy array that contains the nuclear charge of each atom in each molecule and a
numpy array that contains the energy of each molecule. These should have the following dimensions/types:

xyz - numpy array of floats of shape (n_samples, n_atoms, 3)
Zs - numpy array of floats of shape (n_atoms,)
energies - numpy array of floats of shape (n_samples,)

where: n_samples is the number of data points in the data set and n_atoms is the number of atoms in a molecule.
"""

import numpy as np
import glob

"""
Read atoms and xyz coordinates from a .xyz file
"""
def read_xyz(geometry_file):
    """
    Routine to read atomic positions from  geometry_file.xyz
    gives a list of atoms and a list of (x,y,z) coordinates
    """
    atoms = []
    coordinates = []

    xyz = open(geometry_file,'r')
    n_atoms = int(xyz.readline())
    title = xyz.readline().strip()
    for line in xyz:
        atom,x,y,z = line.split()
        atoms.append(atom)
        coordinates.append([float(x),float(y),float(z)])
    xyz.close()
    
    #check number of atoms in the list "atoms" matches n_atoms
    if len(atoms) != n_atoms:
        raise ValueError("Error: number of atoms does not match the number n_atoms stated in the file")
    if len(atoms) != len(coordinates):
        raise ValueError("ERROR: file contains %d atoms but found %d coordinates" % (len(atoms), len(coordinates)))
    
    return atoms, coordinates

"""
Reformat data to be put into a Coulomb matrix as described above
"""

def extract_and_format_xyzs(filestore):
    filenames = glob.glob(filestore) # select all files in the given directory
    all_coordinates = []    # store all coordinates as nested lists
    for file in filenames: # loop through all xyz files
        atoms,coordinates = read_xyz(file)
        all_coordinates.append(coordinates) # add each set of coordinates to the total list
    
    atoms_array = np.array(atoms)    # only do this once because in this case all atoms are the same
    coordinates_tensor = np.array(all_coordinates) # turn coordinates in to numpy array
    
    return atoms_array,coordinates_tensor



"""
Extract energies from a text file and put them into an array
"""

"""
In this case the text file is formatted as:
Geometry         Energy
001.xyz          E1
002.xyz          E2
etc.
"""

def read_energy_data(energy_file):
    configs_list = [] # empty lists to store data
    energies_list = []
    
    energy_data = open(energy_file,'r')
    for line in energy_data: # read each line of the file in turn
        config,energy = line.split() # separate the geometry from the energy
        configs_list.append(line) # just number the geometries rather than saving all the filenames
        energies_list.append(energy)
    energy_data.close()
    config_array,energy_array = np.array(configs_list),np.array(energies_list)
    return config_array,energy_array


def extract_and_format_data(xyz_files,energy_file):
    """
    Specify paths to data files in UNIX style
    """

    # extract geometry data from xyz files
    atoms_array,coordinates_tensor = extract_and_format_xyzs(xyz_files)
    # extract energy data
    configs,energies = read_energy_data(energy_file)
    #create array of atomic numbers
    Z_array = np.array([6,1,1,1,1,6,7])
    
    return coordinates_tensor,energies,Z_array






