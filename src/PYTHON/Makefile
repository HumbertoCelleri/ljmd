.PHONY: default help all clean

CC = gcc

default: help

help: 	
	@echo "\
Options:\n\n\
  make all:           build library\n\
  make clean:         delete output files\n\
  make help:          display this help"

all: 
	$(CC) -c -fPIC -fopenmp ljmd.c 
	$(CC) -shared -fopenmp ljmd.o -o libc.so

clean:
	rm -rfv ljmd.o ljmd.so
