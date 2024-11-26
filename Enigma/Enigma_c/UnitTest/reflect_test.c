#include <stdio.h>

void reflect(int *p)
{
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 13; j++)
            printf("idx: %d\n", p[i * 13 + j]);
}

int main(void)
{
    int reflection[2][13] = {{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}, {14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}};
    reflect(*reflection);

    return 0;
}
