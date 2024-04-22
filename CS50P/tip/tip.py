def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.lstrip('$'))

    # should accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
    # remove the leading $, and return the amount as a float.


def percent_to_float(p):
    return float(p.rstrip('%'))/100

    # should accept a str as input (formatted as ##%, wherein each # is a decimal digit),
    # remove the trailing %, and return the percentage as a float.

main()
