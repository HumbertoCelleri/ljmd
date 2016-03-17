#!/usr/bin/python

import numpy as np
import os
import io_ljmd
import mdsys
import medidor
import termostato
import graficador

def main():

    """
    Main de prueba: el sistema toma la data del archivo argon108
    y hace evolucionar. Cada 1000 pasos mide las energias, y la
    temperatura
    """

    # Lee el archivo de entrada y guarda en diccionario
    path = os.getcwd() # get path of ljmd.py
    a = mdsys.mdsys_t()

    # Inicializamos io
#    InputOutput = io_ljmd.Io_ljmd('..') 
    read_inputs = io_ljmd.Read_inputs('argon_108','../../examples/')
    parameters = read_inputs.read()
    
    # El programa corre nsteps pasos e imprimi cada nprint 
    nsteps = parameters['nsteps']
    nprint = parameters['nprint'] * 5

    # Defino un objeto medidor
    med = medidor.Medidor()

    # Inicializo los parametros del sistema
    a.input(parameters)

    # Defino un objeto graficador
    graf = graficador.Graficador()


    # Empiezo el bucle infinito hasta que la respuesta no sea 'y'
    resp = 'y'
    i_aux = 0
    while resp == 'y':

        for i in range(i_aux, i_aux + nsteps):

            # Rutina de evolucion del sistema
            a.evolution_Tconstante(temp = 0.10)
#            a.evolution()

            if i % nprint == 0:

                ekin = med.kinetic_energy(a)
                epot = med.potencial_energy(a)
           
                energia_total = ekin + epot

                temp = med.temperature(a)

                graf.evolucion_graf(i, nsteps, temp, ekin, epot, energia_total)
        # Pregunta si seguir o no
        resp = raw_input('Seguir? y/n: ')
        i_aux += nsteps

    ## Imprimimos salidas
    #output = io_ljmd.Print_outputs('argon_108','argon_108','')
    #output.printDAT(100,a)
    #output.printXYZ(100,a)

if __name__ == "__main__":
    main()
