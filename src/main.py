#!/usr/bin/python

import numpy as np
import os
from shutil import copyfile
import mdsys as mdsys
import medidor as medidor
import termostato as termostato
import graficador as graficador


# Con 'parallel' usa la libreria paralela y con 'serial', la serial
library = 'parallel'

# Caso a analizar: 'argon_108', 'argon_2916', 'argon_78732'
#   'argon_108_morse', 'argon_2916_morse', 'argon_78732_morse'
caso = 'argon_108'

termostato=False

def main():

    """
    Main de prueba: el sistema toma la data del archivo argon108
    y hace evolucionar. Cada 1000 pasos mide las energias, y la
    temperatura
    """

    # Inicializamos el sistema y elegimos corrida en serie o paralelo
    path_data='./data/'
    copyfile(path_data+caso+'.inp','src/mdinput.py')
    import io_ljmd as io_ljmd
    mdsystem = mdsys.mdsys_t(library)

    # Inicializamos io
    read_inputs = io_ljmd.Read_inputs(caso,path_data)
    parameters = read_inputs.read()
    
    # El programa corre nsteps pasos e imprimi cada nprint 
    nsteps = parameters['nsteps']
    nprint = parameters['nprint'] * 5

    # Defino un objeto medidor
    med = medidor.Medidor(library)

    # Defino un objeto graficador
    graf = graficador.Graficador(mdsystem,caso,path_data)
    output = io_ljmd.Print_outputs(caso,caso,path_data)


    # Inicializo los parametros del sistema
    mdsystem.input(parameters)

    # Empiezo el bucle infinito hasta que la respuesta no sea 'y'
    resp = 'y'
    i_aux = 0
    while resp == 'y':
        for i in range(i_aux, i_aux + nsteps):
            # Rutina de evolucion del sistema
            if termostato :
                mdsystem.evolution_Tconstante(temp = 0.10)
            else :
                mdsystem.evolution()

            if i % nprint == 0:
                ekin = med.kinetic_energy(mdsystem)
                epot = med.potencial_energy(mdsystem)
                energia_total = ekin + epot
                temp = med.temperature(mdsystem)
                graf.evolucion_graf(i, nsteps, temp, ekin, epot, energia_total)
                ## Imprimimos salidas
                output.printDAT(i,mdsystem)
                output.printXYZ(i,mdsystem)
        # Pregunta si seguir o no
        resp = raw_input('Seguir? y/n: ')
        i_aux += nsteps
    graf.histograma_velocidades(med)
    graf.distribucion_posiciones_3D(med)

if __name__ == "__main__":
    main()
