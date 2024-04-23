// Implements a dictionary's functionality
#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

int counter = 0;
int load_success = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 676; // 26^2

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false; case independently
bool check(const char *word)
{
    int index = hash(word);
    node *ptr = table[index];
    while (ptr != NULL)
    {
        if (strcasecmp(ptr->word, word) == 0)
        {
            return true;
        }
        ptr = ptr->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Handle case when only one letter
    if (strlen(word) == 1)
    {
        return toupper(word[0]) - 'A';
    }
    else
    {
        return (26 * (toupper(word[0]) - 'A') + (toupper(word[1]) - 'A'));
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        return false;
    }

    char new_word[LENGTH + 1];
    while (!(fscanf(source, "%s", new_word) == EOF))
    {
        node *n = malloc(sizeof(node)); // free this
        if (n == NULL)
        {
            return false;
        }

        int index = hash(new_word);
        strcpy(n->word, new_word);
        n->next = table[index];
        table[index] = n;

        counter += 1;
    }
    fclose(source);
    load_success = 1;
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (load_success == 1)
    {
        return counter;
    }
    else
    {
        return 0;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    if (load_success == 0)
    {
        return false;
    }
    for (int i = 0; i < N; i++)
    {
        node *ptr = table[i];
        while (ptr != NULL)
        {
            node *next = ptr->next;
            free(ptr);
            ptr = next;
        }
    }

    return true;
}
