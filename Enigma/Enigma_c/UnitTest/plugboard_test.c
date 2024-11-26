#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define ALPHABET "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#define ALPHABET_LEN strlen(ALPHABET)

int main(void)
{
    int plugboard_items[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26};

    int plugboard[2][ALPHABET_LEN / 2];
    for (int i = 0; i < ALPHABET_LEN; i++)
    {
        plugboard[i / (ALPHABET_LEN / 2)][i % (ALPHABET_LEN / 2)] = plugboard_items[i];
    }

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < ALPHABET_LEN / 2; j++)
        {
            printf("plugboard[%d][%d]] = %d\n", i, j, plugboard[i][j]);
        }
    }
    return 0;
}
