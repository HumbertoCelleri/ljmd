#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes as C
CLIB = C.CDLL('./libc.so')


class Medidor(object):

    def __init__(self):
        pass

    def kinetic_energy(self, sys):

        CLIB.ekin(C.byref(sys))

        return sys.ekin


    def potencial_energy(self, sys):

        CLIB.updcells(C.byref(sys))
        CLIB.force(C.byref(sys))

        return sys.epot


    def temperature(self, sys):

        CLIB.ekin(C.byref(sys))
        return sys.temp


    def get_pos(self, sys):

        return sys.pos


    def get_vel(self, sys):

        return sys.vel
