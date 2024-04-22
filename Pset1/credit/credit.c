#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int get_digit(long number, int place);
int get_length(long number);
int invalid_card(long number);
int is_valid(long number);
string which_card(long number);

int main(void)
{
    long number = get_long("Number: ");
    if (!is_valid(number) || (get_length(number) != 13 && get_length(number) != 15 && get_length(number) != 16) ||
        invalid_card(number) == 0)
    {
        printf("INVALID\n");
    }
    else
    {
        printf("%s", which_card(number));
    }
}

string which_card(long number)
{
    int length = get_length(number);
    if (length == 15)
    {
        return "AMEX\n";
    }
    else if (length == 13)
    {
        return "VISA\n";
    }
    else if (length == 16 && get_digit(number, 16) == 5)
    {
        return "MASTERCARD\n";
    }
    else
    {
        return "VISA\n";
    }
    // American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers.
    //  American Express start with 34 or 37; MasterCard numbers 51, 52, 53, 54, or 55; and all Visa numbers start with 4
}

int invalid_card(long number) // this checks the identifying digits
{
    int length = get_length(number);
    if (length == 16 && (get_digit(number, 16) != 4 && get_digit(number, 16) != 5)) // Mastercard 16, Visa 13 or 16
    {
        return 1 == 0;
    }
    else if (length == 13 && (get_digit(number, 13) != 4)) // Visa 13
    {
        return 1 == 0;
    }
    else if (length == 16 &&
             (get_digit(number, 16) == 5 && (get_digit(number, 15) < 1 || get_digit(number, 15) > 5))) // Mastercard second digit
    {
        return 1 == 0;
    }
    else if (length == 15 &&
             ((get_digit(number, 15) != 3) ||
              (get_digit(number, 14) != 4 && get_digit(number, 14) != 7))) // American Express numbers start with 34 or 37
    {
        return 1 == 0;
    }
    else
    {
        return !(1 == 0);
    }
}

int is_valid(long number) // this checks the checksum
{
    int length = get_length(number);

    int uneven_places = 0;
    for (int i = 1; i < length + 1; i += 2)
    {
        int digit_ue = get_digit(number, i);
        uneven_places += digit_ue;
    }

    int even_places = 0;
    for (int i = 2; i < length + 1; i += 2)
    {
        int digit_e = get_digit(number, i);
        if (digit_e * 2 > 9)
        {
            int sub_ten = get_digit(digit_e * 2, 1);
            int sub_one = get_digit(digit_e * 2, 2);
            even_places += (sub_ten + sub_one);
        }
        if (digit_e * 2 <= 9)
        {
            even_places += (digit_e * 2);
        }
    }
    return (uneven_places + even_places) % 10 == 0;
}

int get_length(long number) // alternatively, divide by 10 until you get 0 and increment a counter by 1 each time. This works since there are no leading 0’s
{
    char str[50];
    sprintf(str, "%ld", number); // much help from AI-duck
    return strlen(str);
}

int get_digit(long number, int place)
{
    long ten_power = (long) pow(10, place - 1); // pow() function from AI-duck
    return (number / ten_power) % 10;
}
