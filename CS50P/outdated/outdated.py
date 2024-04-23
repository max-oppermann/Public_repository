# outdated.py

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]




def check_date():
    while True:
        date = input("Date:").strip()
        if "/" in date:
            d1 = date.split("/")
            try:
                x = int(d1[0])
                y = int(d1[1])
                z = int(d1[2])

                if x in range(1, 13) and y in range(1, 32) and z > 0:
                    print(f"{d1[2]}-{x:02}-{y:02}")
                    break
            except:
                pass

        elif "," in date:
            d2 = date.split(" ")
            remove_comma = d2[1].rstrip(",") # day_comma
            try:
                a = d2[0]
                b = int(remove_comma)
                c = int(d2[2])

                if a.isalpha() and a in months and b in range(1, 32) and c > 0:
                    print(f"{c}-{months.index(a)+1:02}-{b:02}")
                    break
            except:
                pass

check_date()


