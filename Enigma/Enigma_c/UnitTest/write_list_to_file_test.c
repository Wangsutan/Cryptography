#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    FILE *fp = NULL;
    fp = fopen("output_file_test_length.txt", "wb");

    int len_total = 6;
    int arr1[6] = {1, 2, 3, 4, 5, 6};
    fwrite(arr1, sizeof(arr1), 1, fp);
    fclose(fp);

    fp = fopen("output_file.txt", "rb");

    int arr2[6];
    fread(arr2, sizeof(arr2), 1, fp);
    fclose(fp);

    for (int i = 0; i < 6; i++)
    {
        printf("%d\n", arr2[i]);
    }

    int arr3[2][3];
    for (int i = 0; i < 6; i++)
    {
        arr3[i / 3][i % 3] = arr2[i];
        printf("arr3[%d][%d] = %d\n", i / 3, i % 3, arr3[i / 3][i % 3]);
    }

    return 0;
}
