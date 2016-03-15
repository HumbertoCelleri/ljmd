#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este archivo contiene las herramientas necesarias para graficar los resultados.

Contiene la clase Graficador con los metodos:
        - histograma_velocidades
        - distribucion_velocidades_3D

"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Graficador(object):
    """
    Clase que grafica resultados de la simulacion DM

    Parameters: sys
    ----------

    """
    def __init__(self, sys):
        super(Graficador, self).__init__()
        self.sys = sys

    def histograma_velocidades(self):
        """function that plots histograma de velocidades"""
        lista_vel = []

        for i in range(0,self.sys.natoms):
            lista_vel.append([self.sys.vel[i],self.sys.vel[i+self.sys.natoms], \
            self.sys.vel[i+2*self.sys.natoms]] )

        """ ploteo histograma"""
        #plt.hist()
        plt.title("Gaussian Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        fig = plt.gcf()
        """
        gaussian_numbers = np.random.randn(1000)
        plt.hist(gaussian_numbers)
        plt.title("Gaussian Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        fig = plt.gcf()
        """

    def distribucion_velocidades_3D(self):
        """ function that plots the 3D graf of posicion particules and velocities"""
        pass

    def distribucion_posiciones_3D(self):
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

        lista_pos = []

        for i in range(0,self.sys.natoms):
            lista_pos.append([self.sys.pos[i],self.sys.pos[i+self.sys.natoms], \
            self.sys.pos[i+2*self.sys.natoms]] )

        """ ploteo scatter"""
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.scatter(lista_pos[0:self.sys.natoms], lista_pos[self.sys.natoms+1:2*self.sys.natoms], lista_pos[2*self.sys.natoms+1:3*self.sys.natoms])
        plt.title('Grafico de posiciones de particulas')
        plt.show()
