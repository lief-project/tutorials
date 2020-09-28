#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define NOINLINE __attribute__ ((noinline))

NOINLINE int check_found(char* input) {
  if (strcmp(input, "easy") == 0) {
    return 1;
  }
  return 0;
}

int main(int argc, char** argv) {

  if (argc != 2) {
    printf("Usage: %s flag\n", argv[0]);
    exit(-1);
  }

  if (check_found(argv[1])) {
    printf("Well done!\n");
  } else {
    printf("Wrong!\n");
  }
  return 0;
}
