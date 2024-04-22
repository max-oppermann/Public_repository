#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string cipher(string text, string key);
string force_upper(string text);
int valid_key(string text);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Wrong number of command-line arguments\n");
        return 1;
    }
    string uppercase_key = force_upper(argv[1]);
    if (valid_key(uppercase_key) == 1)
    {
        printf("Invalid key\n");
        return 1;
    }
    string ptext = get_string("plaintext:");
    printf("ciphertext:%s\n", cipher(ptext, uppercase_key));
}

string cipher(string text, string key)
{
    for (int i = 0; i < strlen(text); i++)
    {
        if (isupper(text[i]))
        {
            text[i] = key[text[i] - 65];
        }
        else if (islower(text[i]))
        {
            text[i] = tolower(key[text[i] - 97]);
        }
    }
    return text;
}

int valid_key(string text) // repetitions, alphabetic, length = 26
{
    if (strlen(text) != 26)
    {
        return 1;
    }
    for (int i = 0; i < strlen(text); i++)
    {
        if (!isalpha(text[i]))
        {
            return 1;
        }
        for (int j = 0; j < strlen(text); j++)
        {
            if (text[i] == text[j] && i != j)
            {
                return 1;
            }
        }
    }
    return 0;
}

string force_upper(string text)
{
    for (int i = 0; i < strlen(text); i++)
    {
        if (islower(text[i]))
        {
            text[i] = toupper(text[i]);
        }
    }
    return text;
}
