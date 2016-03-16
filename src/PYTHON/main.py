import numpy as np
import os
from read_inputs import *
import mdsys
import medidor

def main():

    """ 
    Main de prueba: el sistema toma la data del archivo argon108
    y hace evolucionar. Cada 1000 pasos mide las energias, y la 
    temperatura
    """

    path=os.getcwd() # get path of ljmd.py
    a=mdsys.mdsys_t()
    dict = read_inputs('argon_108','../..')
    a.input(dict)

    # Defino un objeto medidor 
    med = medidor.Medidor()

    for i in range(1,100):
        
        # El sistema evoluciona 1000 pasos
        a.evolution(100)

        energia_total = med.kinetic_energy(a) + med.potencial_energy(a)
        temp = med.temperature(a)

        # Imprime los valores 
        print i*1000, temp, med.kinetic_energy(a), med.potencial_energy(a), energia_total


if __name__ == "__main__":
    main()
