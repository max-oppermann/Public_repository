import sys
import inflect
p = inflect.engine()
from datetime import date

def main():
    birthday = get_bday() # this needs to be a date object
    today_ = date.today()
    delta = today_-birthday
    minutes_difference = round(delta.total_seconds() / 60)
    print(f"{date_to_words(minutes_difference)} minutes")

def get_bday():
    try:
        year, month, day = input("Date of Birth:").split("-")
    except:
        sys.exit("Invalid format")
    try:
        int(year)
        int(month)
        int(day)
        if int(year) not in range(10000) or int(month) not in range(1, 13) or int(day) not in range(1, 32):
            sys.exit("Invalid date")
    except:
        sys.exit("Invalid format")
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        sys.exit("Invalid format")

    bday = year + month + day
    return date.fromisoformat(bday)


def date_to_words(d):
    words = p.number_to_words(d, andword="").capitalize()
    return words


if __name__ == "__main__":
    main()


'''
words = p.number_to_words(1234, andword="")
 "one thousand, two hundred thirty-four"
Use datetime.date.today to get today’s date,
Exit via sys.exit if the user does not input a date in YYYY-MM-DD format.
    Or future date?



'''

