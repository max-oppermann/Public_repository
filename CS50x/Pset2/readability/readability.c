#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

void count_l_s_w(char *str, int *counts);

int main(void)
{
    int counts[3] = {0, 0, 1}; // the last word wouldn't be counted, since text ends in punctuation
    string text = get_string("Text:");
    count_l_s_w(text, counts); // Idea from AI-duck; originally three different functions
    int l = counts[0];
    int s = counts[1];
    int w = counts[2];
    float l_hundred = ((float) l / w) * 100.0;
    float s_hundred = ((float) s / w) * 100.0;
    double grade = 0.0588 * l_hundred - 0.296 * s_hundred - 15.8; // >= 16: Grade 16+ < 1: Before Grade 1

    if (grade >= 1 && grade < 16)
    {
        printf("Grade %i\n", (int) round(grade));
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Before Grade 1\n");
    }
}

void count_l_s_w(char *str, int *counts)
{
    for (int i = 0, n = strlen(str); i < n; i++)
    {
        if (isalpha(str[i]))
        {
            counts[0]++; // the letters
        }
        else if (ispunct(str[i]) && str[i] != ',' && str[i] != '"' && str[i] != '\'' && str[i] != ':' && str[i] != ';' &&
                 str[i] != '-')
        {
            counts[1]++; // the sentences
        }
        else if (isblank(str[i]))
        {
            counts[2]++; // the words
        }
    }
}

/*
int num_letters(string text) // iterate through entire input string int isalpha(char c);
{
    int letters = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

int num_sentences(string text) // number of sentences = number of periods
{
    sentences = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (ispunct(text[i]) && text[i] != ",")
        {
            sentences++;
        }
    }
    return sentences;

}

int num_words(string text) // number of words = number of empty spaces
{

}



(#sentences/#words) times 100 = #sentences/100 words

printf("This is CS%i\n", (int) round(49.5));

*/
