#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes as C
CLIB = C.CDLL('./libc_MP.so')


class Medidor(object):
    """
    Esta clase define un medidor, que mide distintos
    observables de un sistema de particulas
    """

    def __init__(self):
        pass

    def kinetic_energy(self, sys):
        """
        Calula la energia cinetica del sistema de particulas sys
        """
 
        CLIB.ekin(C.byref(sys))

        return sys.ekin


    def potencial_energy(self, sys):
        """
        Calcula la energia potencial del sistema de particulas sys
        """

        CLIB.updcells(C.byref(sys))
        CLIB.force(C.byref(sys))

        return sys.epot


    def temperature(self, sys):
        """ 
        Calcula la temperatura del sistema
        """

        CLIB.ekin(C.byref(sys))
        return sys.temp


    def get_pos(self, sys):

        return sys.pos


    def get_vel(self, sys):

        return sys.vel
