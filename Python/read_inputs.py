import numpy as np
import os
import scipy as sp
import scipy.io as spio
import time

def read_inputs ( case , path ) :
  ifile = open(path+'/examples/')
  natoms = int(ifile.readline().split(' ')[0])
  mass = float(ifile.readline().split(' ')[0]) # in AMU
  epsilon = float(ifile.readline().split(' ')[0]) # in kcal/mol
  sigma = float(ifile.readline().split(' ')[0]) # in angstrom
  rcut = float(ifile.readline().split(' ')[0]) # in angstrom
  box_length = float(ifile.readline().split(' ')[0]) # in angstrom
  restart = ifile.readline().split(' ')[0] # filename for restart
  trajectory = ifile.readline().split(' ')[0] # filename for trajectories
  energies = ifile.readline().split(' ')[0] # filename for energies
  MD_steps = int(ifile.readline().split(' ')[0]) # number of MD steps
  MD_time_step = float(ifile.readline().split(' ')[0]) # MD time step (in fs)
  output_frec = int(ifile.readline().split(' ')[0]) # output print frequency
  ifile.close()
  return ifile, natoms, mass, epsilon, sigma, rcut, box_length, restart,\
    trajectory, energies, MD_steps, MD_time_step, output_frec
