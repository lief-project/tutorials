// clang -fPIC -shared libexample.c -o libexample.dylib
#include <stdio.h>
#include <stdlib.h>

__attribute__((constructor))
void my_constructor(void) {
  printf("Hello World\n");
}
