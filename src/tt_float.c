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


/*
struct _cell::_cell(int na){
    natoms = na;
};*/

/*
main(){
    _cell cc(10, 0, array);

    int o = cc.owner
}*/

/* structure to hold the complete information 
 * about the MD system */
/*
struct _mdsys {
    double dt, mass, epsilon, sigma, box, rcut;
    double ekin, epot, temp, _pad1;
    double *pos, *vel, *frc;
    cell_t *clist;
    int *plist, _pad2;
    int natoms, nfi, nsteps, nthreads;
    int ngrid, ncell, npair, nidx;
    double delta;
};
typedef struct _mdsys mdsys_t;
*/
