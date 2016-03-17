import random as rand
import numpy as np

class Andersen_termostat(object):

    """ Esta clase define un termostato de Andersen:
    temp: temperatura del termostato
    nu: parametro proporcional a la intensidad del termostato
    """

    def __init__(self, temp, nu):
        self.temp = temp
	self.nu = nu
	

    def set_temp(self, mdsys_t):

        """
        Este metodo hace interactuar el termostato
        con el sistema de particulas mdsys_t.
        """

        natoms = mdsys_t.natoms

        kboltz = 0.0019872067
        mv2 = 2390.0573

        velstd = ((kboltz * self.temp) / (mdsys_t.mass * mv2))**0.5

        for i in range(0, natoms):

            if rand.random() < (self.nu * mdsys_t.dt):

                mdsys_t.vel[i] = np.random.normal(0.00, velstd)
                mdsys_t.vel[i + natoms] = np.random.normal(0.00, velstd)
                mdsys_t.vel[i + 2*natoms] = np.random.normal(0.00, velstd)
         

