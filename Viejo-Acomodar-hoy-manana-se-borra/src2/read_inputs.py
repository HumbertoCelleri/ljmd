´´´
Esta funcion lee los inputs de los archivos *.inp y
*.rest y los devuelve como diccionario.
´´´

import numpy as np

def read_inputs ( case , path ) :
    ifile = open(path+'/examples/'+case+'.inp','r')
    dict={\
         'natoms': int(ifile.readline().split(' ')[0]),\ # Number of atoms
         'mass' : float(ifile.readline().split(' ')[0]),\ # Mass in AMU
         'epsilon' : float(ifile.readline().split(' ')[0]),\ # Epsilon in kcal/mol
         'sigma' : float(ifile.readline().split(' ')[0]),\ # Sigma in angstrom
         'rcut' : float(ifile.readline().split(' ')[0]),\ # Cut-off radius in angstrom
         'box' : float(ifile.readline().split(' ')[0]),\ # Box length in angstrom
         'restfile' : ifile.readline().split(' ')[0],\ # Filename for restart
         'trajfile' : ifile.readline().split(' ')[0],\ # Filename for trajectories
         'ergfile' : ifile.readline().split(' ')[0],\ # Filename for energies
         'nsteps' : int(ifile.readline().split(' ')[0]),\ # Number of MD steps
         'dt' : float(ifile.readline().split(' ')[0]),\ # MD time step (in fs)
         'nprint' : int(ifile.readline().split(' ')[0]) # Output print frequency
         }
    ifile.close()
    
    data=np.loadtxt(dict['restfile'])
    dict['pos']=np.reshape(data[:dict['natoms'],:],[dict['natoms']*3],'F')
    dict['vel']=np.reshape(data[dict['natoms']:,:],[dict['natoms']*3],'F')
    del data
    
    dict={'natoms':natoms, 'mass':mass, 'epsilon':epsilon, 'sigma':sigma,\
          'rcut':rcut, 'box':box, 'restfile':restfile, 'trajfile':trajfile,\
          'ergfile':ergfile, 'nsteps':nsteps, 'dt':dt, 'nprint':nprint}
    
    return dict
