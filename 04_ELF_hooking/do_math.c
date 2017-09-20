#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(int argc, char **argv) {
  if (argc != 2) {
    printf("Usage: %s <a> \n", argv[0]);
    exit(-1);
  }

  int a = atoi(argv[1]);
  printf("exp(%d) = %f\n", a, exp(a));
  return 0;
}

