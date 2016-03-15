#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ctypes as C
CLIB = C.CDLL('./tt.so')
CLIB...


class cell_t(C.Structure):
    _fields_ = [ ('natoms', C.c_int),
                 ('owner', C.c_int),
                 ('idxlist', C.pointer(C.c_int))]
    def __init__(self, natoms, owner, idxlist):
        self.natoms = natoms
        self.owner = owner


class mdsys_t(C.Structure):
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
                 ('pos', C.pointer(C.c_double)),
                 ('vel', C.pointer(C.c_double)),
                 ('frc', C.pointer(C.c_double)),
                 ('clist', ''' ver como se pasa '''),
                 ('plist', C.pointer(C.c_int))
                 ('_pad2', C.c_int),
                 ('natoms', C.c_int),
                 ('nfi', C.c_int),
                 ('nsteps', C.c_int),
                 ('nthreads', C.c_int),
                 ('ngrid', C.c_int),
                 ('ncell', C.c_int ),
                 ('npair', C.c_int),
                 ('nidx', C.c_int),
                 ('delta', C.c_double) ]
                 

    def __init__(self, dt , pos = []....):
        self.dt = dt
        self.pos = (C.c_double * N)(pos)
        

    def metodo(self):
        CDLL.funcion(byref(self.pos))
