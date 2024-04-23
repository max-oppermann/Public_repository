
import sys

try:
    open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

name, end = sys.argv[1].split(".")
if end != "py":
    sys.exit("Not a Python file")

counter = 0

with open(sys.argv[1]) as file:
    for line in file:
        if line.lstrip().startswith("#"):
            continue
        elif line.strip() == "":
            continue
        else:
            counter += 1

print(counter)
