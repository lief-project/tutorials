#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>

typedef int(*check_t)(char*);

int main (int argc, char** argv) {

  void* handler = dlopen("./libcrackme101.so", RTLD_LAZY);
  if (!handler) {
    fprintf(stderr, "dlopen error: %s\n", dlerror());
    return 1;
  }
  check_t check_found = (check_t)dlsym(handler, "check_found");

  int output = check_found(argv[1]);

  printf("Output of check_found('%s'): %d\n", argv[1], output);

  return 0;
}
