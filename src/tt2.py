#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ctypes as C
CLIB = C.CDLL('./mylib.so')
CLIB.area.argtypes = [C.Structure]
CLIB.area.restype  = C.c_int


class cell_t(C.Structure):
    _fields_ = [ ('natoms', C.c_int),
                 ('owner', C.c_int),  
                 ('idxlist', C.c_void_p )
                ]

    def __init__(self, natoms, owner, idxlist):
        self.natoms = natoms
        self.owner = owner
        self.idxlist = (C.c_int * natoms)(*idxlist)

    def area(self):
        return CLIB.area(self)


