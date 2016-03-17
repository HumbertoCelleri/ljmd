import numpy as np
import os
import io_ljmd
import mdsys
import medidor
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
    nprint = parameters['nprint']

    # Defino un objeto medidor 
    med = medidor.Medidor()

    # Inicializo los parametros del sistema
    a.input(parameters)

    Graf = graficador.Graficador(a,med)
    for i in range(0,nsteps):
        
        # Rutina de evolucion del sistema 
        a.evolution()

        if i % nprint == 0:

             energia_total = med.kinetic_energy(a) + med.potencial_energy(a)
             temp = med.temperature(a)

             # Imprime los valores 
             print i, temp, med.kinetic_energy(a), med.potencial_energy(a), energia_total
             #Graf.distribucion_posiciones_3D()
             #a.nfi = i

    # Inicializamos la clase
    Graf = graficador.Graficador(a,med)
    # Grafica scatter
    #    Graf.distribucion_posiciones_3D()

    # Grafica   quiver
    #    Graf.distribucion_velocidades_3D()

    # Grafica histograma velocidades
    Graf.histograma_velocidades()
    
    
    ## Imprimimos salidas
    #output = io_ljmd.Print_outputs('argon_108','argon_108','')
    #output.printDAT(100,a)
    #output.printXYZ(100,a)

if __name__ == "__main__":
    main()
