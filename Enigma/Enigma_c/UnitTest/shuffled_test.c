#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int* shuffle_list(int list[], int listSize)
{
    srand((unsigned) time(NULL));
    for (int i = 0; i < listSize - 1; i++)
    {
        int j = rand() % (listSize - i) + i;
        int temp = list[i];
        list[i] = list[j];
        list[j] = temp;
    }
    return list;
}

int main(void)
{
    int init_order[26] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26};
    int sizeofOrder = sizeof(init_order) / sizeof(init_order[0]);
    printf("sizeofOrder: %d\n", sizeofOrder);

    int new_order[sizeofOrder];
    for (int i = 0; i < sizeofOrder; i++)
    {
        new_order[i] = init_order[i];
    }

    shuffle_list(new_order, sizeofOrder);

    for (int i = 0; i < sizeofOrder; i++)
    {
        printf("init_order[%d]: %d\n", i, init_order[i]);
        printf("new_order[%d]: %d\n", i, new_order[i]);
    }
    return 0;
}
