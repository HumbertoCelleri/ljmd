import random as rand
import numpy as np

class Andersen_termostat(object):

    def __init__(self, temp, nu):
        self.temp = temp
	self.nu = nu
	

    def set_temp(self, mdsys_t):

        natoms = mdsys_t.natoms

        kboltz = 0.0019872067

       # velstd = (mdsys_t.mass / (kboltz * self.temp))**0.5

        velstd = 20

        for i in range(0, natoms):

            if rand.random() < (self.nu * mdsys_t.dt):

                mdsys_t.vel[i] = np.random.normal(0, velstd)
                mdsys_t.vel[i + natoms] = np.random.normal(0, velstd)
                mdsys_t.vel[i + 2*natoms] = np.random.normal(0, velstd)
         

