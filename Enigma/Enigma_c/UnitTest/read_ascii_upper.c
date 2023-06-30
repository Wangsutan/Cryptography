#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char* cleanText(char* inputText);

int main(void)
{
    FILE *fp = NULL;
    char buff[1024];

    fp = fopen("plainTextTest.txt", "r");
    fgets(buff, 1024, (FILE*)fp);

    char* plainText = cleanText(buff);

    fclose(fp);

    for (int i = 0; i < 1024; i++)
        if ( isalpha(plainText[i]) )
        {
            printf("%c\n", plainText[i]);
        } else {
            printf("%c\n", plainText[i]);
            break;
        }

    return 0;
}

char* cleanText(char* inputText)
{
    char* plainText = malloc(strlen(inputText) * sizeof(char));
    for (int i = 0; i < strlen(inputText); i++)
    {
        if ( isalpha(inputText[i]) )
        {
            inputText[i] = toupper(inputText[i]);
            strncat(plainText, &inputText[i], 1);
        }
    }
    return plainText;
}
