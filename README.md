This package contains simplified MD code with multi-threading
parallelization for simulating atoms with a Lennard-Jones potential.

The bundled makefiles are set up to compile the executable once
with OpenMP disabled and once with OpenMP enabled with each build
placing the various object files in separate directories.

The examples directory contains 3 sets of example input decks
and the reference directory the corresponding outputs.

Type: make
to compile everything and: make clean
to remove all compiled objects

Original code from Axel Kohlmeyer: https://github.com/akohlmey/ljmd-c

Para el [Workshop en Técnicas de Programación Científica](wp.df.uba.ar/wtpc)
