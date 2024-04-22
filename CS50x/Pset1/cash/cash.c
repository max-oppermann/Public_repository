#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int change;
    do
    {
        change = get_int("Change: ");
    }
    while (change < 0);

    int coins[] = {25, 10, 5, 1}; // modified an idea from the duck-AI
    int total_coins = 0;
    for (int i = 0; i < 4; i++)
    {
        int remainder_i = change % coins[i];
        total_coins += (change - remainder_i) / coins[i];
        change = remainder_i;
    }
    printf("%i\n", total_coins);
}


