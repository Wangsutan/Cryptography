#include <stdio.h>
#include <string.h>

char encipherAndDecipher(char ch, char* alphabet, int alphabet_len, int* order, int cursor, int sign)
{
    int index_orig;
    printf("%d\n", alphabet_len);
    for (int j; j < alphabet_len; j++)
    {
        printf("%d\n", j);
        if ( ch == alphabet[j] )
        {
            printf("%d: true\n", j);
            index_orig = j;
            // break;
        }
    }
    int index_change = order[cursor] * sign;
    int index_new = (index_orig + index_change) % strlen(alphabet);
    ch = alphabet[index_new];
    return ch;
}

int main(void)
{
    char alphabet[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    int alphabet_len = sizeof(alphabet) / sizeof(alphabet[0]);
    printf("%d\n", alphabet_len);

    typedef struct Rotor {
        int* order;
        int cursor;
    } rotor_st;

    int init_order[25] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25};
    int init_cursor = 0;
    rotor_st rotor1 = {init_order, init_cursor};

    char ch = 'G';
    printf("%c\n", ch);

    int sign = -1;
    ch = encipherAndDecipher(ch, alphabet, alphabet_len, rotor1.order, rotor1.cursor, sign);
    printf("%c\n", ch);

    return 0;
}
