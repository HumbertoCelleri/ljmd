.PHONY: default help all clean

CC = gcc

default: help

help: 	
	@echo "\
Options:\n\n\
  make all:           build library serial and parallel\n\
  make serial:        build library serial\n\
  make parallel:      build library parallel\n\
  make clean:         delete output files\n\
  make help:          display this help"

all: serial parallel

serial:
	$(CC) -c -fPIC ljmd.c 
	$(CC) -shared ljmd.o -o libc.so

parallel:
	$(CC) -c -fopenmp -fPIC ljmd.c 
	$(CC) -shared ljmd.o -o -fopenmp libc_MP.so


clean:
	rm -rfv ljmd.o ljmd.so
