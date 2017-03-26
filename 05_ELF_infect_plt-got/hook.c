#include "arch/x86_64/syscall.c"
#define stdout 1

int my_memcmp(const void* lhs, const void* rhs, int n) {
  const char msg[] = "Hook add\n";
  _write(stdout, msg, sizeof(msg));
  _write(stdout, (const char*)lhs, n);
  _write(stdout, "\n", 2);
  _write(stdout, (const char*)rhs, n);
  _write(stdout, "\n", 2);
  return 0;
}
