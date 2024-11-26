#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(void)
{
    char str_orig[] = "HelloWorld";
    char str_new[] = "HELLOWORLD";

    if (strcmp(str_orig, str_new) != 0)
        printf("Have same character!");
    return 0;
}
