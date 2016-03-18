#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
Este archivo contiene las herramientas necesarias para graficar los resultados.

Contiene la clase Graficador con los metodos:
        - histograma_velocidades
        - distribucion_posiciones_3D
        
"""

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

import numpy as np

class Graficador(object):
    """
    Clase que grafica resultados de la simulacion DM

    Parameters: sys
    ----------

    """
    """
    def __init__(self, sys):
        super(Graficador, self).__init__()
        self.sys = sys
    """
    def __init__(self,sys,caso,path):
        self.sys=sys
        self.caso=caso
        self.path=path

    def histograma_velocidades(self,med):
        """function that plots histograma de velocidades"""
        lista_vel = med.get_vel(self.sys)
        velocidades = np.zeros((self.sys.natoms))
        
        for i in range(0,self.sys.natoms):
            velocidades[i]=np.sqrt(lista_vel[i]**2+lista_vel[i+self.sys.natoms]**2+lista_vel[i+self.sys.natoms*2]**2)
        
        #velocidades = med.get_vel(self.sys)
        """ ploteo histograma"""
        histfig = plt.figure()
        plt.hist(velocidades,bins=20)
        plt.title("Histogram of velocity on x")
        plt.xlabel("Velocity")
        plt.ylabel("Count")
        #fig = plt.gcf()
        plt.show()
        plt.savefig(self.path+self.caso+'_Grafico_histograma_velocidades.png')
        """
        gaussian_numbers = np.random.randn(1000)
        plt.hist(gaussian_numbers)
        plt.title("Gaussian Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        fig = plt.gcf()
        """

    def distribucion_velocidades_3D(self):
        """ function that plots the 3D graf of posicion particules and velocities
        
        Parameters:
        ----------
        self.sys.pos = 3*N particules

        Example:
        -------
        lista_pos = []
        for i in range(0,self.sys.natoms):
            lista_pos.append([self.sys.pos[i],self.sys.pos[i*self.sys.natoms],self.sys.pos[2*i*self.sys.natoms] )
        """
        
        """ ploteo  quiver"""
        fig = plt.figure()
        ax = Axes3D(fig)
        # Ojo! que hay que usar meshgrid!!
        """ax.FUNCION( self.sys.pos[0:self.sys.natoms-1],\
        self.sys.pos[self.sys.natoms:2*self.sys.natoms-1],\
        self.sys.pos[2*self.sys.natoms:3*self.sys.natoms-1,\
        self.sys.vel[0:self.sys.natoms-1],\
        self.sys.vel[self.sys.natoms:2*self.sys.natoms-1],\
        self.sys.vel[2*self.sys.natoms:3*self.sys.natoms-1], length=0.1)
        plt.title('Grafico quiver de particulas')
        """
        plt.show()
        plt.savefig(self.path+self.caso+'_Grafico_3D_quiver.png')


    def distribucion_posiciones_3D(self,med):
        """
        function that plots the 3D graf of posicion particules

        Parameters:
        ----------
        pos = 3*N particules

        Example:
        -------
        lista_pos = []
        for i in range(0,self.sys.natoms):
            lista_pos.append([self.sys.pos[i],self.sys.pos[i*self.sys.natoms],self.sys.pos[2*i*self.sys.natoms] )
        """
        
        """
        lista_pos = []

        for i in range(0,self.sys.natoms):
            #Append positions in (x,y,z) format
            lista_pos.append([\
            self.sys.pos[i],\
            self.sys.pos[i+self.sys.natoms], \
            self.sys.pos[i+2*self.sys.natoms]] )
        
        print lista_pos[1:3]
        """
        """ ploteo scatter"""
        fig = plt.figure()
        ax = Axes3D(fig)
        positions = med.get_pos(self.sys)
        ax.scatter(positions[0:self.sys.natoms-1], positions[self.sys.natoms:2*self.sys.natoms-1],\
         positions[2*self.sys.natoms:3*self.sys.natoms-1])
        plt.title('Grafico de posiciones de particulas')
        plt.show()
        plt.savefig(self.path+self.caso+'_Grafico_3D.png')
        
        
    def evolucion_graf(self, i, nsteps, temp = 0, ekin = 0, epot = 0, etot = 0):
        """ 
        Funcion que grafica la evolucion de la temperatura y las energias del sistema en funcion del tiempo
        """

        plt.ion()

        plt.xlim([0, nsteps + nsteps * (i / nsteps)])

        plt.show()

        legend = []

        if temp != 0:
      	    plt.scatter(i, temp, color = 'g')          
            legend.append('Temp')

        if ekin != 0:       
            plt.scatter(i, ekin, color = 'r')         
            legend.append('Ekin')
            
        if epot != 0:
            plt.scatter(i, epot, color = 'b')          
            legend.append('Epot')

        if etot != 0:
            plt.scatter(i, etot, color = 'k')
            legend.append('Etot')
            
 
        plt.legend(legend)
        plt.xlabel('Time')
        plt.draw()
        plt.savefig(self.path+self.caso+'_Evolucion_temporal.png')
