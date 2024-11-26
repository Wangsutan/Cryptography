#include <ctype.h>
#include <stdio.h>

char caesar_cipher(char c, const int shift);

int main(void) {
  char c = '\0';
  const int shift = 3;

  while ((c = getchar()) != '\n') {
    if (isupper(c)) {
      putchar(caesar_cipher(c, shift));
    }
  }
  putchar(c);

  return 0;
}

char caesar_cipher(char c, const int shift) {
  return (c + shift - 'A') % 26 + 'A';
}
