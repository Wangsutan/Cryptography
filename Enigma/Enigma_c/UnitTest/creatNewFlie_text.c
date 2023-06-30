#include <stdio.h>
#include <string.h>
#include <unistd.h>


int main(int argc, char* argv[])
{
    char* inputFile = "inputFile.txt";
    char* outputFile = "outputFile.txt";
    char ch;
    while ((ch = getopt(argc, argv, "i:o:")) != -1)
    {
        switch (ch)
        {
            case 'i':
                inputFile = optarg;
                break;
            case 'o':
                outputFile = optarg;
                break;
        }
    }

    for (int i = 0; i < argc; i++)
    {
        printf("%s\n", argv[i]);
    }

    printf("%s\n", inputFile);
    printf("%s\n", outputFile);

    char plainText[] = "HELLOWORLD\n";

    FILE *fp = NULL;
    fp = fopen(outputFile, "w+");
    fwrite(plainText, sizeof(plainText), 1, fp);
    fclose(fp);

    return 0;
}
