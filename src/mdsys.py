#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes as C
CLIB = C.CDLL('./libc_MP.so')


class cell_t(C.Structure):
    """ Declaro la estructura cell_t definida en el codigo C """

    _fields_ = [ ('natoms', C.c_int),
                 ('owner', C.c_int),
                 ('idxlist', C.POINTER(C.c_int))]

class mdsys_t(C.Structure):
    """ Declaro la estructura asociada al sistema definida en C """

    _fields_ = [ ('dt', C.c_double),
                 ('mass', C.c_double),
                 ('epsilon', C.c_double),
                 ('sigma', C.c_double),
                 ('box', C.c_double),
                 ('rcut', C.c_double),
                 ('ekin', C.c_double),
                 ('epot', C.c_double),
                 ('temp', C.c_double),
                 ('_pad1', C.c_double),
                 ('pos', C.POINTER(C.c_double)),
                 ('vel', C.POINTER(C.c_double)),
                 ('frc', C.POINTER(C.c_double)),
                 ('clist', C.POINTER(cell_t)),
                 ('plist', C.POINTER(C.c_int)),
                 ('_pad2', C.c_int),
                 ('natoms', C.c_int),
                 ('nfi', C.c_int),
                 ('nsteps', C.c_int),
                 ('nthreads', C.c_int),
                 ('ngrid', C.c_int),
                 ('ncell', C.c_int ),
                 ('npair', C.c_int),
                 ('nidx', C.c_int),
                 ('delta', C.c_double),
                 ('D_e',C.c_double),
                 ('a',C.c_double),
                 ('r_e',C.c_double),
                 ('potential',C.c_int) ]


    def __init__(self):

        CLIB.set_nthreads(C.byref(self))
        self.clist = None
        self.plist = None



    def evolution(self, pasos = 1):

        """ Metodo evolucion: el sistema evoluciona mediante el algoritmo de verlet
        la cantidad de pasos especificada. cellfreq se refiere a los pasos en los que
        actualiza la lista de vecinos (definido en el codigo C) """

        cellfreq = 4
        for i in range(0, pasos):

             CLIB.velverlet(C.byref(self))

             if i % cellfreq == 0:
                  CLIB.updcells(C.byref(self))

    def evolution_Tconstante(self, pasos = 1, temp = 40.00, nu = 0.0001):

        self.evolution()

        import termostato
        term = termostato.Andersen_termostat(temp = temp, nu = nu)

        term.set_temp(self)



    def input(self, dict):
        """ Agregar funcion input de datos """

        self.natoms = C.c_int(dict['natoms'])
        self.dt = C.c_double(dict['dt'])
        self.mass = C.c_double(dict['mass'])
        self.box = C.c_double(dict['box'])
        self.rcut = C.c_double(dict['rcut'])
        self.pos = (C.c_double*(3*self.natoms))(*dict['pos'])
        self.vel = (C.c_double*(3*self.natoms))(*dict['vel'])
        self.frc = (C.c_double*(3*self.nthreads*self.natoms))()
        self.nsteps = C.c_int(dict['nsteps'])
        if dict['potential'] == 0: 
            self.potential = C.c_int(0)
            self.epsilon = C.c_double(dict['epsilon'])
            self.sigma = C.c_double(dict['sigma'])
        elif dict['potential'] == 1 :
            self.potential = C.c_int(1)
            self.D_e = C.c_double(dict['D_e'])
            self.a = C.c_double(dict['a'])
            self.r_e = C.c_double(dict['r_e'])
