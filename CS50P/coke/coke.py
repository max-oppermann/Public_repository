# coke.py [surprisingly hard]

balance = 50
while balance > 0:
    while True:
        print("Amount Due:", balance)
        insert = int(input("Insert Coin:"))
        if insert in {25, 10, 5}:
            break
    balance = balance - insert
print("Change Owed:", (-1*balance))
