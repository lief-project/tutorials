CC=gcc
CXX=g++

all: crackme101.bin instrument.bin

crackme101.bin: crackme101.c
	$(CC) $^ -O0 -fPIE -pie -Wl,-strip-all -o $@
	chmod u+rx $@

instrument.bin: instrument.c
	$(CC) $^ -O0 -fPIE -pie -o $@ -ldl
	chmod u+rx $@

run: crackme101.bin instrument.bin
	./instrument.bin test
	./instrument.bin easy

.PHONY: clean

clean:
	rm -rf *.o *~ *.so *.bin
