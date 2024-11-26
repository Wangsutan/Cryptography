// check reflection[i][j]
for (int i = 0; i < 2; i++)
{
    printf("reflection[%d]: ", i);
    for (int j = 0; j < alphabetLen / 2; j++)
    {
        printf("%d ", reflection[i][j]);
    }
    putchar('\n');
}
