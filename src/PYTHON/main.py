import numpy as np
import os
from read_inputs import *
import mdsys
import medidor

def main():
    path=os.getcwd() # get path of ljmd.py
    a=mdsys.mdsys_t()
    dict = read_inputs('argon_108','../..')
    a.input(dict)


    med = medidor.Medidor()

    print med.kinetic_energy(a)

    a.evolution()

    print med.kinetic_energy(a)


if __name__ == "__main__":
    main()
