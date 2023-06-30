#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(void)
{
    int plugboard_items[2][13] = {
        {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13},
        {14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}
    };


    char plainText[] = "TALKISCHEAPSHOWMETHECODE";

    // A-Z: 65-90.
    int i, j, k;
    int index_orig;
    int index_new;
    for (i = 0; i < strlen(plainText); i++)
    {
        index_orig = plainText[i] - ('A' - 1);
        printf("orig: %d\t%c\n", index_orig, plainText[i]);

        for (j = 0; j < 2; j++)
        {
            for (k = 0; k < 13; k++)
            {
                if ( index_orig == plugboard_items[j][k] )
                {
                    printf("index_orig: %d\n", index_orig);
                    index_new = plugboard_items[1 - j][k];
                    printf("index_new: %d\n", index_new);
                    printf("c: %c\n", index_new + ('A' - 1));
                    plainText[i] =  (char) index_new + ('A' - 1);
                }
            }
        }
        printf("new: %d\t%c\n", index_new, plainText[i]);
    }
    return 0;
}
