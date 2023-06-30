#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    char crib[] = "HITLER";
    printf("crib: %s\n", crib);

    char string_cipyer[] = "GBORNUNPXRELBHUNIRGBQRIRYBCFBZRBSGURFRNGGVGHQRF";

    int i = 0;
    while ( i <= strlen(string_cipyer) - strlen(crib) ) {
        bool conflict = false;
        int j = 0;
        while ( j < strlen(crib) ) {
            if ( string_cipyer[i + j] == crib[j] ) {
                conflict = true;
            }
            j += 1;
        }
        if ( !conflict ) {
            printf("%d\n", i);
        }
        i += 1;
    }

    return 0;
}
