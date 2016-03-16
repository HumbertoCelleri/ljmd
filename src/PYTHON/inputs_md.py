import numpy as np
"""Esta funcion lee los datos de los dos archivos de entrada y los
devuelve como diccionario."""

natoms = 108  # Number of atoms
mass = 39.948 # Mass in AMU
epsilon = 0.2379 # Epsilon in kcal/mol
sigma = 3.405 # Sigma in angstrom
rcut = 8.5 # Cut-off radius in angstrom
box = 17.1580 # Box length in angstrom
restfile = 'argon_108.rest' # Filename for restart
trajfile = 'argon_108.xyz' # Filename for trajectories
ergfile = 'argon_108.dat' # Filename for energies
nsteps = 10000  # Number of MD steps
dt = 5.0 # MD time step (in fs)
nprint = 100  # Output print frequency

D_e = epsilon
a = 0.09/sigma
r_e = sigma
