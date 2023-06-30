#include <stdio.h>

int main(void)
{
    int test1[2][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}};
    int password_unit[2 * 4];
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            password_unit[i * 4 + j] = test1[i][j];
            printf("password_unit[%d]: %d\n", i * 4 + j, password_unit[i * 4 + j]);
        }
    }

    int test2[2][4];
    for (int i = 0; i < 8; i++)
    {
        test2[i / 4][i % 4] = password_unit[i];
        printf("test2[%d][%d]: %d\n", i / 4, i % 4, test2[i / 4][i % 4]);
    }

    return 0;
}
