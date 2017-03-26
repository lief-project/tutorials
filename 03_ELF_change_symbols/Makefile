CC=gcc
CXX=g++

all: hashme

hashme: hashme.c
	$(CC) $^ -O0 -o $@ -lm
	chmod u+rx $@

run: all
	unset LD_LIBRARY_PATH
	./hashme 123
	python script.py
	chmod u+x ./hashme.obf
	LD_LIBRARY_PATH=. ./hashme.obf 123

.PHONY: clean

clean:
	rm -rf *.o *~ *.so.* *.bin hashme hashme.obf
