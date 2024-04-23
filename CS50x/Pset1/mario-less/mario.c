#include <cs50.h>
#include <stdio.h>

void print_row(int bricks, int spaces);

int main(void)
{
    int x;
    do
    {
        x = get_int("Size of the pyramid: ");
    }
    while (x < 1);

    for (int i = 0; i < x; i++)
    {
        print_row(i + 1, x - i - 1);
        printf("\n");
    }
}
void print_row(int bricks, int spaces)
{
    for (int j = 0; j < spaces; j++)
    {
        printf(" ");
    }
    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }
}
