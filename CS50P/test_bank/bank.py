
def main():
    greet = input("Greeting: ").strip().lower()
    print(value(greet))


def value(greeting):

    beginning_Hello = greeting.startswith("hello")
    beginning_h = greeting.startswith("h")

    if beginning_Hello:
        return 0
    elif beginning_h:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
