#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char ch;
    const int cipher = 3;

    printf("Caesar Cipher.\n");
    printf("Input your string:\n");
    while ((ch = getchar()) != '\n')
    {
        if (isalpha(ch))
            putchar((toupper(ch) + cipher - 'A') % 26 + 'A');
    }
    putchar(ch);

    return 0;
}
