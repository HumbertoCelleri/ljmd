# Estructura en python de ljmd.c

## Includes

## Physical constants

## Estructuras

### **_cell**
      Structure for cell-list data
      1. Atributos
        int natoms
        int owner
        int * idxlist

#### Alias: cell_t

### **_mdsys**
      Structure to hold the complete information
      about the MD system
      1. Atributos
        ```
        double dt, mass, epsilon, sigma, box, rcut;
        double ekin, epot, temp, _pad1;
        double *pos, *vel, *frc;
        cell_t *clist;
        int *plist, _pad2;
        int natoms, nfi, nsteps, nthreads;
        int ngrid, ncell, npair, nidx;
        double delta;
        ```
#### Alias mdsys_t

## Funciones

### **get_a_line**
      helper function: read a line and then return
      the first string with whitespace stripped off

      1. Input
        ```
        FILE *fp, char *buf
        ```

      2. Output: int
          ```
          return 0
          ```

### **azzero**
      helper function: zero out an array

      1. Input
        ```
        double *d, const int n
        ```
      2. Output: void

      3. Special comments
        ```
        __attribute__((always_inline))
        ```

### **pbc**
      helper function: apply minimum image convention
      1. Input
        ```
        double x, const double boxby2, const double box
        ```
      2. Output: double
        ```
        return x
        ```

      3. Special comments
        ```
        __attribute__((always_inline))
        ```

### **updcells**
      build and update cell list
      1. Input
        ```
        mdsys_t *sys
        ```
      2. Output: void

      3. Special comments
        **Tiene printf**
        **exit(1)**: VER:
        http://stackoverflow.com/questions/24349806/catch-exception-in-ctypes-based-on-c-exit-code

### **free_cell_list**
      release cell list storage

      1. Input:
        ```
        mdsys_t *sys
        ```

      2. Output: void

### **ekin**
      compute kinetic energy

      1. Input
        ```
        mdsys_t *sys
        ```
      2. Output: void

### **force**
      compute forces

      1. Input
        ```
        mdsys_t *sys
        ```
      2. Output: void    

      3. Special comments
        1. **Como es el tema con OpenMP**
        2. Llama **azzero**, **pbc**

### **velverlet**
      velocity verlet

      1. Input
      ```
      mdsys_t *sys
      ```
      2. Output: void  

      3. Special comments
        1. Usa **force**

### **output**
      append data to output

      1. Input
        ```
        mdsys_t *sys, FILE *erg, FILE *traj
        ```
      2. output: void

      3. Special comments
        1. Usa **printf**, **fprintf**

### MAIN

      1. Se define sys.nthreads si `defined(_OPENMP)`
      2. Se lee el archivo ingresado como `./*.x < *.inp` mediante standart input
      3. Memory Allocation
      4. **restfile**: fscanf , perror
      5. Initialize forces and energies
      6. Open other files
      7. MAIN loop
          1. output
          2. velverlet
          3. ekin
          4. updcells
      8. clean up
      9. return 0
