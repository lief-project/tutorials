PYTHON_BINARY=$(shell which python)
CURRENT_DIRECTORY=$(shell pwd)

all: hashme

hashme: hashme.c
	$(CC) $^ -O0 -o $@ -lm
	chmod u+rx $@

run: all
	$(CURRENT_DIRECTORY)/hashme 123
	$(PYTHON_BINARY) script.py
	chmod u+x $(CURRENT_DIRECTORY)/hashme.obf
	LD_LIBRARY_PATH=$(CURRENT_DIRECTORY) $(CURRENT_DIRECTORY)/hashme.obf 123

.PHONY: clean

clean:
	rm -rf *.o *~ *.so.* *.bin hashme hashme.obf
