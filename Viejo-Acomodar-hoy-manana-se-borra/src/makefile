SRC=tt_float.c #tt.c
obj:
	gcc -c -fPIC ${SRC} -o tt.o
	gcc -shared tt.o -o mylib.so

clean:
	rm *.so *.o
