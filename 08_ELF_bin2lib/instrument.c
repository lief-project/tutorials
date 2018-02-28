#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>
typedef int(*check_t)(char*);
int main (int argc, char** argv) {

  void* handler = dlopen("./libcrackme101.so", RTLD_LAZY);
  check_t check_function = (check_t)dlsym(handler, "check");

  int output = check_function(argv[1]);

  printf("Output of check('%s'): %d\n", argv[1], output);

  return 0;
}
