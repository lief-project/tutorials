CC=gcc
CXX=g++

all: crackme.bin hook

crackme.bin: crackme.c
	$(CC) $^ -O3 -o $@
	chmod u+rx $@

hook: hook.c
	$(CC) -Wl,-T script.ld -fno-stack-protector -nostdlib -nodefaultlibs -fPIC -Wl,-shared $^ -o $@

run: all
	python ./hook_pltgot.py
	chmod u+x ./crackme.hooked
	./crackme.hooked XXXXXXXXXXXXXXXXXXXXX


.PHONY: clean

clean:
	rm -rf *.o *~ *.so *.bin hook *.hooked
