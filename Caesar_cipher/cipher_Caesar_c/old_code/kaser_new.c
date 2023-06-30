#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define CIPHER 3;

int ensure_range(int txt, int length, int min, int max);
/*
 * A-Z: 65-90
 * a-z: 97-122
 */

int main(void) {
    char orig_text[128];
    char plain_text[128];
    char cipher_text[128];

    printf("Input a text please:\n");
    scanf("%s", orig_text);

    printf("save alphabet only: ");
    int count = 0;
    for (int i = 0; i < strlen(orig_text); i++) {
        if (( orig_text[i] >= 'A' && orig_text[i] <= 'Z')
            || ( orig_text[i] >= 'a' && orig_text[i] <= 'z')) {
            printf("%c", orig_text[i]);
            plain_text[count] = orig_text[i];
            count++;
        }
    }
    printf("\n");

    int len = strlen(plain_text);
    printf("strlen: %d\n", len);

    for (int i = 0; i < len; i++) {
        plain_text[i] = toupper(plain_text[i]);
    }
    printf("plain text\t%s\n", plain_text);

    printf("cipher text\t");
    for (int i = 0; i < len; i++) {
        cipher_text[i] = plain_text[i] + CIPHER;
        cipher_text[i] = ensure_range(cipher_text[i], 26, 65, 90);
        putchar(cipher_text[i]);
    }
    printf("\n");

    printf("decipher text\t");
    for (int i = 0; i < len; i++) {
        cipher_text[i] -= CIPHER;
        cipher_text[i] = ensure_range(cipher_text[i], 26, 65, 90);
        putchar(cipher_text[i]);
    }
    printf("\n");

    return 0;
}

int ensure_range(int txt, int length, int min, int max) {
    while (txt < min) {
        txt += length;
    }
    while (txt > max) {
        txt -= length;
    }
    return txt;
}
