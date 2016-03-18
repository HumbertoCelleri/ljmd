help:
	@echo "\
Opciones:\n\n\
  make build:    Compila las librerías y crea el link ejecutable molecular_dynamics.py.\n\
  make clean:    Borra los archivos compilados y los archivos de salida generados.\n"

build:
	cd src; $(MAKE) all;\
	chmod u+x main.py; cd ..;\
	ln -s src/main.py; mv main.py molecular_dynamics.py

clean:
	cd src; $(MAKE) clean; cd ..;\
	rm molecular_dynamics.py;\
	cd data; rm *.xyz *.dat *.png; cd ..
