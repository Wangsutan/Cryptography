#include <stdio.h>

int* fun1(int *arr)
{
    arr[0] = 10;
    arr[1] = 20;
    return arr;
}

int* fun2(int arr[])
{
    arr[0] = 10;
    arr[1] = 20;
    return arr;
}

int main(void)
{
    int arr[100] = {0};
    int* ptr = fun2(arr);
    printf("%d %d\n", arr[0], arr[1]);
    printf("%d %d\n", ptr[0], ptr[1]);
    return 0;
}
