#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes as C

class Medidor(object):
    """
    Esta clase define un medidor, que mide distintos
    observables de un sistema de particulas
    """

    def __init__(self, library = 'serial'):

        if library == 'parallel':
            self.CLIB = C.CDLL('./libc_MP.so')
        elif library == 'serial':
            self.CLIB = C.CDLL('./libc.so')

    def kinetic_energy(self, sys):
        """
        Calula la energia cinetica del sistema de particulas sys
        """
 
        self.CLIB.ekin(C.byref(sys))

        return sys.ekin


    def potencial_energy(self, sys):
        """
        Calcula la energia potencial del sistema de particulas sys
        """

        self.CLIB.updcells(C.byref(sys))
        self.CLIB.force(C.byref(sys))

        return sys.epot


    def temperature(self, sys):
        """ 
        Calcula la temperatura del sistema
        """

        self.CLIB.ekin(C.byref(sys))
        return sys.temp

