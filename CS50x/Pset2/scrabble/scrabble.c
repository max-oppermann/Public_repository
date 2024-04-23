#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int score(string word);

int main(void)
{
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    int score1 = score(word1);
    int score2 = score(word2);

    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int score(string word)
{
    int values[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    int score = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        int ascii = toupper(word[i]);
        if (ascii >= 65 && ascii <= 90)
        {
            int p = (ascii - 65);
            score += values[p];
        }
        else
        {
            score += 0;
        }
    }
    return score;
}

/*

toupper(input string [i])

position = 65 - (ASCII as integer) // because A = 65
go to values[position]
add that to a running counter

*/
