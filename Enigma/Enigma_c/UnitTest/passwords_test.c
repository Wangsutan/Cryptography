#include <stdio.h>

int main(void)
{
    int passwords[3][25];
    int init_order[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25};
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 25; j++)
        {
            passwords[i][j] = init_order[j];
            printf("%d\n", passwords[i][j]);
        }
    }
    return 0;
}
