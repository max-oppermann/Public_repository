import csv

name = input("What’s your name? ")
home = input("Where’s your home? ")

with open("studentshomew.csv", "a") as file:
    w = csv.DictWriter(file, fieldnames=["name", "home"])
    w.writerow({"home": home, "name": name})
