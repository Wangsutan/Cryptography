#include <stdio.h>
#include <string.h>

char moveCursor(int* order, int order_len, int cursor)
{
    cursor = (cursor + 1) % order_len;
    return cursor;
}

int main(void)
{
    typedef struct Rotor {
        int* order;
        int cursor;
    } rotor_st;

    int init_order[25] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25};
    int init_cursor = 0;
    rotor_st rotor1 = {init_order, init_cursor};

    int order_len = sizeof(init_order) / sizeof(init_order[0]);
    // int order_len = *(&init_order + 1) - init_order;
    printf("order_len: %d\n", order_len);

    for (int i; i < 64; i++)
    {
        rotor1.cursor = moveCursor(rotor1.order, 25, rotor1.cursor);
        printf("%d\n", rotor1.cursor);
    }
    return 0;
}
