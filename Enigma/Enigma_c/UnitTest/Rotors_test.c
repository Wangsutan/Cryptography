#include <stdio.h>

typedef struct Rotor {
    int* order;
    int cursor;
} Rotor;

int test(Rotor *p, int rotorNum, int order_len)
{
    Rotor *q;
    for ( q = p; q < p + rotorNum; q++ )
    {
        printf("q -> cursor: %d\n", q -> cursor);
        for (int j = 0; j < order_len; j++)
        {
            printf("q -> order[%d]: %d\n", j, q -> order[j]);
        }
        printf("\n");
    }
    return 0;
}

int main(void)
{
    int order_len = 25;
    int init_order[order_len];
    for (int i = 0; i < order_len; i++)
    {
        init_order[i] = i + 1;
    };

    int init_cursor = 0;

    int rotorNum = 3;
    Rotor rotorList[rotorNum];
    for (int i = 0; i < rotorNum; i++)
    {
        rotorList[i].order = init_order;
        rotorList[i].cursor = init_cursor;
    }

    test(rotorList, rotorNum, 25);

    return 0;
}
