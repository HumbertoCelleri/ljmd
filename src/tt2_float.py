#!/usr/bin/env ipython
# -*- coding: utf-8 -*-
import ctypes as C
from ctypes import (
    c_int, c_float, c_double, POINTER, Structure
)
CLIB = C.CDLL('./mylib.so')

#--- area() 
CLIB.area.argtypes = [Structure]
CLIB.area.restype  = c_float


class inp(Structure):
    _fields_ = [
        ('a', c_int),
        ('b', c_float),
        ('bb', POINTER(c_float)),
    ]


class cell_t(Structure):
    _fields_ = [ 
        ('natoms', c_int),
        ('owner', c_int),  
        ('idxlist', POINTER(c_float) ), # funciona ok
        #('run', C.POINTER(C.c_void_p) )
        #('idxlist', C.pointer(C.c_int()) ) #
    ]
    
    """
    def __init__(self, natoms, owner, idxlist):
        print " this init... "
        #self.natoms = natoms
        #self.owner = owner
        #self.idxlist = (C.c_int * natoms)(*idxlist)
    """
    
    def area(self):
        return CLIB.area(self)

#---- test of above
import numpy as np

aa = np.ones(3, dtype=c_float)*10
aaa = aa.ctypes.data_as(POINTER(c_float))
c = cell_t(3, 4, aaa)

#print " ---> parece q c.idxlist se inicilizo en zero :(\n", c.idxlist
print " ---> segun el '.c', el area deberia ser 120: "
print " area: ", c.area() # efectivamente!
#EOF
