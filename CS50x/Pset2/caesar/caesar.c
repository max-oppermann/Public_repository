#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string cipher(string text, int key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Wrong number of command-line arguments\n");
        return 1;
    }
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    int key = atoi(argv[1]);
    string ptext = get_string("plaintext:  ");
    printf("ciphertext: %s\n", cipher(ptext, key));
    return 0;
}

string cipher(string text, int key)
{
    for (int i = 0; i < strlen(text); i++)
    {
        if (isupper(text[i]))
        {
            text[i] = ((((int) text[i] - 65) + key) % 26) + 65;
        }
        if (islower(text[i]))
        {
            text[i] = ((((int) text[i] - 97) + key) % 26) + 97;
        }
    }
    return text;
}

/*
individual letters, k is the key
c_i = (p_i + k) % 26

uppercase
text[i] = ((((int)text[i]-65) + k) % 26) + 65

lowercase
text[i] = ((((int)text[i]-97) + k) % 26) + 97


*/
