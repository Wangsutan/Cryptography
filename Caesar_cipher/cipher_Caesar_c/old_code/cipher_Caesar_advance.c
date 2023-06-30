#include <stdio.h>
#include <ctype.h>

/* p.155-156. */

int main(void) {
  char ch;
  while ((ch = getchar()) != '\n') {
    if (isalpha(ch)) {
      putchar(toupper(ch + 3));
    }
    else {
      putchar(toupper(ch));
    }
  }
  return 0;
}
