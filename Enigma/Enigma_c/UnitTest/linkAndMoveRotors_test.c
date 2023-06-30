#include <stdio.h>
#include <string.h>

typedef struct Rotor {
    int* order;
    int cursor;
} Rotor;

int moveCursor(int* order, int order_len, int cursor)
{
    cursor = (cursor + 1) % order_len;
    return cursor;
}

int linkAndMoveRotors(Rotor *p, int rotorNum, int idx)
{
    (p + idx) -> cursor = moveCursor((p + idx) -> order, 25, (p + idx) -> cursor);
    if ( (p + idx) -> cursor == 0 && idx < (rotorNum - 1) )
    {
        printf("Rotor[%d] -> Cursor = %d: Rotor[%d] Move!\n", idx, (p + idx) -> cursor, idx);
        linkAndMoveRotors(p, rotorNum, idx + 1);
    }
    return 0;
}

int main(void)
{
    int init_order[25] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25};
    int init_cursor = 0;

    int rotorNum = 3;
    Rotor rotorList[rotorNum];
    for (int i = 0; i < rotorNum; i++)
    {
        rotorList[i].order = init_order;
        rotorList[i].cursor = init_cursor;
    }

    int str_len = 1024;
    for (int i = 0; i < str_len; i++)
        {
            linkAndMoveRotors(rotorList, rotorNum, 0);
        }
    return 0;
}
