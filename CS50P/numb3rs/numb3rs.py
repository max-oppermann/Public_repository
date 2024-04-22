import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^((\d{1,3})\.){3}(\d{1,3})$", ip):
        for match in matches.group().split("."):
            try:
                x = int(match)
                if x < 256:
                    continue
                else:
                    return False
            except:
                return False
        return True

    else: return False



if __name__ == "__main__":
    main()



