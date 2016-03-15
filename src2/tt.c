#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

/* a few physical constants */
const double kboltz=0.0019872067;     /* boltzman constant in kcal/mol/K */
const double mvsq2e=2390.05736153349; /* m*v^2 in kcal/mol */

/* Valores de prueba para chequear el resultado
const double kboltz = 1.00;
const double mvsq2e = 1.00;
*/


/* structure for cell-list data */
struct _cell {
    //_cell(int);
    int natoms;                 /* number of atoms in this cell */
    int owner;                  /* task/thread id that owns this cell */
    int *idxlist;               /* list of atom indices */
};
typedef struct _cell cell_t;


/* structure to hold the complete information 
 * about the MD system */

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


/* compute kinetic energy */
void ekin(mdsys_t *sys)
{   
    int i;

    sys->ekin=0.0;
    for (i=0; i< 3*sys->natoms; ++i) {
        sys->ekin += sys->vel[i]*sys->vel[i];
    }
    sys->ekin *= 0.5*mvsq2e*sys->mass;
    sys->temp  = 2.0*sys->ekin/(3.0*sys->natoms-3.0)/kboltz;
}

