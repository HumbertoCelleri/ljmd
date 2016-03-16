import numpy as np

def read_inputs ( inpfile , path ) :
    """Esta funcion lee los datos de los dos archivos de entrada y los
    devuelve como diccionario."""

    ifile = open(path+'/examples/'+inpfile+'.inp','r')
    dict={}
    dict['natoms'] = int(ifile.readline().split(' ')[0]) # Number of atoms
    dict['mass'] = float(ifile.readline().split(' ')[0]) # Mass in AMU
    dict['epsilon'] = float(ifile.readline().split(' ')[0]) # Epsilon in kcal/mol
    dict['sigma'] = float(ifile.readline().split(' ')[0]) # Sigma in angstrom
    dict['rcut'] = float(ifile.readline().split(' ')[0]) # Cut-off radius in angstrom
    dict['box'] = float(ifile.readline().split(' ')[0]) # Box length in angstrom
    dict['restfile'] = ifile.readline().split(' ')[0] # Filename for restart
    dict['trajfile'] = ifile.readline().split(' ')[0] # Filename for trajectories
    dict['ergfile'] = ifile.readline().split(' ')[0] # Filename for energies
    dict['nsteps'] = int(ifile.readline().split(' ')[0]) # Number of MD steps
    dict['dt'] = float(ifile.readline().split(' ')[0]) # MD time step (in fs)
    dict['nprint'] = int(ifile.readline().split(' ')[0]) # Output print frequency
    dict['D_e'] = dict['epsilon']
    dict['a'] = 6./dict['sigma']
    dict['r_e'] = dict['sigma']
    dict['method'] = 'lj'
    ifile.close()
    
    data=np.loadtxt(path+'/examples/'+dict['restfile'])
    dict['pos']=np.reshape(data[:dict['natoms'],:],[dict['natoms']*3],'F')
    dict['vel']=np.reshape(data[dict['natoms']:,:],[dict['natoms']*3],'F')
    del data
    
    return dict
