from cs50 import get_string


def main():
    number = get_string("Number: ")

    if is_valid(number) and (len(number) in [13, 15, 16]):
        print(f"{which_card(number)}\n")
    else:
        print("INVALID\n")


def is_valid(number):
    sum = 0

    start_double = 0 if len(number) % 2 == 0 else 1
    start_single = 0 if start_double == 1 else 1

    for digit in number[start_double::2]:
        digit2 = int(digit) * 2
        sum += digit2 - 9 if digit2 > 9 else digit2
    for digit in number[start_single::2]:
        sum += int(digit)
    return sum % 10 == 0


def which_card(number):
    if number.startswith(("34", "37")) and len(number) == 15:
        return "AMEX\n"
    elif number.startswith(("51", "52", "53", "54", "55")) and len(number) == 16:
        return "MASTERCARD\n"
    elif number.startswith("4") and len(number) in [13, 16]:
        return "VISA\n"
    else:
        return "INVALID\n"


main()
