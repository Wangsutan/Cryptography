#include <stdio.h>
int main()
{
    printf("%lu\n", sizeof(char));
    printf("%lu\n", sizeof(int));
    printf("%lu\n", sizeof(float));
    printf("%lu\n", sizeof(double));

    int int_array[] = {1, 2, 3, 4, 5, 6};
    printf("%lu\n", sizeof(int_array));
    printf("%lu\n", sizeof(int_array) / sizeof(int));
    return 0;
}
