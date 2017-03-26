#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Damn_YoU_Got_The_Flag
char password[] = "\x18\x3d\x31\x32\x03\x05\x33\x09\x03\x1b\x33\x28\x03\x08\x34\x39\x03\x1a\x30\x3d\x3b";

inline int check(char* input);

int check(char* input) {
  for (int i = 0; i < sizeof(password) - 1; ++i) {
    password[i] ^= 0x5c;
  }
  return memcmp(password, input, sizeof(password) - 1);
}

int main(int argc, char **argv) {
  if (argc != 2) {
    printf("Usage: %s <password>\n", argv[0]);
    return EXIT_FAILURE;
  }

  if (strlen(argv[1]) == (sizeof(password) - 1) && check(argv[1]) == 0) {
    puts("You got it !!");
    return EXIT_SUCCESS;
  }

  puts("Wrong");
  return EXIT_FAILURE;

}

