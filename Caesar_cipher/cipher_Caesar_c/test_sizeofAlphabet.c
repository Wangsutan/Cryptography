#include <stdio.h>
#include <string.h>

int main(void)
{
    char* alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int len_alphabet = strlen(alphabet);
    printf("%d\n", len_alphabet);
    int sizeofAlphabet = (int) sizeof(alphabet) / sizeof(alphabet[0]);
    printf("%d\n", sizeofAlphabet);

    printf("%c\n", alphabet[0]);
    return 0;
}
