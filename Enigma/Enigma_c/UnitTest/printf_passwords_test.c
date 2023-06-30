//check passwords[i][j]
for (int i = 0; i < rotorsNum; i++)
{
    printf("password[%d]: ", i);
    for (int j = 0; j < passwordLen; j++)
        printf("%d ", passwords[i][j]);
    putchar('\n');
}
