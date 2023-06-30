#include <stdio.h>
#define SPACE ' '
int main(void) {
  char ch;
  while ((ch = getchar()) != '\n'){
    if (ch != SPACE){    //Do not put space.
      if ((ch <= 90) && ((ch + 3) > 90)){
	/* still return letter. */
	putchar(ch + 3 - 26);
      }
      else {
	putchar(ch + 3);
      }
    }
  }
  putchar(ch);    //Now `ch` is '\n'.

  return 0;
}
