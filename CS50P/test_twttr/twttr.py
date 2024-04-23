

def main():
    inp = input("Input: ")
    print(shorten(inp))


def shorten(word):
    empty = ""
    for l in word:
        if l not in {"a", "e", "o", "i", "u", "A", "E", "I", "O", "U"}:
            empty += l
    return empty

if __name__ == "__main__":
    main()
