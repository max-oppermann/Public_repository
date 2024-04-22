# plate.py

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() and s[0:2].isalpha() and 2 <= len(s) <= 6 and first_null(s) and middle_num(s):
        return True

def first_null(string):
    if "0" not in string:
        return True
    elif "0" in string:
        first, null, junk = string.partition("0")
        return not first.isalpha()


def middle_num(string):
    for i in range(len(string)-1):
        if string[i].isdigit() and string[i + 1].isalpha():
            return False
    return True


if __name__ == "__main__":
    main()
