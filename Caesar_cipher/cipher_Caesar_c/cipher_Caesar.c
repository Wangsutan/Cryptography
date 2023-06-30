#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <ctype.h>

char* cleanText(char* inputText);
char* encrypt(char* alphabet, int method, char* plainText);
int rotor(int alphabet_index_orig, int method, int sizeofAlphabet);

int main(int argc, char* argv[])
{
    char* alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int method;
    char* inputFile;
    char* outputFile;

    char* otherInfo = "-m <method> -i <input text file> -o <output text file>";

    int ch;
    while ((ch = getopt(argc, argv, "hm:i:o:")) != -1)
    {
        switch (ch)
        {
            case 'h':
                printf("USAGE: %s %s\n", argv[0], otherInfo);
                break;
            case 'm':
                method = atoi(optarg);
                break;
            case 'i':
                inputFile = optarg;
                break;
            case 'o':
                outputFile = optarg;
                break;
            case '?':
                printf("Unknown option: %c\n",(char)optopt);
                break;
        }
    }

    FILE *fp = NULL;
    char buff[1024];

    fp = fopen(inputFile, "r");
    fgets(buff, 1024, (FILE*)fp);

    char* plainText = cleanText(buff);
    char* cypheredText = encrypt(alphabet, method, plainText);

    fp = fopen(outputFile, "w+");
    fputs(cypheredText, fp);
    fclose(fp);

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

char* encrypt(char *alphabet, int method, char* plainText)
{
    int sizeofAlphabet = strlen(alphabet);
    int alphabet_index_orig;
    char* cypherText = malloc(1024 * sizeof(char));

    for (int i = 0; i < strlen(plainText); i++)
    {
        for (int alphabet_index_orig = 0; alphabet_index_orig < sizeofAlphabet; alphabet_index_orig++)
        {
            if (plainText[i] == alphabet[alphabet_index_orig])
            {
                int alphabet_index_new = rotor(alphabet_index_orig, method, sizeofAlphabet);
                char cypherChar = alphabet[alphabet_index_new];
                strncat(cypherText, &cypherChar, 1);
            }
        }
    }
    return cypherText;
}

int rotor(int alphabet_index_orig, int method, int sizeofAlphabet)
{
    int alphabet_index_new = (alphabet_index_orig + method) % sizeofAlphabet;
    return alphabet_index_new;
}
