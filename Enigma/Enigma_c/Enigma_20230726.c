#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <getopt.h>
#include <time.h>
#include <ctype.h>
#include <stdbool.h>

typedef struct Rotor {
    int order[25];
    int cursor;
} Rotor;

void shuffle_list(int* list, int listSize);
int findSize(char file_name[]);
char encipherAndDecipher(char ch, char* alphabet, int alphabet_len, int* order, int cursor, int sign);
void linkAndMoveRotors(Rotor* rotorList, int rotorNum, int idx);
void reflect(int reflection[], int reflectionLen, char plainText[], int i);

int main(int argc, char** argv)
{
    char* alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int alphabetLen = strlen(alphabet);

    int rotorsNum = 3;
    int order_init[25] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25};
    int cursor_init = 0;

    char passwordFrom = 'm';
    char passwordsFile[32] = "passwords.txt";
    int passwordLen = 25;

    char reflectionFrom = 'm';
    char reflectionFile[32] = "reflection.txt";
    int reflectionLen = 26;
    int reflection_init[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26};
    int reflection_unit[reflectionLen];

    char inputFile[32] = "inputFile.txt";
    char outputFile[32] = "outputFile.txt";

    FILE *fp = NULL;

    // get rotor number and locations of 4 files.
    const char* optstr = "hn:p:r:i:o:";
    char opt;
    while ((opt = getopt(argc, argv, optstr)) != -1)
    {
        switch (opt)
        {
            case 'h':
                printf("USAGE: %s %s\n", argv[0], optstr);
                break;
            case 'n':
                rotorsNum = atoi(optarg);
                break;
            case 'p':
                passwordFrom = 'M';
                strcpy(passwordsFile, optarg);
                break;
            case 'r':
                reflectionFrom = 'M';
                strcpy(reflectionFile, optarg);
                break;
            case 'i':
                strcpy(inputFile, optarg);
                break;
            case 'o':
                strcpy(outputFile, optarg);
                break;
            case '?':
                printf("Unknown option: %c\n", (char) optopt);
                break;
        }
    }

    Rotor rotorList[rotorsNum];
    int password_unit[rotorsNum * passwordLen];

    // get passwords
    if (passwordFrom == 'm')
    {
        for (int i = 0; i < rotorsNum; i++)
        {
            shuffle_list(order_init, sizeof(order_init) / sizeof(order_init[0]));
            for (int j = 0; j < passwordLen; j++)
            {
                password_unit[i * passwordLen + j] = order_init[j];
            }
        }
        fp = fopen(passwordsFile, "wb");
        fwrite(password_unit, sizeof(password_unit), 1, fp);
    } else if (passwordFrom == 'M')
    {
        int res = findSize(passwordsFile);
        if (rotorsNum * passwordLen != res / sizeof(int))
            exit(1);

        fp = fopen(passwordsFile, "rb");
        fread(password_unit, sizeof(password_unit), 1, fp);
    }

    // set order of rotors from passwords
    for (int i = 0; i < rotorsNum; i++)
    {
        rotorList[i].cursor = cursor_init;
        for (int j = 0; j < passwordLen; j++)
        {
            rotorList[i].order[j] = password_unit[i * passwordLen + j];
        }
    }

    // get reflection
    if ( reflectionFrom == 'm' )
    {
        shuffle_list(reflection_init, reflectionLen);
        for (int i = 0; i < reflectionLen; i++)
            reflection_unit[i] = reflection_init[i];

        fp = fopen( reflectionFile, "wb");
        fwrite(reflection_unit, sizeof(reflection_unit), 1, fp);
    } else if ( reflectionFrom == 'M' )
    {
        int res = findSize(reflectionFile);
        if (res / sizeof(int) != reflectionLen)
            exit(1);
        fp = fopen(reflectionFile, "rb");
        fread(reflection_unit, sizeof(reflection_unit), 1, fp);
    }

    // get plain text
    int res = findSize(inputFile);
    // printf("res: %d\n", res);
    int plainTextLen = res / sizeof(char);
    char plainText[plainTextLen];

    fp = fopen(inputFile, "r");
    fread(plainText, plainTextLen, 1, fp);
    plainText[plainTextLen] = '\0';
    // printf("%s\n", plainText);
    // printf("sizeof(plainText): %lu\n", sizeof(plainText));
    // printf("last char: %c\n", plainText[plainTextLen]);

    // encipher and decipher
    int  i, r;
    for (i = 0; i < plainTextLen; i++)
    {
        for (r = 0; r < rotorsNum; r++)
            plainText[i] = encipherAndDecipher(plainText[i], alphabet, alphabetLen, rotorList[r].order, rotorList[r].cursor, 1);

        reflect(reflection_unit, reflectionLen, plainText, i);

        for (r = 0; r < rotorsNum; r++)
            plainText[i] = encipherAndDecipher(plainText[i], alphabet, alphabetLen, rotorList[r].order, rotorList[r].cursor, -1);

        linkAndMoveRotors(&rotorList[0], rotorsNum, 0);
    }

    // save cipher text to file
    fp = fopen(outputFile, "w+");
    fwrite(plainText, sizeof(plainText), 1, fp);
    fclose(fp);

    return 0;
}

void shuffle_list(int* list, int listSize)
{
    srand((unsigned) time(NULL));
    for (int i = 0; i < listSize - 1; ++i)
    {
        int j = rand() % (listSize - i) + i;
        int temp = list[i];
        list[i] = list[j];
        list[j] = temp;
    }
}

int findSize(char* file_name)
{
    FILE* fp = fopen(file_name, "r");
    if (fp == NULL) {
        printf("File Not Found!\n");
        exit(1);
    }

    fseek(fp, 0, SEEK_END);
    int res = ftell(fp);
    fclose(fp);

    return res;
}

char encipherAndDecipher(char ch, char* alphabet, int alphabet_len, int* order, int cursor, int sign)
{
    int idx, index_orig, index_change, index_new;
    for (idx = 0; idx < alphabet_len; idx++)
    {
        if ( toupper(ch) == alphabet[idx] )
        {
            index_orig = idx;
            index_change = order[cursor] * sign;
            index_new = (index_orig + index_change + alphabet_len) % alphabet_len;

            ch = alphabet[index_new];
            break;
        }
    }
    return ch;
}

void linkAndMoveRotors(Rotor* rotorList, int rotorNum, int idx)
{
    int order_len = sizeof(rotorList[idx].order) / sizeof(int);
    // printf("order_len: %d\n", order_len);
    rotorList[idx].cursor = (rotorList[idx].cursor + 1) % order_len;
    if (rotorList[idx].cursor == 0 && idx < (rotorNum - 1) )
    {
        printf("Rotor[%d] Move!\n", idx);
        linkAndMoveRotors(rotorList, rotorNum, (idx + 1));
    }
}

void reflect(int reflection[], int reflectionLen, char plainText[], int i)
{
    int index_orig = (int)plainText[i] - (int)'A' + 1;
    for (int j = 0; j < reflectionLen; j++)
    {
        if ( index_orig == reflection[j] )
        {
            int index_new = reflection[(j  + (reflectionLen / 2)) % reflectionLen];
            plainText[i] =  (char) (index_new + (int) 'A' - 1);
            break;
        }
    }
}
