CC=gcc
CXX=g++

all: crackme.bin hook

crackme.bin: crackme.c
	$(CC) $^ -O3 -o $@
	chmod u+rx $@

hook: hook.c
	$(CC) -nostdlib -nodefaultlibs -fPIC -Wl,-shared $^ -o $@

.PHONY: clean

clean:
	rm -rf *.o *~ *.so *.bin hook *.hooked
