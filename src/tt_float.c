#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>


/* structure for cell-list data */
struct _cell {
    //_cell(int);
    int natoms;                 /* number of atoms in this cell */
    int owner;                  /* task/thread id that owns this cell */
    float *idxlist;               /* list of atom indices */
    //void run(void); // imposible in C?
};
typedef struct _cell cell_t;


struct _another{
    int a;
    float b;
    float *bb;
};
typedef struct _another inp;


float area(cell_t c){
    return c.natoms*c.owner*c.idxlist[0];
}




/* main */
int run(inp in) {
    int nprint, i;
    char restfile[BLEN], trajfile[BLEN], ergfile[BLEN], line[BLEN];
    FILE *fp,*traj,*erg;
    mdsys_t sys;

#if defined(_OPENMP)
#pragma omp parallel
    {
        if(0 == omp_get_thread_num()) {
            sys.nthreads=omp_get_num_threads();
            printf("Running OpenMP version using %d threads\n", sys.nthreads);
        }
    }
#else
    sys.nthreads=1;
#endif

    /* read input file */
    if(get_a_line(stdin,line)) return 1;
    sys.natoms=atoi(line);
    if(get_a_line(stdin,line)) return 1;
    sys.mass=atof(line);
    if(get_a_line(stdin,line)) return 1;
    sys.epsilon=atof(line);
    if(get_a_line(stdin,line)) return 1;
    sys.sigma=atof(line);
    if(get_a_line(stdin,line)) return 1;
    sys.rcut=atof(line);
    if(get_a_line(stdin,line)) return 1;
    sys.box=atof(line);
    if(get_a_line(stdin,restfile)) return 1;
    if(get_a_line(stdin,trajfile)) return 1;
    if(get_a_line(stdin,ergfile)) return 1;
    if(get_a_line(stdin,line)) return 1;
    sys.nsteps=atoi(line);
    if(get_a_line(stdin,line)) return 1;
    sys.dt=atof(line);
    if(get_a_line(stdin,line)) return 1;
    nprint=atoi(line);

    /* allocate memory */
    sys.pos=(double *)malloc(3*sys.natoms*sizeof(double));
    sys.vel=(double *)malloc(3*sys.natoms*sizeof(double));
    sys.frc=(double *)malloc(sys.nthreads*3*sys.natoms*sizeof(double));

    /* read restart */
    fp=fopen(restfile,"r");
    if(fp) {
        int natoms;
        natoms=sys.natoms;
        
        for (i=0; i<natoms; ++i) {
            fscanf(fp,"%lf%lf%lf",sys.pos+i, sys.pos+natoms+i, sys.pos+2*natoms+i);
        }
        for (i=0; i<natoms; ++i) {
            fscanf(fp,"%lf%lf%lf",sys.vel+i, sys.vel+natoms+i, sys.vel+2*natoms+i);
        }
        fclose(fp);
        azzero(sys.frc, 3*sys.nthreads*sys.natoms);
    } else {
        perror("cannot read restart file");
        return 3;
    }

    /* initialize forces and energies.*/
    sys.nfi=0;
    sys.clist=NULL;
    sys.plist=NULL;
    updcells(&sys);
    force(&sys);
    ekin(&sys);
    
    erg=fopen(ergfile,"w");
    traj=fopen(trajfile,"w");

    printf("Starting simulation with %d atoms for %d steps.\n",sys.natoms, sys.nsteps);
    printf("     NFI            TEMP            EKIN                 EPOT              ETOT\n");
    output(&sys, erg, traj);

    
    // clean up: close files, free memory 
    printf("Simulation Done.\n");
    fclose(erg);
    fclose(traj);
    free(sys.pos);
    free(sys.vel);
    free(sys.frc);
    free_cell_list(&sys);
    
    return 0;
}

//EOF
