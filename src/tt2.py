#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ctypes as C
CLIB = C.CDLL('./mylib.so')

#--- area() 
CLIB.area.argtypes = [C.Structure]
CLIB.area.restype  = C.c_int


class cell_t(C.Structure):
    _fields_ = [ ('natoms', C.c_int),
                 ('owner', C.c_int),  
                 ('idxlist', C.POINTER(C.c_int) ) # funciona ok
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

aa = np.ones(3)
aaa = aa.ctypes.data_as(C.POINTER(C.c_int))
c = cell_t(3, 4, aaa)

print c.idxlist

#EOF
