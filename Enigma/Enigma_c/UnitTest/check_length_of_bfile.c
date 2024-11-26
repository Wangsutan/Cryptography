#include <stdio.h>
#include <stdlib.h>

long int findSize(char file_name[])
{
    FILE* fp = fopen(file_name, "r");
    if (fp == NULL) {
        printf("File Not Found!\n");
        return -1;
    }

    fseek(fp, 0L, SEEK_END);

    // calculating the size of the file
    long int res = ftell(fp);

    fclose(fp);

    return res;
}

// Driver code
int main()
{
    char file_name[] = { "output_file_test_length.txt" };
    int res = findSize(file_name);
    if (res != -1)
    {
        printf("Size of the file is %ld bytes \n", res);
    } else {
        printf("exit\n");
        exit(1);
    }

    int target_size = sizeof(int);
    int target_num = res / target_size;
    printf("target_num: %d\n", target_num);

    int num_expect = 6;
    printf("%s\n", num_expect == target_num? "Right!": "Wrong!");

    return 0;
}
