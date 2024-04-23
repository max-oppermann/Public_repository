# meal.py
def main():
    time = input("What time is it? ")
    t = convert(time)
    if 7 <= t <= 8:
        print("Breakfast time")
    if 12 <= t <= 13:
        print("Lunch time")
    if 18 <= t <= 19:
        print("Dinner time")


def convert(time):
    hrs, minutes = time.split(":")
    return float(hrs) + float(minutes)/60

if __name__ == "__main__":
    main()
