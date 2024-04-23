# fuel.py

def main():
    while True:
        try:
            inp = input("Fraction:")
            frac = convert(inp)
            break
        except:
            pass
    print(gauge(frac))

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


def convert(fraction):
    num, slash, denom = fraction.partition("/")
    try:
        num_i = int(num)
        denom_i = int(denom)
        frac = round(100*(num_i/denom_i))
        if frac > 100:
            raise ValueError
    except ValueError:
        raise
    except ZeroDivisionError:
        raise
    return frac


if __name__ == "__main__":
    main()
