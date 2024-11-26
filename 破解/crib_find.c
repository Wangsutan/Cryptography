#include <stdbool.h>
#include <stdio.h>
#include <string.h>

int main() {
  char crib[] = "HITLER";
  printf("crib: %s\n", crib);

  char string_cipyer[] = "GBORNUNPXRELBHUNIRGBQRIRYBCFBZRBSGURFRNGGVGHQRF";

  int i = 0;
  while (i <= strlen(string_cipyer) - strlen(crib)) {
    bool is_conflict = false;
    int j = 0;
    while (j < strlen(crib)) {
      if (string_cipyer[i + j] == crib[j]) {
        is_conflict = true;
      }
      j += 1;
    }
    if (!is_conflict) {
      printf("%d\n", i);
    }
    i += 1;
  }

  return 0;
}
