import numpy as np 
import tt

natoms = 108
mass = 0.01

# Construyo un vector de velocidades para probar
# Las velocidades en todas las direcciones 
# valen 1 
vel = []
for i in range(natoms * 3):
    vel.append(1)
vel = np.array(vel, dtype = np.float)


# Creo un objeto mdsys_t: por ahora solo hace falta
# el numero de atomos, la masa, y la lista de velocidad
A = tt.mdsys_t(natoms, mass, vel)

# Imprimo la energia cinetica y la temperatura
print A.kinetic_energy()
print A.temp
        


