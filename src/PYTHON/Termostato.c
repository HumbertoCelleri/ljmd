
// Set simulation parameters


struct _andersen_termostat {
	double Temp;
	double nu;
	double velSTD;
};
typedef struct _andersen_termostat a_termostat;

void Andersen_termostat(mdsys_t *sys, a_termostat *a_term)
{

	int i;

	double dt = sys->dt;        // Integration time
	double dt2 = dt*dt;        // Integration time, squared

	double Temp = a_term->Temp;         // Simulation temperature
	double nu = a_term->nu;           // Thermostat parameter - frequency of collisions with the heat bath

	a_term->velSTD = sqrt(Temp/sys->mass); // Thermostat parameter - standard deviation of the velocity
 
        for (i = 0; i < 3*sys->natoms; ++i) {
        sys->ekin += sys->vel[i]*sys->vel[i];
    }
	// Implement the Andersen thermostat
	for(i = 0; i < self->natoms, i++)
	{
	//	Test for collisions with the Andersen heat bath
        
		if (rand() < nu*dt)
		{
	              // If the particle collided with the bath, draw a new velocity
        	      // out of a normal distribution
        	      sys->vel[i] = randGauss(0,velSTD,nDim);
        	      sys->vel[i + sys->natoms] = randGauss(0,velSTD,nDim);
        	      sys->vel[i + (sys->natoms)*2] = randGauss(0,velSTD,nDim);
		}
	}
}	

