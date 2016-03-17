""" io.py contiene todas los metodos de entrada salida
"""

import numpy as np
import random
import mdinput as mdi

class Io_ljmd(object):
    """ La clase Io contiene todos los metodos de ingreso y salida"""
    def __init__(self,path):
        self.path=path


class Read_inputs(Io_ljmd):
    """ Clase que contiene los metodos de lectura"""
    def __init__(self,inpfile,path):
        self.inpfile = inpfile
        super(Read_inputs, self).__init__(path)

    def read(self): # AGREGAN POR DEFAULT y sacamos readline-> ASIGNAMOS
        """Este metodo lee los datos de los dos archivos de entrada y los
        devuelve como diccionario."""
        
        input_dict={}
        input_dict['natoms'] = mdi.natoms  # Number of atoms
        input_dict['mass'] = mdi.mass      # Mass in AMU
        input_dict['rcut'] = mdi.rcut      # Cut-off radius in angstrom
        input_dict['box'] = mdi.box        # Box length in angstrom
        if mdi.potential == 'lj':
            input_dict['epsilon'] = mdi.epsilon  # Epsilon in kcal/mol
            input_dict['sigma'] = mdi.sigma      # Sigma in angstrom
            input_dict['potential'] = 0
        elif mdi.potential == 'morse':
            input_dict['D_e'] = mdi.D_e  # D_e in kcal/mol
            input_dict['r_e'] = mdi.r_e  # r_e in angstrom
            input_dict['a'] = mdi.a      # a in 1/angstrom
            input_dict['potential'] = 1
        input_dict['restfile'] = mdi.restfile  # Filename for restart
        input_dict['trajfile'] = mdi.trajfile  # Filename for trajectories
        input_dict['ergfile'] = mdi.ergfile    # Filename for energies
        input_dict['nsteps'] = mdi.nsteps      # Number of MD steps
        input_dict['dt'] = mdi.dt              # MD time step (in fs)
        input_dict['nprint'] = mdi.nprint      # Output print frequency
        
        data=np.loadtxt(self.path+input_dict['restfile'])
        input_dict['pos']=np.reshape(data[:mdi.natoms,:],[mdi.natoms*3],'F')
        #input_dict['pos']=np.array([random.uniform(-mdi.box,mdi.box) for _ in range(mdi.natoms*3)])
        input_dict['vel']=np.reshape(data[mdi.natoms:,:],[mdi.natoms*3],'F')

        del data
        
        return input_dict



class Print_outputs(Io_ljmd):
    """ Este clase imprime (x,y,z) en xyzfile y (paso,temp, Ec, Ep,Et) en datfile

    Parameters
    ----------
        xyzfile :: (x,y,z)
        datfile :: (paso,temp, Ec, Ep,Et)

    Petodos
    -------
        printXYZ
        printDAT
    """

    def __init__(self,xyzfile, datfile,path):
        self.xyzfile = xyzfile
        self.datfile = datfile
        super(Print_outputs, self).__init__(path)
        """ Escribimos headers"""
        oXYZfile = open(self.path+self.xyzfile+'.xyz','w')
        oDATfile = open(self.path+self.datfile+'.dat','w')
        oXYZfile.write('nfi\tekin\tepot\tetor\n')
        oDATfile.write('Archivo con (paso,temp, Ec, Ep,Et)')
        oXYZfile.close()
        oDATfile.close()


    def printDAT(self,nfi,sys):
        """ metodo que imprime DAT

        Parameters
        ----------
            nfi :: paso de calculo
            sys :: sistema de estudio
        """
        oDATfile = open(self.path+self.datfile+'.dat','a')
        oDATfile.write("\n%i\t%.7f\t%.7f\t%.7f\t%.7f\n" % (nfi, sys.temp, sys.ekin, sys.epot, sys.ekin+sys.epot))
        oDATfile.close()


    def printXYZ(self,nfi,sys):
        """ metodo que imprime XYZ en xyzfile

        Parameters
        ----------
            nfi :: paso de calculo
            sys :: sistema de estudio
        """
        oXYZfile = open(self.path+self.xyzfile+'.xyz','a')
        oXYZfile.write("%i\n nfi = %i\n" % (sys.natoms, nfi))
        for runner in range(0,sys.natoms):
            oXYZfile.write("Ar\t%.7f\t%.7f\t%.7f\n" % (sys.pos[runner], sys.pos[runner+sys.natoms], sys.pos[runner+2*sys.natoms]))

        oXYZfile.close()
