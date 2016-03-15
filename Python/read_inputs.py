import numpy as np
import os
import scipy as sp
import scipy.io as spio
import time

def read_inputs ( case , path ) :
    ifile = open(path+'/examples/'+case+'.inp','r')
    sys.natoms = int(ifile.readline().split(' ')[0]) # Number of atoms
    sys.mass = float(ifile.readline().split(' ')[0]) # Mass in AMU
    sys.epsilon = float(ifile.readline().split(' ')[0]) # Epsilon in kcal/mol
    sys.sigma = float(ifile.readline().split(' ')[0]) # Sigma in angstrom
    sys.rcut = float(ifile.readline().split(' ')[0]) # Cut-off radius in angstrom
    sys.box = float(ifile.readline().split(' ')[0]) # Box length in angstrom
    restfile = ifile.readline().split(' ')[0] # Filename for restart
    trajfile = ifile.readline().split(' ')[0] # Filename for trajectories
    ergfile = ifile.readline().split(' ')[0] # Filename for energies
    sys.nsteps = int(ifile.readline().split(' ')[0]) # Number of MD steps
    sys.dt = float(ifile.readline().split(' ')[0]) # MD time step (in fs)
    nprint = int(ifile.readline().split(' ')[0]) # Output print frequency
    ifile.close()
    
    data=np.loadtxt(restfile)
    sys.pos=np.reshape(data[:sys.natoms,:],[sys.natoms*3],'F')
    sys.vel=np.reshape(data[sys.natoms:,:],[sys.natoms*3],'F')
    del data
    
    return sys, trajfile, ergfile, nprint
