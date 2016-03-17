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
	$(CC) -c -g -O0 -fPIC ljmd.c 
	$(CC) -shared ljmd.o -o libc.so

parallel:
	$(CC) -c -fopenmp -fPIC ljmd.c 
	$(CC) -shared ljmd.o -fopenmp -o libc_MP.so


clean:
	rm -rfv ljmd.o libc.so libc_MP.so *.pyc
