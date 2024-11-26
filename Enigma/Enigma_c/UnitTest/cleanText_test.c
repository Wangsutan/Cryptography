#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void cleanText(char* inputText, char* result);

int main(void)
{
    // read original text as input text
    // char inputText[] = "Hello, 38World!";
    char inputText[1024];
    FILE *fp0 = NULL;
    fp0 = fopen("inputText.txt", "r");
    fgets(inputText, 1024, fp0);
    fclose(fp0);
    printf("inputText: %s %lu %lu\n", inputText, strlen(inputText), sizeof(inputText));

    // clean text
    char plainText[sizeof(inputText)];
    printf("plainText: %lu %lu\n", strlen(plainText), sizeof(plainText));

    cleanText(inputText, plainText);
    plainText[strlen(plainText)] = '\0';
    printf("plainText: %s %lu %lu\n", plainText, strlen(plainText), sizeof(plainText));

    // write string to file
    FILE *fp1 = NULL;
    fp1 = fopen("cleanText.txt", "w");
    fputs(plainText, fp1);
    fclose(fp1);

    // read string from file
    char readText[strlen(inputText) + 1];
    FILE *fp2 = NULL;
    fp2 = fopen("cleanText.txt", "r");
    fgets(readText, strlen(inputText) + 1, fp2);
    printf("readText: %s %lu %lu\n", readText, strlen(readText), sizeof(readText));
    fclose(fp2);

    return 0;
}

void cleanText(char* inputText, char* result)
{
    int  i, j;
    for (i = 0, j = 0; inputText[i] != '\0'; i++)
    {
        if ( isalpha(inputText[i]) )
        {
            result[j] = toupper(inputText[i]);
            j++;
        }
    }
    result[j] = '\0';
}
