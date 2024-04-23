import random
import sys

def main():
    level = get_integer("Level:")
    rand_num = random.randint(1, level)
    guess=-1
    while guess != rand_num:
        guess = get_integer("Guess:")
        if guess < rand_num:
            print("Too small!")
        elif guess > rand_num:
            print("Too large!")
    sys.exit("Just right!")


def get_integer(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return(n)
            else:
                pass
        except:
            pass
main()
