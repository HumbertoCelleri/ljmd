#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
Este archivo contiene las herramientas necesarias para graficar los resultados.

Contiene la clase Graficador con los metodos:
        - histograma_velocidades
        - distribucion_velocidades_3D

TO DO:
 - Repair inp path
 -

"""

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


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
    def __init__(self):
        pass

    def histograma_velocidades(self,med,sys):
        """function that plots histograma de velocidades"""
        plt.close("all")

        lista_vel = []

        for i in range(0,sys.natoms):
            lista_vel.append([sys.vel[i],sys.vel[i+sys.natoms], \
            sys.vel[i+2*sys.natoms]] )

        velocidades = sys.vel
        """ ploteo histograma"""
        histfig = plt.figure()
        ax_hist = histfig.add_subplot(111)

        ax_hist.hist(velocidades[0:sys.natoms-1],bins=20)
        #ax_hist.hist(velocidades[sys.natoms:2*sys.natoms-1],bins=20)
        #ax_hist.hist(velocidades[2*sys.natoms:3*sys.natoms-1],bins=20)
        plt.title("Histogram of velocity on x")
        plt.xlabel("Position")
        plt.ylabel("Velocity")
        plt.grid(True)
        plt.show()
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
        plt.save('Grafico_3D_quiver')


    def distribucion_posiciones_3D(self,med,sys,i):
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
        plt.close("all")
        plt.ion()
        plt.xlim(-sys.box,sys.box)

        figDistrPos = plt.figure()
        ax = Axes3D(figDistrPos)
        #plt.show()
        #plt.Axes3D()
        """ax.scatter(lista_pos[0:self.sys.natoms], lista_pos[self.sys.natoms+1:2*self.sys.natoms], lista_pos[2*self.sys.natoms+1:3*self.sys.natoms])"""
        # ACA TENGO QUE LLAMAR A MEDIDOR(sys)
        positions = sys.pos
        ax.scatter(positions[0:sys.natoms-1], positions[sys.natoms:2*sys.natoms-1],\
         positions[2*sys.natoms:3*sys.natoms-1])
        #ax.scatter(self.sys.pos[0:self.sys.natoms-1], self.sys.pos[self.sys.natoms:2*self.sys.natoms-1], self.sys.pos[2*self.sys.natoms:3*self.sys.natoms-1])
        plt.title('Grafico de posiciones de particulas')
        plt.xlim([-round(sys.box)-3, round(sys.box)+3])
        plt.ylim([-round(sys.box)-3, round(sys.box)+3])
        ax.set_zlim3d([-round(sys.box)-3, round(sys.box)+3])
        #plt.savefig('Grafico_3D.png')
        #plt.draw()
        plt.savefig('Grafico_Profiling'+str(i)+'.png')
        #plt.clf()
        plt.close("all")

    def evolucion_graf(self, i, nsteps, temp = 0, ekin = 0, epot = 0, etot = 0):
        """
        Funcion que grafica la evolucion de la temperatura y las energias del sistema en funcion del tiempo
        """
        plt.ion()
        plt.xlim([0, nsteps + nsteps * (i / nsteps)])
        plt.grid(True)
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
