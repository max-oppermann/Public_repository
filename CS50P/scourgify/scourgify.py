import sys
import csv

try:
    open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

name, end = sys.argv[1].split(".")
if end != "csv":
    sys.exit("Not a CSV file")

with open(sys.argv[1]) as file:
    first_list = csv.DictReader(file)
    with open(sys.argv[2], "w", newline='') as file2:
            sec_list = csv.DictWriter(file2, fieldnames =["first", "last", "house"])
            sec_list.writeheader()
            for entry in first_list:
                last, first = entry["name"].split(",")
                sec_list.writerow({"first": first.strip(), "last": last, "house": entry["house"]})
