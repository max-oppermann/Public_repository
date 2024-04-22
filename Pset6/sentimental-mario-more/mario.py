import cs50


def main():
    while True:
        height = cs50.get_int("Height: ")
        if height > 0 and height < 9:
            break
    for i in range(height):
        print_row(i + 1, (height - i) - 1)
        print("  ", end="")
        print_row(i + 1, 0)
        print()


def print_row(bricks, spaces):
    for _ in range(spaces):
        print(" ", end="")
    for _ in range(bricks):
        print("#", end="")


main()
