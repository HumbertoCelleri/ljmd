import numpy as np
import os
from read_inputs import *
import mdsys
import medidor
import termostato

def main():

    """ 
    Main de prueba: el sistema toma la data del archivo argon108
    y hace evolucionar. Cada 1000 pasos mide las energias, y la 
    temperatura
    """
    
    # Lee el archivo de entrada y guarda en diccionario
    path = os.getcwd() # get path of ljmd.py
    a = mdsys.mdsys_t()
    parameters = read_inputs('argon_108','../..')

    # El programa corre nsteps pasos e imprimi cada nprint 
    nsteps = parameters['nsteps']
    nprint = parameters['nprint']

    # Defino un objeto medidor 
    med = medidor.Medidor()

    # Inicializo los parametros del sistema
    a.input(parameters)

    for i in range(0, 10000):
        
        # Rutina de evolucion del sistema 
        a.evolution_Tconstante(temp = 10.00)
        

        if i % nprint == 0:

            energia_total = med.kinetic_energy(a) + med.potencial_energy(a)

            temp = med.temperature(a)

            # Imprime los valores 
            print i, temp, med.kinetic_energy(a), med.potencial_energy(a), energia_total
        

if __name__ == "__main__":
    main()
