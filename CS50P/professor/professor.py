# professor.py

import random



def main():
    level = get_level()

    wrong = 0
    m = 1
    for m in range(1, 11):

        sum1 = generate_integer(level)
        sum2 = generate_integer(level)
        attempt = 1
        while True:
            while True:
                try:
                    answer = int(input(f"{sum1} + {sum2} ="))
                    break
                except:
                    print("EEE")
                    continue
            if answer != sum1 + sum2:
                print("EEE")
                attempt += 1
                if attempt not in range(1, 4):
                    print(sum1, "+", sum2, "=", sum1+sum2)
                    m += 1
                    wrong += 1
                    break
            else:
                break

        if answer == sum1 + sum2:
            m += 1
            continue
    print("Score:", 10-wrong)



def get_level():
    while True:
        try:
            n = int(input())
            if n in [1, 2, 3]:
                return(n)
            else:
                pass
        except:
            pass



def generate_integer(level): # random.randrange(start, stop[, step])
    if level ==1:
        rand_int = random.randrange(0, 10)
    else:
        rand_int = random.randrange(10**(level-1), 10**level)
    return rand_int




if __name__ == "__main__":
    main()
