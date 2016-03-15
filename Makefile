.PHONY: default help
# -*- Makefile -*-
SHELL=/bin/sh

# compiler flags
FC=gcc
CFLAGS=-Wall -g -O3 -ffast-math -fomit-frame-pointer
FFLAGS=-Wall -g -std=f95 $(OPT)
PARALLEL=-fopenmp
# list of source files
SRC=ljmd.c

default: help

help:
	@echo "\
Options:\n\n\
  make preprocessing: gcc runs up to pre-processor and stops, creating calculator.pp_c\n\
  make assembler:     gcc runs up to assembler code generation and stops, creating calculator.asm\n\
  make object:        gcc runs up to the creation of the binary object calculator.o\n\
  make executable:    gcc goes all the way and creates the executable calculator.e\n\
  make all:           build all previous\n\
  make clean:         delete output files\n\
  make help:          display this help"

############################################
# derived makefile variables
OBJ_SERIAL=$(SRC:src/%.c=Obj-serial/%.o)
OBJ_PARALLEL=$(SRC:src/%.c=Obj-parallel/%.o)
############################################

serial: serial

parallel:	parallel

all: serial parallel

serial parallel:
	$(MAKE) $(MFLAGS) -C Obj-$@

clean:
	$(MAKE) $(MFLAGS) -C Obj-serial clean
	$(MAKE) $(MFLAGS) -C Obj-parallel clean
