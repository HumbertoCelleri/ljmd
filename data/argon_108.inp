"""Archivo con parametros de entrada."""

particles = 'argon'    # Name of particles
natoms = 108           # Number of atoms
mass = 39.948          # Mass in AMU
potential = 'lj'       # 'lj' for Lennard-Jones - 'morse' for Morse
if potential == 'lj':
    epsilon = 0.2379   # Epsilon in kcal/mol
    sigma = 3.405      # Sigma in angstrom
elif potential == 'morse':
    D_e = 0.2379       # D_e in kcal/mol
    r_e = 3.405        # r_e in angstrom
    a = 10./r_e        # a in 1/angstrom

rcut = 8.5             # Cut-off radius in angstrom
box = 17.1580          # Box length in angstrom
nsteps = 10000         # Number of MD steps
dt = 5.0               # MD time step (in fs)
nprint = 100           # Output print frequency

restfile = particles+'_'+str(108)+'.rest' # Filename for restart
trajfile = particles+'_'+str(108)+'.xyz'  # Filename for trajectories
ergfile = particles+'_'+str(108)+'.dat'   # Filename for energies
