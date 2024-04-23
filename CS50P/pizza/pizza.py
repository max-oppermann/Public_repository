'''


exactly 1 command line argument
must end in.csv
must start with regular or sicilian
FileNotFoundError


'''
import sys
import csv
from tabulate import tabulate

try:
    open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

name, end = sys.argv[1].split(".")
if end != "csv":
    sys.exit("Not a CSV file")

with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    headers = next(reader)
    table = []
    for row in reader:
        table.append(row)

print(tabulate(table, headers, tablefmt="grid"))
