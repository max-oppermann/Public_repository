import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d+):?(\d*)? (AM|PM) to (\d+):?(\d*)? (PM|AM)$", s):
        hours1 = int(matches.group(1))
        time_1_2 = matches.group(2) # may be empty
        first_AMPM = matches.group(3)
        hours2 = int(matches.group(4))
        time_2_2 = matches.group(5) # may be empty
        second_AMPM = matches.group(6)

        try:
            minutes1 = int(time_1_2)
        except:
            minutes1 = 0
        try:
            minutes2 = int(time_2_2)
        except:
            minutes2 = 0

        if minutes1 > 59 or minutes2 > 59:
            raise ValueError
        if first_AMPM == "PM" and hours1 != 12:
            hours1 = int(hours1) +12
        if second_AMPM == "PM" and hours2 != 12:
            hours2 = int(hours2) +12
        if first_AMPM == "AM" and hours1 == 12:
            hours1 = 0
        if second_AMPM == "AM" and hours2 == 12:
            hours2 = 0
        return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"

    else: raise ValueError


if __name__ == "__main__":
    main()
